# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ShoppingListItem(models.Model):
    _name = 'shopping.listitem'
    _description = 'Shopping list Items'

    name = fields.Char(string="Item name", required=True)
    price = fields.Float("Price")
    description = fields.Char(string="Item description")
