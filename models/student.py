from odoo import models, fields, api


class Student(models.Model):
    _name = 'student.pipeline.student'
    _description = 'Student'

    name = fields.Char('Name', required=True)
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    date_of_birth = fields.Date('Date of Birth')
    address = fields.Text('Address')

    # Academic Information
    education_level = fields.Selection([
        ('high_school', 'High School'),
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('phd', 'PhD')
    ], string='Current Education Level')
    gpa = fields.Float('GPA')

    # Documents
    resume = fields.Binary('Resume')
    resume_filename = fields.Char('Resume Filename')

    # Relationships
    university_ids = fields.Many2many('student.pipeline.university', string='Applied Universities')

    # Application Processes
    application_ids = fields.One2many('student.pipeline.process', 'student_id', string='Applications')

    active = fields.Boolean(default=True)