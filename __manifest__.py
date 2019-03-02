# -*- coding: utf-8 -*-
{
    'name': "music",

    'summary': """
        Musical group ERP module
    """,

    'description': """
        Musical group ERP module
    """,

    'author': "jev",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Music',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/key.xml',
        'views/views.xml',
        'views/templates.xml',
        'datas/datas.xml'
    ],
}