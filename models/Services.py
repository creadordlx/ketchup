from odoo import api, fields, models


class KetchupServices(models.Model):
    _name = "ketchup.services"
    _description = "List of Services"

    name = fields.Char(string='Название', size=128)
    content = fields.Text(string='Содержимое')
    price = fields.Integer(string='Цена', default=0)
    tour_ids = fields.Many2many('ketchup.tours', string='Туры')
    description = fields.Text(string="Описание")
    photo_ids = fields.One2many('ir.attachment', 'service_id', string='Фотографии')
