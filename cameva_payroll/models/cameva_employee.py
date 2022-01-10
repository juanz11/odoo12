from odoo import models, fields, api
from odoo.exceptions import UserError
import base64


class CamevaEmploye(models.Model): #

    _inherit = 'hr.employee' # nos permite modificar el modelo que vamos a especificar
    
  #  shoes = fields.Selection([('34', '34'), ('35', '35'), ('36', '36'),('37', '37'),('38', '38'),('39', '39'),('40', '40'),('41', '41'),('42', '42'),('43', '43'),('44', '44'),('45', '45'),('46', '46')], string='Zapatos')
  #  zone3 = fields.Selection([('26', '26'),('28', '28'),('30', '30'),('32', '32'),('34', '34'),('36', '36'),('38', '38'),('40', '40')], string='Pantalon')
    zone4 = fields.Selection([ ('S', 'S'), ('M', 'M'),('L', 'L'),('XL', 'XL'),('XXL', 'XXL')], string='Camisa')
    zone5 = fields.Selection([ ('S', 'S'), ('M', 'M'),('L', 'L'),('XL', 'XL'),('XXL', 'XXL')], string='Chemise') 
    zone6 = fields.Selection([('A','Alimentos'),('F','Fármacos'),('As','Asma alérgico'),('Anl','Animales'),('Da','Dermatitis atópica'),('Pn','Poliposis nasal'),('Ra','Rinitis alérgica'),('Uc','Urticaria'),('Niq','Níquel'),('Sus','Sustancias'),('Ot','Otras'),('Ni','Ninguna')], string='Tipo de alergia')
    zone7 = fields.Selection([('O', 'O+'),('ON', 'O-'),('A', 'A-'),('Ap', 'A+'),('Bn', 'B-'),('Bp', 'B+'),('ABn', 'AB-'),('AB', 'AB+')], string='Grupo sanguíneo')
    alergia = fields.Text()
    dosis= fields.Char()
    ndosis=fields.Selection([('1','1'),('2','2'),('3','3')])
    sale_ok = fields.Boolean('Se encuentra vacunado', default=True)


  

    allergy_type = fields.Many2one('hr.employee.allergy','Tipo de alergia')
    uniforms_size = fields.Many2one('hr.employee.uniforms','Zapatos')
    pants_size = fields.Many2one('hr.employee.pants', 'Pantalon')
    shirt_size = fields.Many2one('hr.employee.shirt','Shirt')

class HrEmployeeAllergy(models.Model):
    _name = 'hr.employee.allergy'
    _descriptions = 'Allergies'
    
    name = fields.Char(required='true')
    relation = fields.One2many('hr.employee','allergy_type')

class HrEmployeeUniforms(models.Model):
    _name = 'hr.employee.uniforms'
    _descriptions = 'uniforms'

    name = fields.Integer(required= 'true')
    relation = fields.One2many('hr.employee','uniforms_size')

class HrEmployeePants(models.Model):
    _name = 'hr.employee.pants'
    _descriptions = 'pants'

    name = fields.Integer(required= 'true')
    relation = fields.One2many('hr.employee','pants_size')

class HrEmployeeShirt(models.Model):
    _name = 'hr.employee.shirt'
    _descriptions = 'Shirt'

    name = fields.Integer(required= 'true')
    relation = fields.One2many('hr.employee','shirt_size')

     