# -*- coding: utf-8 -*-
from odoo import http

# class AutoProduct(http.Controller):
#     @http.route('/auto_product/auto_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/auto_product/auto_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('auto_product.listing', {
#             'root': '/auto_product/auto_product',
#             'objects': http.request.env['auto_product.auto_product'].search([]),
#         })

#     @http.route('/auto_product/auto_product/objects/<model("auto_product.auto_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('auto_product.object', {
#             'object': obj
#         })