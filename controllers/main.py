# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/index', auth='public')
    def index(self, **kw):
        tours = request.env["ketchup.tours"].search([], limit=4)
        services = request.env["ketchup.services"].search([], limit=4)
        for s in tours:
            print(s.name)
            print(s.photo_ids[0].id)
        return request.render("ketchup.index", {
            "title": "Home",
            "tours": tours,
            "services": services
        })

    @http.route('/services', auth='public')
    def services(self, **kw):
        services = request.env["ketchup.services"].search([])
        return request.render("ketchup.services", {
            "title": "Services",
            "services": services
        })

    @http.route('/about', auth='public')
    def about(self, **kw):
        return request.render("ketchup.about", {
            "title": "About"
        })

    @http.route('/blog', auth='public')
    def blog(self, **kw):
        blogs = request.env["ketchup.blog"].search([])
        return request.render("ketchup.blog", {
            "title": "Review",
            "blogs": blogs
        })

    @http.route('/blog_single', auth='public')
    def blog_single(self, **kw):
        return request.render("ketchup.blog_single", {
            "title": "Review"
        })

    @http.route('/contact', auth='public')
    def contact(self, **kw):
        return request.render("ketchup.contact", {
            "title": "Contact"
        })

    @http.route('/places', auth='public')
    def hotels(self, **kw):
        places = request.env["ketchup.places"].search([])
        return request.render("ketchup.hotels", {
            "title": "Places",
            "places": places
        })

    @http.route('/tours', auth='public')
    def tours(self, **kw):
        tours = request.env["ketchup.tours"].search([])
        return request.render("ketchup.tours", {
            "title": "Tours",
            "tours": tours
        })
