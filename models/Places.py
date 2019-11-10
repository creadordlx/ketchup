from odoo import api, fields, models


class KetchupPlaces(models.Model):
    _name = "ketchup.places"
    _description = "List of Places to visit"

    name = fields.Char(string='Название', size=128)
    price = fields.Integer(string='Цена', default=0)
    photo_ids = fields.One2many('ir.attachment', 'place_id', string='Фотографии')
    description = fields.Text(string='Описание')
    rating = fields.Float(string="Рейтинг")

    tour_ids = fields.Many2many('ketchup.tours', string='Туры')
    blog_ids = fields.One2many('ketchup.blog', 'place_id', string='Рецензии')


class KetchupAttachment(models.Model):
    _inherit = 'ir.attachment'

    place_id = fields.Many2one('ketchup.places', string='Место')
    blog_ids = fields.Many2many('ketchup.blog', string='Рецензии')
