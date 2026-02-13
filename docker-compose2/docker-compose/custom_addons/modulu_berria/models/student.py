from odoo import models, fields

class EskolaStudent(models.Model):
    _name = 'eskola.student'
    _description = 'Eskolako Ikaslea'

    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname')
    image = fields.Binary(
        string='Image',
    )
    student_age = fields.Integer(string='Age')
    student_day_of_birth = fields.Date(string='Date of Birth')

    student_gender = fields.Selection(
        [('m', 'Male'), ('f', 'Female'), ('o', 'Other')],
        string='Gender'
    )

    student_blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        string='Blood Group'
    )

    def _default_image(self):
        return self.env['ir.binary'].sudo()._get_default_image()