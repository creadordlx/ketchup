from odoo import fields, models


class KetchupBlog(models.Model):
    _inherit = "ir.attachment"

    place_id = fields.Many2one("ketchup.places")
    blog_id = fields.Many2one("ketchup.blog")
    service_id = fields.Many2one("ketchup.services")
    tour_id = fields.Many2one("ketchup.tours")
