# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.safe_eval import safe_eval 

from datetime import date, datetime, time
from pytz import timezone


class SalaryRule(models.Model):
    _inherit = 'hr.salary.rule'
    _description = 'Custom Salary Rule: Extending hr.salary.rule'

    #TODO should add some checks on the type of result (should be float)
    @api.multi
    def _compute_rule(self, localdict):
        """
        :param localdict: dictionary containing the environement in which to compute the rule
        :return: returns a tuple build as the base/amount computed, the quantity and the rate
        :rtype: (float, float, float)
        """
        self.ensure_one()
        if self.amount_select == 'fix':
            try:
                return self.amount_fix, float(safe_eval(self.quantity, localdict)), 100.0
            except:
                raise UserError(('Wrong quantity defined for salary rule %s (%s).') % (self.name, self.code))
        elif self.amount_select == 'percentage':
            try:
                return (float(safe_eval(self.amount_percentage_base, localdict)),
                        float(safe_eval(self.quantity, localdict)),
                        self.amount_percentage)
            except:
                raise UserError(('Wrong percentage base or quantity defined for salary rule %s (%s).') % (self.name, self.code))
        else:
            try:
                safe_eval(self.amount_python_compute, localdict, mode='exec', nocopy=True)
                #El resultado del codigo ahora se multiplica por el campo cantidad
                '''
                    Pensado para las reglas salariales:
                        Horas extras diurnas y nocturnas
                        Dias feriados y descanso trabajados
                '''
                localdict['result_qty'] = float(self.quantity)
                localdict['result'] = float(localdict['result']) * float(self.quantity)

                return (localdict['result'], 
                        'result_qty' in localdict and localdict['result_qty'] or 1.0, 
                        'result_rate' in localdict and localdict['result_rate'] or 100.0)
            except:
                raise UserError(('Wrong python code defined for salary rule %s (%s).') % (self.name, self.code))



class Payslip(models.Model):
    _inherit = 'hr.payslip'
    _descrption = 'Cameva Payroll module: Extending HRPayslip odoo model'

    @api.model
    @api.depends('date_from','date_to')
    def get_worked_day_lines(self, contracts, date_from, date_to):
        """
        @param contract: Browse record of contracts
        @return: returns a list of dict containing the input that should be applied for the given contract between date_from and date_to
        """
        res = []
        # fill only if the contract as a working schedule linked
        for contract in contracts.filtered(lambda contract: contract.resource_calendar_id):
            day_from = datetime.combine(fields.Date.from_string(date_from), time.min)
            day_to = datetime.combine(fields.Date.from_string(date_to), time.max)

            # compute leave days
            leaves = {}
            calendar = contract.resource_calendar_id
            tz = timezone(calendar.tz)
            day_leave_intervals = contract.employee_id.list_leaves(day_from, day_to, calendar=contract.resource_calendar_id)
            for day, hours, leave in day_leave_intervals:
                holiday = leave[:1].holiday_id
                current_leave_struct = leaves.setdefault(holiday.holiday_status_id, {
                    'name': holiday.holiday_status_id.name or ('Global Leaves'),
                    'sequence': 5,
                    'code': holiday.holiday_status_id.name.upper() or 'GLOBAL',
                    'number_of_days': 0.0,
                    'number_of_hours': 0.0,
                    'contract_id': contract.id,
                })
                current_leave_struct['number_of_hours'] += hours
                work_hours = calendar.get_work_hours_count(
                    tz.localize(datetime.combine(day, time.min)),
                    tz.localize(datetime.combine(day, time.max)),
                    compute_leaves=False,
                )
                if work_hours:
                    current_leave_struct['number_of_days'] += hours / work_hours

            # compute contract worked days
            work_data = contract.employee_id.get_work_days_data(day_from, day_to, calendar=contract.resource_calendar_id)
            attendances = {
                'name': ("Normal Working Days paid at 100%"),
                'sequence': 1,
                'code': 'WORK100',
                'number_of_days': work_data['days'],
                'number_of_hours': work_data['hours'],
                'contract_id': contract.id,
            }

            # compute contract worked days
            work_data = contract.employee_id.get_work_days_data(day_from, day_to, calendar=contract.resource_calendar_id)
            contract_days = {
                'name': ("Normal Working Days paid at 100%"),
                'sequence': 1,
                'code': 'WORK100',
                'number_of_days': work_data['days'],
                'number_of_hours': work_data['hours'],
                'contract_id': contract.id,
            }

            # computando dias de asistencia
            work_data = {
                'attendance': contract.employee_id.attendance_ids,
                'days': 0.0,
                'hours': 0.0
            }
            
            for att in work_data['attendance']:
                if self.date_from <= att.check_in.date() <= self.date_to:
                    work_data['hours'] += att.worked_hours
                    work_data['days'] = work_data['hours'] / 8 

            attendances = {
                'name': ("Attendance"),
                'sequence': 3,
                'code': 'ATTENDANCE',
                'number_of_days': work_data['days'],
                'number_of_hours': work_data['hours'],
                'contract_id': contract.id,
            }

            res.append(contract_days)
            res.append(attendances)
            res.extend(leaves.values())
        return res


        '''
            Estructura de las lineas de Dias trabajados

            linea = {
                'name': ("Asistencias del sistema"),
                'sequence': 3,
                'code': 'ATTENDANCE',
                'number_of_days': work_data['days'],
                'number_of_hours': work_data['hours'],
                'contract_id': contract.id,
            }


            leaves.values() expande todos los objetos de leaves
        '''




