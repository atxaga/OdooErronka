from odoo import models, fields

class Classroom(models.Model):
    _name = 'xz.classroom'
    _description = 'Ikasgela'

    name = fields.Char(string="Gela", required=True)
    location = fields.Char(string="Kokapena")
    equipment_ids = fields.One2many('xz.equipment', 'classroom_id', string="Ekipamendua")