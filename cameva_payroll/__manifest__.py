# -*- coding: utf-8 -*-
{
    'name': "cameva_payroll",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'hr_payroll'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/employee_views.xml',
        'views/templates.xml',
        'views/salary_rule.xml',
        'views/allergy_views.xml',
        'views/blood_views.xml',
        'views/uniforms_views.xml',
        'views/pants_views.xml',
        'views/shirt_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}