# -*- coding: utf-8 -*-

{
    'name': "Library Books",
    'summary': "Manage your books",
    'description': """Long description""",
    'author': "Nebil Aydi",
    'license': "AGPL-3",
    'website': "http://www.example.com",
    'category': 'Uncategorized',
    'version': '11.0.1.0.1',
    'depends': ['base', 'decimal_precision', 'stock'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',

        'data/res_partner.xml',

        'views/library_book.xml',
    ],
    'demo': [
        'demo/demo.xml'
    ],
}
