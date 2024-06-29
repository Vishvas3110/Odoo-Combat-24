# -*- coding: utf-8 -*-
{
    'name': "FurnitureRenting",
    'summary': "Manage furniture rentals and bookings",
    'description': """
        Manage furniture rentals and bookings
    """,
    'author': "Odoo Combat",
    'website': "",
    'category': 'FurnitureRenting/FurnitureRenting',
    'version': '0.1',
    'depends': ['base', 'product', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/product.xml',
        'views/sale.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

