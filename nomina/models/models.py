# -*- coding: utf-8 -*-

from typing import SupportsFloat
from odoo import models, fields, api

# class nomina(models.Model):
#     _name = 'nomina.nomina'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100