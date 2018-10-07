# -*- coding: utf-8 -*-
##############################################################################
#
#    Addon for Odoo sale by Dusal.net
#    Copyright (C) 2015 Dusal.net Almas
#
##############################################################################


{
    "name" : "Product images on Purchase order and Quotation",
    "summary" : "Useful extension for Odoo Purchase",
    "version" : "3.0",
    "description": """
        Add numbering and image (product picture, product photo)(picture, photo) of products on list view and print (pdf) of product lines. If you want images on Sales order then please check my other addons. Support and contact email: almas@dusal.net
    """,
    'author' : 'Dusal Solutions',
    'support': 'almas@dusal.net',
    #'website' : 'http://dusal.net',
    'license': 'Other proprietary',
    'category' : 'Purchases',
    'price': 10.00,
    'currency': 'EUR',
    'images': ['static/images/main_screenshot.png', 'static/images/screenshot1.png', 'static/images/edit_line_screenshot.png', 'static/images/screenshot.png'],
    "depends" : [
                 "purchase",
                 "product",
    ],
    "data" : [
                'data.xml',
                'views/views.xml',
                'views/report_purchasequotation.xml',
                'views/report_purchaseorder.xml',
                ],
    "auto_install": False,
    "installable": True,
}
