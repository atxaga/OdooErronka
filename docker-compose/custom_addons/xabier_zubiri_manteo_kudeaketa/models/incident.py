from odoo import models, fields, api  # api gehitu behar da

class Incident(models.Model):
    _name = 'xz.incident'
    _description = 'Inzidentzia'

    name = fields.Char(string="Deskribapena", required=True)
    equipment_id = fields.Many2one('xz.equipment', string="Ekipamendua", required=True)
    reported_by = fields.Many2one('res.users', string="Jakinarazi duena", default=lambda self: self.env.user)
    date = fields.Date(string="Data", default=fields.Date.today)
    priority = fields.Selection([
        ('low', 'Baxua'),
        ('medium', 'Ertaina'),
        ('high', 'Altua')
    ], string="Lehentasuna")
    state = fields.Selection([
        ('open', 'Irekita'),
        ('in_progress', 'Prozesuan'),
        ('closed', 'Itxita')
    ], default='open', string="Egoera")

    @api.model
    def create(self, vals):
        record = super(Incident, self).create(vals)
        if record.equipment_id:
            record.equipment_id.state = 'repair'
        return record
