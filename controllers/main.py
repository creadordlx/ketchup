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
            print(len(s.photo_ids))
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

    @http.route('/tour/<int:id>', auth='public')
    def tour(self, id, **kw):
        tour = request.env["ketchup.tours"].search([("id", "=", id)])
        services = request.env["ketchup.services"].search([("id", "in", list(map(lambda x: x.id, tour.service_ids)))])
        places = request.env["ketchup.places"].search([("id", "in", list(map(lambda x: x.id, tour.place_ids)))])
        print(services)
        return request.render("ketchup.tour_single", {
            "title": "Tour",
            "tour": tour,
            "services": services,
            "places": places
        })

    @http.route('/js_mod', auth='public')
    def js_mod(self, **kw):
        return request.render("ketchup.js_mod", {})

    @http.route('/tours/create', auth='public')
    def tours_create(self, **kw):
        return request.render('ketchup.create_tour', {
            "title": 'Создание Тура'
        })
