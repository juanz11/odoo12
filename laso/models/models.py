	# -*- coding: utf-8 -*-

from odoo import models	, fields, api
import datetime


class Visit(models.Model):
    _name = 'custom_crm.visit'
    _description = 'Visit'

    name = fields.Char(string='Descripción')
    customer = fields.Many2one(string='Cliente', comodel_name='res.partner')
    date = fields.Datetime(string='Fecha')
    type = fields.Selection([('P', 'Presencial'), ('W', 'WhatsApp'), ('T', 'Telefónico')], string='Tipo', required=True)
    done = fields.Boolean(string='Realizada', readonly=True)
    image = fields.Binary(string='Imagen')

    def toggle_state(self):
        self.done = not self.done

    #ORM
    def f_create(self):
        visit = {
            'name': 'ORM test',
            'customer': 1,
            'date': str(datetime.date(2020, 8, 6)),
            'type': 'P',
            'done': False
        }
        print(visit)
        self.env['custom_crm.visit'].create(visit)

    def f_search_update(self):
        visit = self.env['custom_crm.visit'].search([('name', '=', 'ORM test')])
        print('search()', visit, visit.name)

        visit_b = self.env['custom_crm.visit'].browse([8])
        print('browse()', visit_b, visit_b.name)

        visit.write({
            'name': 'ORM test write'
        })

    def f_delete(self):
        visit = self.env['custom_crm.visit'].browse([8])
        visit.unlink()


class VisitReport(models.AbstractModel):

    _name='report.custom_crm.report_visit_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('custom_crm.report_visit_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['custom_crm.visit'],
            'docs': self.env['custom_crm.visit'].browse(docids)
        }


class CustomSaleOrder(models.Model): #

    _inherit = 'sale.order' # nos permite modificar el modelo que vamos a especificar

    zone = fields.Selection([('N', 'Nose'), ('C', 'Caracas'), ('S', 'Sureste')], string='Zona comercial')


class CustomEmploye(models.Model): #

    _inherit = 'hr.employee' # nos permite modificar el modelo que vamos a especificar
    
    zone2 = fields.Selection([('34', '34'), ('35', '35'), ('36', '36'),('37', '37'),('38', '38'),('39', '39'),('40', '40'),('41', '41'),('42', '42'),('43', '43'),('44', '44'),('45', '45'),('46', '46')], string='Zapatos')
    zone3 = fields.Selection([('26', '26'),('27', '27'),('28', '28'),('29', '29'),('30', '30'),('32', '32'),('33', '33'),('34', '34'),('35', '35'),('36', '36'),('37', '37'),('38', '38'),('39', '39'),('40', '40')], string='Pantalon')
    zone4 = fields.Selection([('X', 'XS'), ('S', 'S'), ('M', 'M'),('L', 'L'),('XL', 'XL'),('XXL', 'XXL')], string='Camisa')
    zone5 = fields.Selection([('X', 'XS'), ('S', 'S'), ('M', 'M'),('L', 'L'),('XL', 'XL'),('XXL', 'XXL')], string='Chemise') 
    zone6 = fields.Selection([('A','Alimentos'),('F','Fármacos'),('As','Asma alérgico'),('Anl','Animales'),('Da','Dermatitis atópica'),('Pn','Poliposis nasal'),('Ra','Rinitis alérgica'),('Uc','Urticaria'),('Niq','Níquel'),('Sus','Sustancias'),('Ot','Otras'),('Ni','Ninguna')], string='Tipo de alergia')
    zone7 = fields.Selection([('O', 'O+'),('ON', 'O-'),('A', 'A-'),('Ap', 'A+'),('Bn', 'B-'),('Bp', 'B+'),('ABn', 'AB-'),('AB', 'AB+')], string='Grupo sanguíneo')
    alergia = fields.Text()
    vacuna = fields.Selection([('S','Si'),('N','No')])
    dosis= fields.Text()
    ndosis=fields.Selection([('1','1'),('2','2'),('2','2')])
 