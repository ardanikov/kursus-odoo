from odoo import models, fields, api

class Kursus(models.Model):
    _name = 'cdn.kursus'
    _description = 'Tabel Kursus'

    name = fields.Char(string='Nama Kursus', required=True)
    description = fields.Text(string='Deskripsi')
    user_id = fields.Many2one('res.users', string='Penanggung jawab')
    session_line_ids = fields.One2many(comodel_name='cdn.kursus.session', string='Session', inverse_name='kursus_id')
    
class KursusSession(models.Model):
    _name = 'cdn.kursus.session'
    _description = 'Tabel Kursus Session'

    name = fields.Char(string='Nama Kursus Session', required=True)
    kursus_id = fields.Many2one(comodel_name='cdn.kursus', string='Kursus', required=True, ondelete='cascade')
    start_date = fields.Date(string='Tanggal Mulai', required=True)
    duration = fields.Float(string='Durasi', required=True)
    seats = fields.Integer(string='Jumlah Peserta', compute='_compute_jml_peserta')
    peserta_ids = fields.Many2many(comodel_name='cdn.peserta', string='Peserta')
    instruktur_id = fields.Many2one(comodel_name='cdn.instruktur', string='Instruktur')
    no_hp = fields.Char(string='No. HP', related='instruktur_id.mobile')
    email = fields.Char(string='Email', related='instruktur_id.email')
    jenis_kelamin = fields.Selection(string='Jenis Kelamin', related='instruktur_id.jenis_kelamin')

    @api.depends('instruktur_id')
    def _compute_jml_peserta(self):
        for record in self:
            record.seats = len(record.peserta_ids)