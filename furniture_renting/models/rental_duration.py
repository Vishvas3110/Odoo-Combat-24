# -*- coding: utf-8 -*-
from odoo import models, fields, api

class RentalDuration(models.Model):
    _name = 'rental.duration'

    name = fields.Char("Name")
    code = fields.Char("Code")
    value = fields.Integer("Value")