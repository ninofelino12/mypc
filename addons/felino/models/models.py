from odoo import models, fields, api


class felino(models.Model):
     _name = 'felino.felino'
     _description = 'felino.felino'

     name = fields.Char()
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()

     @api.depends('value')
     def _value_pc(self):
         for record in self:
             record.value2 = float(record.value) / 100
