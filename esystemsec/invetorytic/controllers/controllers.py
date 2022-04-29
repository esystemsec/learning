# -*- coding: utf-8 -*-
# from odoo import http


# class Invetorytic(http.Controller):
#     @http.route('/invetorytic/invetorytic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invetorytic/invetorytic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('invetorytic.listing', {
#             'root': '/invetorytic/invetorytic',
#             'objects': http.request.env['invetorytic.invetorytic'].search([]),
#         })

#     @http.route('/invetorytic/invetorytic/objects/<model("invetorytic.invetorytic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invetorytic.object', {
#             'object': obj
#         })
