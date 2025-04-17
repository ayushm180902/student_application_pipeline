from odoo import models, fields, api


class University(models.Model):
    _name = 'student.pipeline.university'
    _description = 'University'

    name = fields.Char('University Name', required=True)
    code = fields.Char('University Code')
    country_id = fields.Many2one('res.country', string='Country')
    city = fields.Char('City')
    address = fields.Text('Address')
    website = fields.Char('Website')

    # Academic Information
    ranking = fields.Integer('Ranking')
    accreditation = fields.Char('Accreditation')

    # Available Programs
    programs = fields.Text('Available Programs')

    # Relationships
    student_ids = fields.Many2many('student.pipeline.student', string='Applicants')

    # Application Processes
    application_ids = fields.One2many('student.pipeline.process', 'university_id', string='Applications')

    active = fields.Boolean(default=True)