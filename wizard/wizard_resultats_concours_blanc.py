#See LICENSE file for full copyright and licensing details.


from odoo import fields, models, api,_
from odoo.exceptions import UserError
from datetime import datetime
import csv, codecs
from io import BytesIO
import base64
from dateutil.relativedelta import relativedelta
import xlwt
from odoo import fields, models,api ,SUPERUSER_ID, _

class ConcoursBalancWizard(models.TransientModel):
    _name = "concour.blanc.wizard"
    #_rec_name = "date_start"
    _description = " Resultats du concours Blanc"


    @api.model
    def _get_default_academic_year(self):
        academic_year_obj = self.env['leaders.year']
        academic_year_id = academic_year_obj.search([('actived', '=', True)], limit=1)
        return academic_year_id and academic_year_id.id or False

    #name = fields.Char("Noms")
    concour_id = fields.Many2one("leaders.concour.config", string="Concours", required=True)
    #matiere_ids = fields.Many2many("leaders.matier", string="Matières")
    number = fields.Selection([('1', '1'),
                               ('2', '2'),
                               ('3', '3'),
                               ('4', '4'),
                               ('5', '5'),
                               ('6', '6'),
                               ('6', '6'),
                               ('7', 'Or'),
                               ], string="Numéro du Concours Blanc", required=True)

    year_id = fields.Many2one("leaders.year", string="Année en cours", required=True,
                              default=lambda self: self._get_default_academic_year())
    center_ids = fields.Many2many("leaders.center", string="Centre de preparation")
    file_name = fields.Char('Nom du fichier', size=255, readonly=True)
    file_data = fields.Binary('File', readonly=True)
    bool = fields.Boolean('Exporté', readonly=True)


    def print_report(self):
        for record in self:
            data = self._get_data()
            #raise UserError(_(data))
            #print()
            buf = BytesIO()
            buffer_xls = BytesIO()
            wb = xlwt.Workbook(encoding='cp1251')
            ws = wb.add_sheet(u'RESULTATS CONCOURS BLANCS')
            style_number = xlwt.easyxf('font: name Times New Roman', num_format_str='#,##0')
            # ------------------- Corps du fichier --------------------#

            for i in range(len(data)):
                for j in range(len(data[i])):
                    if j < len(data[i]):
                        ws.write(i, j, data[i][j], style_number)

            wb.save(buffer_xls)
            file = base64.encodestring(buffer_xls.getvalue())
            buffer_xls.close()
            buf.close()
            fname = u'RESULTATS_CONCOURS_BLANCS.xls'
            self.write({'file_data': file, 'file_name': fname, 'bool': True})
            return {
                'name': 'Exportation des fichiers',
                'type': 'ir.actions.act_window',
                'res_model': 'concour.blanc.wizard',
                'view_mode': 'form',
                'view_type': 'form',
                'res_id': record.id,
                'views': [(False, 'form')],
                'target': 'new',
            }

    def _get_data(self):

        # livraisions_obj = self.env.get('stock.picking')

        # domain = [('number','=',self.number),
        #           ('year_id','=',self.year_id),
        #           ('concour_id','=',self.concour_id)]

        domain =[]

        # if self.concour_ids:
        #     domain.append(('concour_id', 'in', self.concour_ids.ids))

        data = [
            [' ',
             u' RESULTATS CONCOURS BLANCS  ' + str(self.number) + ' DE ' + str(self.concour_id.name)],
            [' '],
            [u'RANG',u'CENTRE', u'NOMS ET PRENOMS DE L''ELEVE ', u'DERNIER ETABLISSAMENT FREQUENTE', u'MATIERE 1', u'MATIERE 2', u'MATIERE 3',  u'MATIERE 4',
             u'MOYENNE']
        ]
        # stagiaire_ids = stagiaire_obj.search([('date_register', '>=', date_start),('date_register', '<=', date_end)])

        # livraison_ids = self.env['stock.picking'].search(domain, order="company_id desc")
        # len_total = len(stagiaire_ids)
        ligne_concours_ids = self.env['leaders.concour.blanc.line'].search(domain, order="average asc")

        # company_ids = self.env['res.company'].browse(data.get('company_ids'))
        # souscript_ids = self.env['res.partner.title'].browse(data.get('souscript_ids'))

        # data.update({'company_ids': ",".join([company.name for company in company_ids])})

        # article_ids = list(set(docs.mapped("move_ids_without_package.name")))
        # livraison.partner_id.cnp,
        # livraison.partner_id.id_nr,
        indis = 1
        for ligne in ligne_concours_ids:
            data.append([indis,
                         ligne.apprenant_id.center_id.name,
                         ligne.apprenant_id.etablissment_id.name,
                         ligne.note_mat1,
                         ligne.note_mat2,
                         ligne.note_mat3,
                         ligne.note_mat4,
                         ligne.average,
                         ])
            indis = indis + 1
        return data


class ConcoursBalancReportWizard(models.TransientModel):
        _name = "concour.blanc.report.wizard"
        _description = " Resultats du  Blanc"

        #name = fields.Char("Noms")
        #concour_id = fields.Many2one("leaders.concour.config", string="Concours")






# class TestModelWizard(models.TransientModel):
#     _name =  'test.model.wizard'
#     _description = 'Test Model Wizard'
#
#     test_field = fields.Char(string = 'Test Field')
#
#     def create_wizard(self):
#         wizard = self.env['test.model.wizard'].create({'test_field': self.name })
#         return { 'name': _('Test Wizard'),
#                  'type': 'ir.actions.act_window',
#                  'res_model': 'test.model.wizard',
#                  'view_mode': 'form',
#                  'res_id': wizard.id,
#                  'target': 'new'
#                  }