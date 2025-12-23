from odoo import models, fields, api

class DaftarHadir(models.Model):
    _name = "cdn.daftar_hadir"
    _description = "Daftar Hadir"
    _rec_name = "tanggal"

    tanggal = fields.Date(string="Tanggal", default=fields.Date.today, required=True)
    kursus_id = fields.Many2one("cdn.kursus", string="Kursus", required=True)
    state = fields.Selection(string="Status", selection=[('draft', 'Draft'), ('confirm', 'Confirm')], default='draft')
    session_id = fields.Many2one("cdn.kursus.session", string="Sesi", domain="[('kursus_id', '=', kursus_id)]", required=True)
    harga_kursus_total = fields.Float(string="Harga Kursus", related="session_id.kursus_id.harga_kursus_total")
    daftar_hadir_ids = fields.One2many(comodel_name="cdn.daftar_hadir_line", inverse_name="daftar_hadir_id", string="Detail Kehadiran")
    jml_peserta_hadir = fields.Integer(string="Peserta Hadir", compute="_compute_peserta_hadir")

    @api.onchange('kursus_id')
    def _onchange_kursus_id(self):
        if self.kursus_id:
            pendaftaran_records = self.env['cdn.pendaftaran'].search([('kursus_id', '=', self.kursus_id.id), ('state', '=', 'confirm')])
            line = []
            for reg in pendaftaran_records:
                line.append((0, 0, {'peserta_id': reg.pendaftar_id.id, 'is_hadir': 'hadir',}))
            
            self.daftar_hadir_ids = [(5, 0, 0)] + line

    def action_confirm(self):
        for record in self:
            if record.state == 'draft':
                record.state = 'confirm'

    def action_reset(self):
        for record in self:
            record.state = 'draft'

    @api.depends('daftar_hadir_ids')
    def _compute_peserta_hadir(self):
        for record in self:
            record.jml_peserta_hadir = len(record.daftar_hadir_ids.filtered(lambda x: x.is_hadir == 'hadir'))

class DaftarHadirLine(models.Model):
    _name = "cdn.daftar_hadir_line"
    _description = "Detail Daftar Hadir"

    daftar_hadir_id = fields.Many2one("cdn.daftar_hadir")
    peserta_id = fields.Many2one("cdn.peserta", string="Peserta")
    is_hadir = fields.Selection(string="Hadir", selection=[('hadir', 'Hadir'), ('tidak_hadir', 'Tidak Hadir'), ('izin', 'Izin')], default='hadir', required=True)


    
