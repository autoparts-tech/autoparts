from statistics import mean
from odoo import api, fields, models, _
from odoo.exceptions import UserError, Warning, ValidationError


class autopart(models.Model):
    _inherit = 'product.template'
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', ' name must be unique'), ]

    @api.multi
    @api.depends('item', 'dsc', 'drc', 'org', 'car', 'model', 'manf', 'year')
    def naming(self):
        for rec in self:
            if rec.year:
                rec.name = " ".join(
                    [rec.item or "", rec.drc or "", rec.dsc or "",
                     rec.org or "", rec.manf or "", rec.car or "",
                     rec.model or "", rec.year or ""
                     ])
            else:
                rec.name = " ".join(
                    [rec.item or "", rec.drc or "", rec.dsc or "",
                     rec.org or "", rec.manf or "", rec.car or "",
                     rec.model or "",
                     ])

    name = fields.Char(string="Name", compute=naming, store=True, required=False,)
    item = fields.Char(store=True, string="Item", required=False, )
    dsc = fields.Char(store=True, string="Description", required=False, )
    drc = fields.Char(store=True, string="Direction", required=False,)
    org = fields.Char(store=True, string="Origin", required=False,)
    manf = fields.Char(store=True, string="Origin manufacture", required=False,)
    car = fields.Char(store=True, string="Car", required=False, )
    model = fields.Char(store=True, string="Model", required=False,default='')
    year = fields.Char(store=True, string="Year", required=False, )


