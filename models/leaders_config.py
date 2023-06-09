# -*- coding: utf-8 -*-

import time
from datetime import datetime
from odoo import models, fields, api


class leaders_concours(models.Model):
    _name = 'leaders.concour.config'
    _description = ' Les Configuration de Concours'
    _order = 'id DESC'

    name = fields.Char(string="Nom")
    nb_matier = fields.Char(string="Nombre de Matières")
    matiere_ids = fields.Many2many("leaders.matier", string="Matières presente du concours")


class leaders_center(models.Model):
    _name = 'leaders.center'
    _inherit = 'hr.department'
    _description = ' Les  centres de preparations'
    #_order = 'id DESC'

    #name = fields.Char(string="Nom")

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

    #region_id = fields.Many2one("leaders.region", string="Region")

    # def name_get(self):
    #     '''Method to display name and code'''
    #     return [(rec.id, ' (' + str(rec.region_id.name) + ')' + str(rec.name)) for rec in self]


# class leaders_region(models.Model):
#     _name = 'leaders.region'
#     _inherit = 'hr.department'
#     _description = ' Les  regions'
#     #_order = 'id DESC'
#
#     name = fields.Char(string="Nom")

    #region_id = fields.Many2one("leaders.center", string="Region")


class leaders_year(models.Model):
    _name = 'leaders.year'
    _description = ' Les  années scolaires'
    _order = 'id DESC'

    name = fields.Char("Nom", default=' ')
    date_start = fields.Date('Date de debut', required=True)
    date_end = fields.Date('Date de fin' , required=True)
    actived = fields.Boolean('Active ?')
    #description = fields.Char("Description")


    def name_get(self):
        '''Method to display name and code'''
        return [(rec.id, ' ' + str(rec.date_start.year) + '/' + str(rec.date_end.year)) for rec in self]






class leaders_school(models.Model):
        _name = 'leaders.school'
        _description = ' Les etablissements Scolaire'
        #_order = 'id DESC'

        name = fields.Char(string="Noms")



class leaders_filiere(models.Model):
        _name = 'leaders.filiere'
        _description = ' Les Fileres des apprenants'
        #_order = 'id DESC'

        name = fields.Char(string="Nom")

class leaders_work(models.Model):
        _name = 'leaders.work'
        _description = ' Les professions des parents'
        #_order = 'id DESC'

        name = fields.Char(string="Nom")

class leaders_town(models.Model):
        _name = 'leaders.town'
        _description = ' Les villes des parents'
        #_order = 'id DESC'
        name = fields.Char(string="Noms")


class leaders_speciality(models.Model):
    _name = 'leaders.speciality'
    _description = ' Les Specialite des parents'
    # _order = 'id DESC'
    name = fields.Char(string="Noms")
