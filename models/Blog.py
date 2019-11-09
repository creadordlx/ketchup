from odoo import fields, models


class KetchupBlog(models.Model):
    _name = "ketchup.blog"
    _description = "List of Blog"

    name = fields.Char(string='name', size=128, required=True)
    place_id = fields.Many2one('ketchup.places', string='place_id')
    tour_id = fields.Many2one('ketchup.tours', string='tour_id')
    photo_ids = fields.One2many('ir.attachment', 'blog_id', string='photo_ids')

    content = fields.Text(string='content')
