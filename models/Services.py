from odoo import api, fields, models


class KetchupServices(models.Model):
    _name = "ketchup.services"
    _description = "List of Services"

    name = fields.Char(string='name', size=128)
    content = fields.Text(string='content')
    price = fields.Float(string='price', default=0)
    tour_ids = fields.Many2many('ketchup.tours', string='tour_ids')