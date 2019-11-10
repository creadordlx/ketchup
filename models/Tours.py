from odoo import api, fields, models


class KetchupTours(models.Model):
    _name = "ketchup.tours"
    _description = "List of Tours"

    name = fields.Char('Название', size=128)
    description = fields.Text('Описание')
    rating = fields.Float('Рейтинг', default=0.0)

    place_ids = fields.Many2many('ketchup.places', string='Места')
    blog_ids = fields.One2many('ketchup.blog', 'tour_id', string='Рецензии')
    service_ids = fields.Many2many('ketchup.services', string='Услуги')
    photo_ids = fields.One2many('ir.attachment', 'tour_id', string='Фотографии')
    type = fields.Selection(string='type', selection=[(0, 'Горячее'), (1, 'Новое'), (2, 'Популярное')])

    @api.one
    @api.depends("place_ids", "service_ids")
    def compute_total_price(self):
        self.total_price = 0
        for model in self.place_ids:
            self.total_price += model.price

        for model in self.service_ids:
            self.total_price += model.price

    total_price = fields.Integer(default=0, string='Общая цена', compute="compute_total_price")