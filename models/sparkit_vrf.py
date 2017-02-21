from openerp import models, fields, api

class VisitReportForm(models.Model):
	_name = 'sparkit.vrf'
	_inherit = 'sparkit.vrf'

	#Pilot Updates (so it can be accessed via VRF for updating)
	pilot_update_ids = fields.One2many(related='community_id.pilot_update_ids')
