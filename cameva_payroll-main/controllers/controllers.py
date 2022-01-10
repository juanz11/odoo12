# -*- coding: utf-8 -*-
from odoo import http

# class CamevaPayroll(http.Controller):
#     @http.route('/cameva_payroll/cameva_payroll/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cameva_payroll/cameva_payroll/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cameva_payroll.listing', {
#             'root': '/cameva_payroll/cameva_payroll',
#             'objects': http.request.env['cameva_payroll.cameva_payroll'].search([]),
#         })

#     @http.route('/cameva_payroll/cameva_payroll/objects/<model("cameva_payroll.cameva_payroll"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cameva_payroll.object', {
#             'object': obj
#         })