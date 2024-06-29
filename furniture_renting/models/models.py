# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class furniture_renting(models.Model):
#     _name = 'furniture_renting.furniture_renting'
#     _description = 'furniture_renting.furniture_renting'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

