# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/index', auth='public')
    def index(self, **kw):
        return request.render("ketchup.index", {
            "title": "Главная"
        })

    @http.route('/services', auth='public')
    def services(self, **kw):
        return request.render("ketchup.services", {
            "title": "Сервисы"
        })

    @http.route('/about', auth='public')
    def about(self, **kw):
        return request.render("ketchup.about", {
            "title": "О компании"
        })

    @http.route('/blog', auth='public')
    def blog(self, **kw):
        return request.render("ketchup.blog", {
            "title": "Блог"
        })

    @http.route('/blog_single', auth='public')
    def blog_single(self, **kw):
        return request.render("ketchup.blog_single", {
            "title": "Блог"
        })

    @http.route('/contact', auth='public')
    def contact(self, **kw):
        return request.render("ketchup.contact", {
            "title": "Связаться"
        })

    @http.route('/hotels', auth='public')
    def hotels(self, **kw):
        return request.render("ketchup.hotels", {
            "title": "Отели"
        })

    @http.route('/tours', auth='public')
    def tours(self, **kw):
        return request.render("ketchup.tours", {
            "title": "Туры"
        })
