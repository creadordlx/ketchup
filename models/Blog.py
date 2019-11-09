from odoo import fields, models


class KetchupBlog(models.Model):
    _name = "ketchup.blog"
    _description = "List of Blog"

    name = fields.Char(string='name', size=128)
    place_id = fields.Many2one('ketchup.places', string='place_id')
    photo_ids = fields.Many2many('ir.attachment', string='photo_ids')

    content = fields.Text(string='content')
