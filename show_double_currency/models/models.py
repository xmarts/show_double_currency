# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class show_double_currency(models.Model):
#     _name = 'show_double_currency.show_double_currency'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class CRMAddCurrency(models.Model):
	"""Add double currency"""
	_inherit = "crm.lead"

	second_currency_id = fields.Many2one("res.currency", default=lambda self: self.env['res.currency'].search([('name','=','USD')], limit=1).id or '', readonly=True)
	usd_price = fields.Monetary(string="Cantidad en USD", currency_field='second_currency_id')
	ing_usd = fields.Boolean(string="Ingresar en USD", default=False)


	@api.onchange('usd_price')
	def _onchange_usd_price(self):
		self.planned_revenue = self.env['res.currency']._compute(self.company_currency,self.second_currency_id,self.usd_price)