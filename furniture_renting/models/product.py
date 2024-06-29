# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    rental_ok = fields.Boolean("Can be Rental")
    product_rental_price_ids = fields.One2many('product.rental.price', 'product_template_id', string='Rental Pricing')


class ProductRentalPrice(models.Model):
    _name = 'product.rental.price'

    product_template_id = fields.Many2one("product.template", "Product Template")
    duration_id = fields.Many2one("rental.duration", 'Duration')
    price = fields.Float('Price')