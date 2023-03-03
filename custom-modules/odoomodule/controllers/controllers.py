# -*- coding: utf-8 -*-
# from odoo import http


# class Odoomodule(http.Controller):
#     @http.route('/odoomodule/odoomodule', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoomodule/odoomodule/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoomodule.listing', {
#             'root': '/odoomodule/odoomodule',
#             'objects': http.request.env['odoomodule.odoomodule'].search([]),
#         })

#     @http.route('/odoomodule/odoomodule/objects/<model("odoomodule.odoomodule"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoomodule.object', {
#             'object': obj
#         })
