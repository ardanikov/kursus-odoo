from odoo import models, fields, api

class KursusWizard(models.TransientModel):
    _name = 'cdn.kursus.wizard'
    _description = 'Kursus Wizard'

    def _default_session(self):
        return self.env['cdn.kursus.session'].browse(self._context.get('active_ids'))

    session_id = fields.Many2one('cdn.kursus.session', string='Session', default=_default_session)
    session_ids = fields.Many2many('cdn.kursus.session', string='Multi Kursus Session', default=_default_session)
    peserta_ids = fields.Many2many('cdn.peserta', string='Peserta')

    def action_add_peserta(self):
        self.session_id.peserta_ids |= self.peserta_ids

    def action_add_many_peserta(self):
        for session in self.session_ids:
            session.peserta_ids |= self.peserta_ids