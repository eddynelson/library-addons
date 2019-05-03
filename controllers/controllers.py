# -*- coding: utf-8 -*-
from odoo import http

# class /odoo/custom/addons/library(http.Controller):
#     @http.route('//odoo/custom/addons/library//odoo/custom/addons/library/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//odoo/custom/addons/library//odoo/custom/addons/library/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/odoo/custom/addons/library.listing', {
#             'root': '//odoo/custom/addons/library//odoo/custom/addons/library',
#             'objects': http.request.env['/odoo/custom/addons/library./odoo/custom/addons/library'].search([]),
#         })

#     @http.route('//odoo/custom/addons/library//odoo/custom/addons/library/objects/<model("/odoo/custom/addons/library./odoo/custom/addons/library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/odoo/custom/addons/library.object', {
#             'object': obj
#         })