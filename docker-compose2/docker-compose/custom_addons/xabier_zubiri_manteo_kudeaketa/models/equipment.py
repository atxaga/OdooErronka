from odoo import models, fields

class Equipment(models.Model):
    _name = 'xz.equipment'
    _description = 'Ekipamendua'

    name = fields.Char(string="Izena", required=True)
    serial_number = fields.Char(string="Serie Zenbakia")
    
    type = fields.Selection([
        ('computer', 'Ordenagailua'),
        ('screen', 'Pantaila')
    ], string="Mota", required=True)

    purchase_date = fields.Date(string="Erosketa Data")
    cost = fields.Float(string="Kostua")

    classroom_id = fields.Many2one('xz.classroom', string="Gela")
    student_id = fields.Many2one('xz.student', string="Esleitutako Ikaslea")

    state = fields.Selection([
        ('available', 'Libre'),
        ('assigned', 'Esleituta'),
        ('repair', 'Konponketan')
    ], default='available', string="Egoera")
