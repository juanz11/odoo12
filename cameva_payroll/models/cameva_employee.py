from cameva_payroll.models.cameva_payroll import Payslip
from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime


class CamevaEmploye(models.Model):

    _inherit = 'hr.employee'
    
    shoes = fields.Selection([('34', '34'), ('35', '35'), ('36', '36'),('37', '37'),('38', '38'),('39', '39'),('40', '40'),('41', '41'),('42', '42'),('43', '43'),('44', '44'),('45', '45'),('46', '46')], string='Zapatos')
    zone3 = fields.Selection([('26', '26'),('28', '28'),('30', '30'),('32', '32'),('34', '34'),('36', '36'),('38', '38'),('40', '40')], string='Pantalon')
    zone4 = fields.Selection([('X', 'XS'), ('S', 'S'), ('M', 'M'),('L', 'L'),('XL', 'XL'),('XXL', 'XXL')], string='Camisa')
    zone5 = fields.Selection([('X', 'XS'), ('S', 'S'), ('M', 'M'),('L', 'L'),('XL', 'XL'),('XXL', 'XXL')], string='Chemise') 
    zone7 = fields.Selection([('O', 'O+'),('ON', 'O-'),('A', 'A-'),('Ap', 'A+'),('Bn', 'B-'),('Bp', 'B+'),('ABn', 'AB-'),('AB', 'AB+')], string='Grupo sanguíneo')
    alergia = fields.Text()
    vacuna = fields.Selection([('S','Si'),('N','No')])
    dosis= fields.Text()
    ndosis=fields.Selection([('1','1'),('2','2'),('3','3')])

    allergy_type = fields.Many2one('hr.employee.allergy','Select an allergy type')
    supermarket = fields.Many2one('hr.supermarket',string="Supermercado",required=False)

    def payslip_instance(self):
        return self.env["hr.payslip"]
    
    @api.multi
    def calculate_massive_payroll(self):
        payslip_instance = self.payslip_instance()
        code = payslip_instance.search_count([])

        for employee in self:
            _payslip = {
                'name': "Nomina para " + employee.name,
                'struct_id':employee.contract_id.struct_id['id'],
                'employee_id':employee['id'],
                'number': "SPL " + str(code),
                'state': "draft",
                'company_id':employee.company_id['id'],
                'paid':False,
                'contract_id':employee.contract_id['id'],
                'credit_note':False,
                'date_from':datetime.now().strftime('%Y-%m-%d')
            }

            payslip_instance.create(_payslip)
            code = code + 1





class HrEmployeeAllergy(models.Model):
    _name = 'hr.employee.allergy'
    _descriptions = 'Allergies'
    
    name = fields.Char(required='true')
    relation = fields.One2many('hr.employee','allergy_type')


class HrSupermarket(models.Model):
    _name = 'hr.supermarket'
    _description = 'Supermarket info'

    supermarket_id = fields.One2many('hr.employee','supermarket')
    name = fields.Char(string='Nombre supermercado',required=True)
    address = fields.Text(string='Dirección',required=True)
    responsable = fields.Many2one('hr.employee',string='Responsable',required=True)



    


     