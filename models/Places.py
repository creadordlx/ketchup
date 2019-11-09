from odoo import api, fields, models


class KetchupPlaces(models.Model):
    _name = "ketchup.places"
    _description = "List of Places to visit"

    name = fields.Char(string='name', size=128)
    price = fields.Float(string='price', default=0)
    photo_ids = fields.One2many('ir.attachment', 'place_id', string='photo_ids')
    type = fields.Selection(string='type', selection=[(0, 'Hot'), (1, 'New'), (2, 'Popular')])

    tour_ids = fields.Many2many('ketchup.tours', string='tour_ids')
    blog_id = fields.One2many('ketchup.blog', 'place_id', string='blog_id')


class KetchupAttachment(models.Model):
    _inherit = 'ir.attachment'

    place_id = fields.Many2one('ketchup.places', string='place_id')
    blog_ids = fields.Many2many('ketchup.blog', string='blog_ids')