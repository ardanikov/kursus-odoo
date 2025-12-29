# -*- coding: utf-8 -*-
{
    'name': "Kursus",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Aplikasi untuk mengelola kursus
    """,

    'author': "Cendana2000",
    'website': "https://www.cendana2000.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '18.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'product', 'account'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/ir_action_report_data.xml',
        'views/menu_kursus.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/kursus.xml',
        'views/kursus_session.xml',
        'views/instruktur.xml',
        'views/provinsi.xml',
        'views/kota.xml',
        'views/kecamatan.xml',
        'views/desa.xml',
        'views/peserta.xml',
        'views/product_inherit.xml',
        'views/pendaftaran.xml',
        'views/daftar_hadir.xml',
        'wizards/kursus_wizard.xml',
        'reports/peserta-card.xml',
        'reports/daftar-hadir-report.xml',
        'reports/pendaftaran_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

