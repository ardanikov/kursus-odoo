from odoo import models, fields, api

class Pendaftaran(models.Model):
    _name = 'cdn.pendaftaran'
    _description = 'Tabel Pendaftaran'

    name = fields.Char(string='Nomor Pendaftaran', readonly=True)
    tanggal = fields.Date(string='Tanggal', default=fields.Date.today, required=True)
    pendaftar_id = fields.Many2one(comodel_name='cdn.peserta', string='Pendaftar', required=True)
    jenis_kelamin = fields.Selection(string='Jenis Kelamin', related="pendaftar_id.jenis_kelamin", readonly=True)
    no_hp = fields.Char(string='No. HP', related='pendaftar_id.mobile', readonly=True)
    kursus_id = fields.Many2one(comodel_name='cdn.kursus', string='Kursus', required=True)
    # session_id = fields.Many2one(comodel_name='cdn.kursus.session', string='Session', required=True)
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('confirm', 'Confirm')], default='draft')
    harga_kursus_total = fields.Float(string='Harga Kursus Total', related="kursus_id.harga_kursus_total", readonly=True)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('sequence.pendaftaran')
        return super(Pendaftaran, self).create(vals)

    def action_confirm(self):
        for record in self:
            if record.state == 'draft':
                record.state = 'confirm'

    def action_reset(self):
        for record in self:
            record.state = 'draft'