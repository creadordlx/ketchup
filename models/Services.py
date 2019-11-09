from odoo import api, fields, models


class KetchupServices(models.Model):
    _name = "ketchup.services"
    _description = "List of Services"

    name = fields.Char(string='name', size=128)
    content = fields.Text(string='content')
    price = fields.Integer(string='price', default=0)
    tour_ids = fields.Many2many('ketchup.tours', string='tour_ids')
    description = fields.Text(string="Описание")
    photo_ids = fields.One2many('ir.attachment', 'service_id', string='photo_ids')