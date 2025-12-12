from odoo import models, fields, api, _

class Provinsi(models.Model):
    _name = 'cdn.provinsi'
    _description = 'Tabel Provinsi'

    name = fields.Char(string='Nama Provinsi', required=True)
    kode = fields.Char(string='Kode Provinsi', required=True)
    singkatan = fields.Char(string='Singkatan',)
    description = fields.Text(string='Deskripsi')

    kota_ids = fields.One2many(comodel_name='cdn.kota', string='Kota', inverse_name='provinsi_id')

class Kota(models.Model):
    _name = 'cdn.kota'
    _description = 'Tabel Kota'

    name = fields.Char(string='Nama Kota', required=True)
    kode = fields.Char(string='Kode Kota', required=True)
    singkatan = fields.Char(string='Singkatan',)
    description = fields.Text(string='Deskripsi')

    provinsi_id = fields.Many2one(comodel_name='cdn.provinsi', string='Provinsi', required=True)
    kecamatan_ids = fields.One2many(comodel_name='cdn.kecamatan', string='Kecamatan', inverse_name='kota_id')

class Kecamatan(models.Model):
    _name = 'cdn.kecamatan'
    _description = 'Tabel Kecamatan'

    name = fields.Char(string='Nama Kecamatan', required=True)
    kode = fields.Char(string='Kode Kecamatan', required=True)
    singkatan = fields.Char(string='Singkatan',)
    description = fields.Text(string='Deskripsi')

    kota_id = fields.Many2one(comodel_name='cdn.kota', string='Kota', required=True)
    desa_ids = fields.One2many(comodel_name='cdn.desa', string='Desa', inverse_name='kecamatan_id')

class Desa(models.Model):
    _name = 'cdn.desa'
    _description = 'Tabel Desa'

    name = fields.Char(string='Nama Desa', required=True)
    kode = fields.Char(string='Kode Desa', required=True)
    singkatan = fields.Char(string='Singkatan',)
    description = fields.Text(string='Deskripsi')

    kecamatan_id = fields.Many2one(comodel_name='cdn.kecamatan', string='Kecamatan', required=True)