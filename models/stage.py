from odoo import models, fields, api


class Stage(models.Model):
    _name = 'student.pipeline.stage'
    _description = 'Application Stage'
    _order = 'sequence'

    name = fields.Char('Stage Name', required=True)
    sequence = fields.Integer('Sequence', default=1)
    fold = fields.Boolean('Folded in Pipeline')
    is_won = fields.Boolean('Is Won Stage')

    # These are the default stages
    @api.model
    def _get_default_stages(self):
        return [
            (0, 0, {'name': 'New', 'sequence': 1}),
            (0, 0, {'name': 'Applied', 'sequence': 2}),
            (0, 0, {'name': 'Under Review', 'sequence': 3}),
            (0, 0, {'name': 'Interview', 'sequence': 4}),
            (0, 0, {'name': 'Accepted', 'sequence': 5, 'is_won': True}),
            (0, 0, {'name': 'Rejected', 'sequence': 6, 'fold': True})
        ]