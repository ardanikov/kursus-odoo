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
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('confirm', 'Confirm')], default='draft')
    harga_kursus_total = fields.Float(string='Harga Kursus Total', related="kursus_id.harga_kursus_total", readonly=True)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    invoice_id = fields.Many2one('account.move', string='Invoice')
    
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

    def action_create_invoice(self):
        Invoice  = self.env['account.move']
        for record in self:
            invoice_vals = {
                'partner_id': record.pendaftar_id.partner_id.id,
                'move_type': 'out_invoice',
                'invoice_date': fields.Date.today(),
                'invoice_line_ids': [(0, 0, {
                    'name': record.kursus_id.name,
                    'product_id': record.kursus_id.produk_kursus.id,
                    'price_unit': record.harga_kursus_total,
                    'quantity': 1,
                })],
            }
            invoice = Invoice.create(invoice_vals)
            record.invoice_id = invoice
            invoice.action_post()