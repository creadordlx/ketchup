# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/about', auth='public')
    def about(self, **kw):
        return request.render("ketchup.about", {
            "title": "О компании"
        })

    @http.route('/main', auth='public')
    def main(self, **kw):
        return request.render("ketchup.main", {
            "title": "Главная"
        })

    @http.route('/products', auth='public')
    def products(self, **kw):
        return request.render("ketchup.products", {
            "title": "Места"
        })

    @http.route('/store', auth='public')
    def store(self, **kw):
        return request.render("ketchup.store", {
            "title": "Корзина"
        })