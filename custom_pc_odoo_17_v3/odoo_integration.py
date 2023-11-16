```python
from odoo import models, fields, api

class CustomPCInventory(models.Model):
    _inherit = 'product.template'

    cpu_model = fields.Char(string='CPU Model')
    gpu = fields.Char(string='GPU')
    ram = fields.Char(string='RAM')
    storage_type = fields.Char(string='Storage Type')
    storage_capacity = fields.Char(string='Storage Capacity')

class CustomPCSales(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_confirm(self):
        res = super(CustomPCSales, self).action_confirm()
        for order in self:
            order._integrate_with_crm()
        return res

    def _integrate_with_crm(self):
        self.env['crm.lead'].create({
            'name': self.name,
            'partner_id': self.partner_id.id,
            'team_id': self.team_id.id,
            'description': 'Custom PC Order: ' + self.name,
            'order_id': self.id,
        })

class CustomPCAccounting(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def action_invoice_open(self):
        res = super(CustomPCAccounting, self).action_invoice_open()
        for invoice in self:
            invoice._track_financials()
        return res

    def _track_financials(self):
        self.env['account.financial.report'].create({
            'name': self.number,
            'date': self.date_invoice,
            'company_id': self.company_id.id,
            'debit': self.amount_total_signed,
            'credit': self.amount_total_company_signed,
        })
```