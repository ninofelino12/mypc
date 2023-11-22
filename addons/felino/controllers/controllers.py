# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request



class Felino(http.Controller):
     @http.route('/felino/felino', auth='public')
     def index(self, **kw):
         return """
        <a href="/felino/iot">IOT</a>
        """
     
     @http.route('/felino/iot', auth='public')
     def iotidx(self, **kw):
         #my_data = {'name': 'John Doe', 'age': 30}
         #template = "my_module.my_template"
         return http.request.render('fwindow',{})
            

     @http.route('/felino/felino/objects', auth='public')
     def list(self, **kw):
         return http.request.render('felino.listing', {
             'root': '/felino/list',
             'objects': http.request.env['felino.felino'].search([]),
         })

     @http.route('/felino/felino/objects/<model("felino.felino"):obj>', auth='public')
     def object(self, obj, **kw):
         return http.request.render('felino.object', {
             'object': obj
         })
