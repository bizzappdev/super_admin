# -*- coding: utf-8 -*-
{
    'name': 'Super Admin',
    'version': '1.0',
    'category': '',
    "sequence": 14,
    'complexity': "easy",
    'category': 'Hidden',
    'description': """
        Mark All Super Admin users as member of all group by default
    """,
    'author': 'Ruchir Shukla',
    'website': 'www.bizzappdev.com',
    'depends': [],
    'init_xml': [],
    'update_xml': [
        "base_view.xml",
    ],
    'demo_xml': [],
    'test': [
    ],
    'css' : [
        "static/src/css/base.css",
    ],
    'js': ['static/src/js/attachment.js'],
    'installable': True,
    'auto_install': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
