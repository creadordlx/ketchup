from odoo import fields, models


class KetchupBlog(models.Model):
    _name = "ketchup.blog"
    _description = "List of Blog"

    name = fields.Char(string='name', size=128, required=True)
    place_id = fields.Many2one(string='Достопримечательность', comodel_name='ketchup.places')
    tour_id = fields.Many2one('ketchup.tours', string='Тур')
    photo_ids = fields.One2many('ir.attachment', 'blog_id', string='Фотографии')

    content = fields.Text(string='Содержимое')
