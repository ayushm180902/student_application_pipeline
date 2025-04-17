from odoo import models, fields, api


class ProcessPipeline(models.Model):
    _name = 'student.pipeline.process'
    _description = 'Student Application Process'
    _rec_name = 'name'
    _order = 'id desc'

    def _get_default_stage_id(self):
        stage = self.env['student.pipeline.stage'].search([('sequence', '=', 1)], limit=1)
        return stage.id if stage else False

    name = fields.Char('Application Reference', compute='_compute_name', store=True)
    student_id = fields.Many2one('student.pipeline.student', string='Student', required=True)
    university_id = fields.Many2one('student.pipeline.university', string='University', required=True)
    stage_id = fields.Many2one('student.pipeline.stage', string='Stage',
                               default=_get_default_stage_id, group_expand='_read_group_stage_ids')
    is_won = fields.Boolean('Is Won', related='stage_id.is_won', store=True)

    # Application details
    application_date = fields.Date('Application Date', default=fields.Date.today)
    program_applied = fields.Char('Program Applied For')
    expected_start_date = fields.Date('Expected Start Date')

    # Documents status
    documents_submitted = fields.Boolean('Documents Submitted')
    documents_notes = fields.Text('Document Notes')

    # Additional Information
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
    ], string='Priority', default='1')

    notes = fields.Text('Notes')
    color = fields.Integer('Color')

    @api.depends('student_id', 'university_id')
    def _compute_name(self):
        for record in self:
            if record.student_id and record.university_id:
                record.name = f"{record.student_id.name} - {record.university_id.name}"
            else:
                record.name = "New Application"

    @api.model
    def _read_group_stage_ids(self, domain, order):
        """Group expand method to show all stages in Kanban view."""
        if not isinstance(order, str) or not order.strip():
            order = 'sequence'
        stages = self.env['student.pipeline.stage'].search([], order=order)
        return stages

    def action_view_student(self):
        """Return an action to open the related student's form view."""
        self.ensure_one()
        if not self.student_id:
            raise ValueError("No student associated with this process.")
        return {
            'type': 'ir.actions.act_window',
            'name': 'Student',
            'res_model': 'student.pipeline.student',
            'view_mode': 'form',
            'res_id': self.student_id.id,
        }

    def action_view_university(self):
        """Return an action to open the related university's form view."""
        self.ensure_one()
        if not self.university_id:
            raise ValueError("No university associated with this process.")
        return {
            'type': 'ir.actions.act_window',
            'name': 'University',
            'res_model': 'student.pipeline.university',
            'view_mode': 'form',
            'res_id': self.university_id.id,
        }
