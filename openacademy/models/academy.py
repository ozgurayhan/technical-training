from odoo import api, fields, models



class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Course Session'
    _rec_name = 'title'
    
    title = fields.Char(string='Title')
    course_id = fields.Many2one('openacademy.course', string='Course', ondelete='cascade', required=True)
    attendee_ids = fields.Many2many('openacademy.partner', relation='openacademy_session_attendee_rel', string='Attendees')
    professors_ids = fields.Many2many('openacademy.partner', relation='openacademy_session_professor_rel', string='professors')
    
    
class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Course'
    _rec_name = 'title'
    
    title = fields.Char(string='Title')
    responsible_id = fields.Many2one('res.users', string='Responsible')
    session_ids = fields.One2many('openacademy.session', 'course_id', string='sessions')
    
    
    
class Partner(models.Model):
    _name = 'openacademy.partner'
    _description = 'Course Partner'
    
    name = fields.Char(string='Name')
    session_ids = fields.Many2many('openacademy.session', relation='openacademy_session_attendee_rel', string='Sessions')
    
    
    
    