# from odoo import models, fields, api


# class xabier-zubiri__manteo_kudeaketa(models.Model):
#     _name = 'xabier-zubiri__manteo_kudeaketa.xabier-zubiri__manteo_kudeaketa'
#     _description = 'xabier-zubiri__manteo_kudeaketa.xabier-zubiri__manteo_kudeaketa'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

