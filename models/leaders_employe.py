# -*- coding: utf-8 -*-

import time
from datetime import datetime
from odoo import models, fields, api

class leaders_employee(models.Model):
    _name = 'leaders.employee'
    _inherit = ['hr.employee']
    _description = ' Les  Employés de Leaders'
    #_order = 'id DESC'

    #name = fields.Char(string="Nom")
    #is_teacher = fields.Boolean("Est'il un enseignant ?")

    type = fields.Selection([('teacher', 'Enseignant'),('perma', 'Employé permanant'),
                             ('temp', 'Employé Temporaire'),
                             ], string="Type d'employé", required=True)

    matiere_ids = fields.Many2many("leaders.matier", string="Matières Enseignées")
    univ_id = fields.Many2one("leaders.school", string="Université")
    center_id = fields.Many2one("leaders.center", string="Centre de preparation")
    region = fields.Selection([('ad', 'ADAMAOUA'),
                               ('ce', 'CENTRE'),
                               ('en', 'EXTREME-NORD'),
                               ('es', 'EST'),
                               ('lt', 'LITTORAL'),
                               ('no', 'NORD'),
                               ('nd', 'NORD-OUEST'),
                               ('ou', 'OUEST'),
                               ('su', 'SUD'),
                               ('sd', 'SUD-OUEST'),
                               ],
                              string='REGION',
                              help="La region ou se situe le centre de prepaartion")
    category_ids = fields.Many2many(
        'hr.employee.category', 'student_category_rel',
        'student_id', 'category_id',
        string='Tags')




class leaders_matier(models.Model):
    _name = 'leaders.matier'
    _description = ' Les Matières enseignées'
    #_order = 'id DESC'

    name = fields.Char(string="Nom",required=True)


