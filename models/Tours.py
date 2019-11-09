from odoo import api, fields, models


class KetchupTours(models.Model):
    _name = "ketchup.tours"
    _description = "List of Tours"

    name = fields.Char('name', size=128)
    place_ids = fields.Many2many('ketchup.places', string='place_ids')
    service_ids = fields.Many2many('ketchup.services', string='service_ids')

    @api.one
    @api.depends("place_ids", "service_ids")
    def compute_total_price(self):
        # places = self.env["ketchup.places"].search([('id', 'in', self.place_ids)])
        # services = self.env['ketchup.services'].search([('id', 'in', self.service_ids)])
        self.total_price = 0
        for model in self.place_ids:
            self.total_price += model.price

        for model in self.service_ids:
            self.total_price += model.price

    total_price = fields.Float(default=0, string='price', compute="compute_total_price")