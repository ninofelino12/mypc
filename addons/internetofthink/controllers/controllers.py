# -*- coding: utf-8 -*-
# from odoo import http


# class Internetofthink(http.Controller):
#     @http.route('/internetofthink/internetofthink', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/internetofthink/internetofthink/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('internetofthink.listing', {
#             'root': '/internetofthink/internetofthink',
#             'objects': http.request.env['internetofthink.internetofthink'].search([]),
#         })

#     @http.route('/internetofthink/internetofthink/objects/<model("internetofthink.internetofthink"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('internetofthink.object', {
#             'object': obj
#         })
