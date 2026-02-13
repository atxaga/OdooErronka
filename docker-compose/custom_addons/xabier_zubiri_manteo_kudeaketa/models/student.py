from odoo import models, fields, api

class Student(models.Model):
    _name = 'my_student.student'
    _description = 'Ikasleak'
    
    name = fields.Char(string='Izena', required=True)
    user_id = fields.Many2one('res.users', string='Erabiltzailea', required=True)
    notes = fields.Text(string='Oharrak')

class StudentEvent(models.Model):
    _name = 'my_student.event'
    _inherit = 'calendar.event'  # Calendar module-arekin integratuta

    student_id = fields.Many2one('my_student.student', string='Ikaslea')

    @api.model
    def create(self, vals):
        # Ziurtatu ikasle bakoitzak bere ekintzak bakarrik sortzen ditu
        if 'student_id' in vals and vals['student_id']:
            student = self.env['my_student.student'].browse(vals['student_id'])
            if student.user_id != self.env.user:
                raise ValueError("Ez duzu ekintza hau sortzeko baimenik")
        return super(StudentEvent, self).create(vals)
