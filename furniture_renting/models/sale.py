# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_rental_order = fields.Boolean("Is Rental Order")

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_rental_product = fields.Boolean(related="product_id.rental_ok")
    duration_value = fields.Integer('Duration')
    duration_id = fields.Many2one("rental.duration", 'Duration Type')
    valid_from = fields.Datetime("Valid From")
    valid_to = fields.Datetime("Valid To")
    qty_returned = fields.Float("Returned")