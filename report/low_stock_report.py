# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, api
from odoo.exceptions import UserError


class low_stock_template(models.AbstractModel):
    _name = 'report.bi_product_low_stock_notification.low_stock_template'

    @api.model
    def _get_report_values(self, docids, data=None):

        rec_ids = []
        low_stock_transient = self.env['low.stock.transient']
        for rec in low_stock_transient.search([]):
            rec_ids.append(rec)
        return {'doc_ids': docids, 'data': data, 'docs': rec_ids, 'rec_ids': rec_ids,}
