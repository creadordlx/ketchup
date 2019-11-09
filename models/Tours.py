from odoo import api, fields, models


class KetchupTours(models.Model):
    _name = "ketchup.tours"
    _description = "List of Tours"

    name = fields.Char('name', size=128)
    description = fields.Text('description')
    rating = fields.Float('rating', default=0.0)

    place_ids = fields.Many2many('ketchup.places', string='place_ids')
    blog_id = fields.One2many('ketchup.blog', 'tour_id', string='blog_id')
    service_ids = fields.Many2many('ketchup.services', string='service_ids')
    photo_ids = fields.Many2many('ir.attachment', string='photo_ids')
    type = fields.Selection(string='type', selection=[(0, 'Hot'), (1, 'New'), (2, 'Popular')])

    @api.one
    @api.depends("place_ids", "service_ids")
    def compute_total_price(self):
        self.total_price = 0
        for model in self.place_ids:
            self.total_price += model.price

        for model in self.service_ids:
            self.total_price += model.price

    total_price = fields.Integer(default=0, string='price', compute="compute_total_price")