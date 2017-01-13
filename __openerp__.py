# -*- coding: utf-8 -*-

{
    'name': 'Products filter by Supplier',
    'description': """Products filter by Supplier in RFQ/PO.""",
    'summary': 'Products filter by Supplier',
    'version': '1.0',
    'author': 'CogitoWeb',
    'category': 'Purchase',
    'depends': ['purchase'],
    'data': [
        'purchase_view.xml',
		'product_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}

