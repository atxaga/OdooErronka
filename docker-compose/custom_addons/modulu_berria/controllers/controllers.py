# from odoo import http


# class ModuluBerria(http.Controller):
#     @http.route('/modulu_berria/modulu_berria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulu_berria/modulu_berria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulu_berria.listing', {
#             'root': '/modulu_berria/modulu_berria',
#             'objects': http.request.env['modulu_berria.modulu_berria'].search([]),
#         })

#     @http.route('/modulu_berria/modulu_berria/objects/<model("modulu_berria.modulu_berria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulu_berria.object', {
#             'object': obj
#         })

