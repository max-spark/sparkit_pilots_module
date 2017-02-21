# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Community(models.Model):
	_name = 'sparkit.community'
	_inherit = 'sparkit.community'


	pilot_ids = fields.Many2many('sparkit.pilot', string="Pilots",
		track_visibility='onchange')
	pilot_update_ids = fields.One2many('sparkit.pilotupdate', 'community_id')
