# -*- coding: utf-8 -*-
from odoo import http

# class ShowDoubleCurrency(http.Controller):
#     @http.route('/show_double_currency/show_double_currency/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/show_double_currency/show_double_currency/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('show_double_currency.listing', {
#             'root': '/show_double_currency/show_double_currency',
#             'objects': http.request.env['show_double_currency.show_double_currency'].search([]),
#         })

#     @http.route('/show_double_currency/show_double_currency/objects/<model("show_double_currency.show_double_currency"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('show_double_currency.object', {
#             'object': obj
#         })