# -*- coding: utf-8 -*-
{
    'name': "leaders_app",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "MT CONSULTING SARL",
    'website': "http://www.mtconsulting.cm",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/leaders_apprenant.xml',
        'views/leaders_config.xml',
        'views/leaders_employe.xml',
        'views/leaders_concours_blanc.xml',

        #WIZARD
        'wizard/wizard_resultats_concours_blanc.xml',

         'menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
