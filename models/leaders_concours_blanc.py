# -*- coding: utf-8 -*-

import time
from datetime import datetime
from odoo import models, fields, api, SUPERUSER_ID, _
from odoo.exceptions import UserError, Warning, ValidationError


class leaders_concours_blanc(models.Model):
    _name = 'leaders.concour.blanc'
    _description = 'Concours Blanc'
    _order = 'id DESC'

    @api.model
    def _get_default_academic_year(self):
        academic_year_obj = self.env['leaders.year']
        academic_year_id = academic_year_obj.search([('actived', '=', True)], limit=1)
        return academic_year_id and academic_year_id.id or False

    name = fields.Char("Nom")
    date_concours = fields.Date("Date du concours", require=True)
    concour_id = fields.Many2one("leaders.concour.config", string="Concours", required=True)
    matiere_ids = fields.Many2many("leaders.matier", string="Matières")
    number = fields.Selection([('1', '1'),
                               ('2', '2'),
                               ('3', '3'),
                               ('4', '4'),
                               ('5', '5'),
                               ('6', '6'),
                               ], string="Numero", required=True)

    state = fields.Selection([('draft', 'Brouillon'),
                               ('valited', 'Valider'),
                               ('delete', 'Annuler')
                               ], string="Etat")

    year_id = fields.Many2one("leaders.year", string="Année en cours", required=True,
                              default=lambda self: self._get_default_academic_year())
    center_id = fields.Many2one("leaders.center", string="Centre de preparation", require=True)

    # lignes_ids = fields.On2many( )

    lignes_ids = fields.One2many('leaders.concour.blanc.line', 'concours_id', copy=True, string="Les Apprenants")

    @api.model
    def create(self, vals):
        # vals['ane_academique_id'] = "Your Value"

        vals.update({
            'name':  'Concours Blanc No' + str(self.number) + 'de' + str(self.concour_id.name) +'du'+ str(self.date_concours)
        })
        res = super(leaders_concours_blanc, self).create(vals)

        return res

    def set_to_validated(self):
        # for record in self:
        #     if record.annuel_average > record.classe_id.min_average:
        #         raise UserError(_("Alerte! la moyenne de cet élève est "
        #                           "superieure a la note minimale requise  pour l'admision en classe superieure"))
        return self.write({"state": 'valited'})

    def set_to_draft(self):
        # for record in self:
        #     if record.annuel_average > record.classe_id.min_average:
        #         raise UserError(_("Alerte! la moyenne de cet élève est "
        #                           "superieure a la note minimale requise  pour l'admision en classe superieure"))
        return self.write({"state": 'draft'})

    def set_to_delete(self):
        # for record in self:
        #     if record.annuel_average > record.classe_id.min_average:
        #         raise UserError(_("Alerte! la moyenne de cet élève est "
        #                           "superieure a la note minimale requise  pour l'admision en classe superieure"))
        return self.write({"state": 'delete'})


    def name_get(self):
        '''Method to display name and code'''
        return [(rec.id, 'Concours Blanc No' + str(rec.number) + '-' + str(rec.concour_id.name)) for rec in self]

    # @api.onchange('concour_id', 'year_id')
    def load_contours_trainer(self):
        concours_ids= self.env['leaders.concour.config'].search([ ])

        lignes_ids = self.env['leaders.apprenant'].search([('center_id', '=', self.center_id.id),
                                                           ('year_id', '=', self.year_id.id)
                                                           ])
        #('center_id', '=', self.center_id)
        # if len(lignes_ids) == 0:
        #     raise UserError(_("'Alert !!! Il n'ya pas d'apprenant remplissant  les criteres insérés '"))
        if not self.concour_id or not self.center_id:
            raise UserError(_("'Alert !!! veillez remplir tous les champs obligatoires '"))

        for rec in self:

            if rec.concour_id:
                lines = [(5, 0, 0)]
                for line in lignes_ids:
                    vals = {
                        'apprenant_id': line.id,
                        'etablissment_id': line.etablissment_id.id,
                        'center_id': line.center_id.id
                    }
                    lines.append((0, 0, vals))
                rec.lignes_ids = lines



class leaders_concours_blanc_line(models.Model):
    _name = 'leaders.concour.blanc.line'
    _description = ' Ligne de Concours Blanc'
    _order = 'id DESC'

    @api.model
    def _get_default_academic_year(self):
        academic_year_obj = self.env['leaders.year']
        academic_year_id = academic_year_obj.search([('actived', '=', True)], limit=1)
        return academic_year_id and academic_year_id.id or False

    apprenant_id = fields.Many2one("leaders.apprenant", string="Apprenants")
    note_mat1 = fields.Float("Matiere 1 ")
    note_mat2 = fields.Float("Matiere 2 ")
    note_mat3 = fields.Float("Matiere 3 ")
    note_mat4 = fields.Float("Matiere 4 ")
    average = fields.Float("Moyene")
    concours_id = fields.Many2one("leaders.concour.blanc", string="Concours")
    center_id = fields.Many2one("leaders.center", string="Centre de preparation")
    etablissment_id = fields.Many2one("leaders.school", string="Etablissement Frequenté")
    number = fields.Selection([('1', '1'),
                               ('2', '2'),
                               ('3', '3'),
                               ('4', '4'),
                               ('5', '5'),
                               ('6', '6'),
                               ], string="Numero")
    year_id = fields.Many2one("leaders.year", string="Année en cours",
                              default=lambda self: self._get_default_academic_year())




    # rang = fields.Float("Rang")

