from odoo import models, fields, api

class Peserta(models.Model):
    _name = 'cdn.peserta'
    _description = 'Tabel Peserta'
    _inherits = {'res.partner': 'partner_id'}
    
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner', ondelete='cascade', required=True)
    pendidikan = fields.Selection(selection=[('sd', 'SD'), ('smp', 'SMP'), ('sma', 'SMA'), ('d1', 'D1'), ('d2', 'D2'), ('d3', 'D3'), ('s1', 'S1'), ('s2', 'S2'), ('s3', 'S3')], string='Pendidikan')
    is_menikah = fields.Boolean(string='Sudah Menikah')
    nama_pasangan = fields.Char(string='Nama Pasangan')
    pekerjaan = fields.Char(string='Pekerjaan')
    hp_pasangan = fields.Char(string='No. HP Pasangan')
    tmp_lahir = fields.Char(string='Tempat Lahir')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    profile_image = fields.Image(string='Foto Profil', max_width=256, max_height=256)
    kursus_session_ids = fields.Many2many(comodel_name='cdn.kursus.session', string='Sesi Kursus')
    no_peserta = fields.Char(string='No. Peserta', readonly=True)
    @api.model
    def create(self, vals):
        vals['no_peserta'] = self.env['ir.sequence'].next_by_code('sequence.peserta')
        return super(Peserta, self).create(vals)
        