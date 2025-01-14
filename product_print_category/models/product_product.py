# Copyright (C) 2016-Today: La Louve (<http://www.lalouve.net/>)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    # Columns Section
    print_category_id = fields.Many2one(
        string="Print Category",
        comodel_name="product.print.category",
        default=lambda s: s._default_print_category_id(),
    )

    to_print = fields.Boolean(string="To Print")

    # Default Section
    def _default_print_category_id(self):
        return self.env.user.company_id.print_category_id

    @api.model
    def create(self, vals):
        if vals.get("print_category_id", False):
            vals["to_print"] = True
        return super().create(vals)

    @api.multi
    def write(self, vals):
        res = super().write(vals)
        product_ids = []
        # Set 'To print' if we change one field choosen in print_category
        for product in self.filtered(lambda x: x.print_category_id):
            triggering_fields = product.print_category_id.field_ids.mapped("name") + [
                "print_category_id"
            ]
            if len(list(set(vals.keys()) & set(triggering_fields))):
                product_ids.append(product.id)
        products = self.browse(product_ids)
        super(ProductProduct, products).write({"to_print": True})
        return res
