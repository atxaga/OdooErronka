from odoo import models, fields

class ZubiriStudent(models.Model):
    _name = 'xz.student' 
    _description = 'Ikasleen kudeaketa'

    name = fields.Char(string='Izena', required=True)
    apellido = fields.Char(string='Abizena')
    email = fields.Char(string='Email Korporatiboa')
    zikloa = fields.Selection([
        ('ms', 'MS'), 
        ('ssa', 'SSA'), 
        ('wg', 'WG'), 
        ('paag', 'PAAG')
    ], string='Zikloa')
    
    equipment_id = fields.Many2one('xz.equipment', string='PC Esleitua')