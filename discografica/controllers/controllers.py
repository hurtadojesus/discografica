# -*- coding: utf-8 -*-
# from odoo import http


# class Ut5Discografica(http.Controller):
#     @http.route('/ut5_discografica/ut5_discografica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ut5_discografica/ut5_discografica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ut5_discografica.listing', {
#             'root': '/ut5_discografica/ut5_discografica',
#             'objects': http.request.env['ut5_discografica.ut5_discografica'].search([]),
#         })

#     @http.route('/ut5_discografica/ut5_discografica/objects/<model("ut5_discografica.ut5_discografica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ut5_discografica.object', {
#             'object': obj
#         })
