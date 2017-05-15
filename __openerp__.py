# -*- coding: utf-8 -*-
{
    'name': "Amount To Text Arabic (Algeria)",

    'summary': """
        This Module converts the amount of the invoice/order to Arabic text.
        it's also supporting the current Currency symbol.
        """,

    'description': """
        This Module converts the amount of the invoice/order to Arabic
        it's also supporting the current Currency symbol.
        For more details or support please contact us at:
        contact@3t-solutions.net
    """,

    'author': "EURL 3TSolutions",
    'website': "http://www.3t-solutions.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Localization',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'account'],

    # always loaded
    'data': [
        'views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}