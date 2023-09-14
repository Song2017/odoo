# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "TMS",
    'version': '1.0',
    'depends': ["base"],
    'author': "Ben Song",
    'category': 'Inventory/Inventory',
    'description': """  TMS 国际运输管理系统  """,
    'data': [
        # 'security/crm_security.xml',
        'security/ir.model.access.csv',

        'views/aaa_views.xml'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
