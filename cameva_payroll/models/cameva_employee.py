from odoo import models, fields, api
from odoo.exceptions import UserError


class CamevaEmploye(models.Model): #

    _inherit = 'hr.employee' # nos permite modificar el modelo que vamos a especificar
    
    shoes = fields.Selection([('34', '34'), ('35', '35'), ('36', '36'),('37', '37'),('38', '38'),('39', '39'),('40', '40'),('41', '41'),('42', '42'),('43', '43'),('44', '44'),('45', '45'),('46', '46')], string='Zapatos')
    zone3 = fields.Selection([('26', '26'),('28', '28'),('30', '30'),('32', '32'),('34', '34'),('36', '36'),('38', '38'),('40', '40')], string='Pantalon')
    zone4 = fields.Selection([('X', 'XS'), ('S', 'S'), ('M', 'M'),('L', 'L'),('XL', 'XL'),('XXL', 'XXL')], string='Camisa')
    zone5 = fields.Selection([('X', 'XS'), ('S', 'S'), ('M', 'M'),('L', 'L'),('XL', 'XL'),('XXL', 'XXL')], string='Chemise') 
    zone6 = fields.Selection([('A','Alimentos'),('F','Fármacos'),('As','Asma alérgico'),('Anl','Animales'),('Da','Dermatitis atópica'),('Pn','Poliposis nasal'),('Ra','Rinitis alérgica'),('Uc','Urticaria'),('Niq','Níquel'),('Sus','Sustancias'),('Ot','Otras'),('Ni','Ninguna')], string='Tipo de alergia')
    zone7 = fields.Selection([('O', 'O+'),('ON', 'O-'),('A', 'A-'),('Ap', 'A+'),('Bn', 'B-'),('Bp', 'B+'),('ABn', 'AB-'),('AB', 'AB+')], string='Grupo sanguíneo')
    alergia = fields.Text()
    vacuna = fields.Selection([('S','Si'),('N','No')])
    dosis= fields.Text()
    ndosis=fields.Selection([('1','1'),('2','2'),('3','3')])