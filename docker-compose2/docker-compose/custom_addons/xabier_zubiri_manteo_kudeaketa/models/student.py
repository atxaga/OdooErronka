from odoo import models, fields

class Student(models.Model):
    _name = 'xz.student'
    _description = 'Student'

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    classroom_id = fields.Many2one('xz.classroom', string="Classroom")