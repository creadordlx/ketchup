from odoo import api, fields, models


class KetchupTours(models.Model):
    _name = "ketchup.tours"
    _description = "List of Tours"

    name = fields.Char('name', size=128)
    place_ids = fields.Many2many('ketchup.places', string='place_ids')
    total_price = fields.Float(default=0, string='price')

