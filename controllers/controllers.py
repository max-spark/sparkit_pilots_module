# -*- coding: utf-8 -*-
from openerp import http

# class SparkitLearningPilots(http.Controller):
#     @http.route('/sparkit_learning_pilots/sparkit_learning_pilots/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sparkit_learning_pilots/sparkit_learning_pilots/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sparkit_learning_pilots.listing', {
#             'root': '/sparkit_learning_pilots/sparkit_learning_pilots',
#             'objects': http.request.env['sparkit_learning_pilots.sparkit_learning_pilots'].search([]),
#         })

#     @http.route('/sparkit_learning_pilots/sparkit_learning_pilots/objects/<model("sparkit_learning_pilots.sparkit_learning_pilots"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sparkit_learning_pilots.object', {
#             'object': obj
#         })