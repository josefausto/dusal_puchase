# -*- coding: utf-8 -*-
##############################################################################
#
#    Addon for Odoo sale by Dusal.net
#    Copyright (C) 2015 Dusal.net Almas
#
##############################################################################


from openerp import models, fields, osv

class purchase_order(models.Model):
    _inherit = 'purchase.order'


    print_image = fields.Boolean('Print image', readonly=False, help="Print Quotation with product images", default=True)
    image_size = fields.Selection([('small', 'Small'), ('medium', 'Medium'), ('original', 'Big')], 'Image sizes', help="Choose an image size here", default='small')
    print_line_number = fields.Boolean('Print line number', readonly=False, help="Print line number on Sales order & Quotation", default=False)

class purchase_order_line(models.Model):
    _inherit = 'purchase.order.line'

    product_image = fields.Binary(string="Image", related="product_id.image")
    product_image_medium = fields.Binary(string="Image", related="product_id.image_medium")
    product_image_small = fields.Binary(string="Image", related="product_id.image_small")
