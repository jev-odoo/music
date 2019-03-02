from odoo import api, fields, models

NOTES = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G')]
MODIFIERS = [('flat', 'b'), ('natural', 'Natural'), ('sharp', "#")]


class key(models.Model):
    _name = 'music.key'
    _description = 'Key of the instrument'
 
    name = field_name = fields.Char(
        compute='_compute_name'
    )

    
    short_name = fields.Char(
        compute='_compute_short_name'
    )
    

    note = fields.Selection(
        string=u'name',
        selection=(NOTES),
        default='A',
        required=True
    )

    modifier = fields.Selection(
        string=u'modifier',
        selection=(MODIFIERS),
        default='natural',
        required=True
        
    )
        
    @api.multi
    def getFullKey(self):
        return self.name + self.modifier

    @api.depends('note', 'modifier')
    def _compute_name(self):
        for record in self:
            record.name = record.note + ' ' + record.modifier
            record.short_name = record.note + ('' if dict(MODIFIERS)[record.modifier] == 'Natural' else dict(MODIFIERS)[record.modifier])
