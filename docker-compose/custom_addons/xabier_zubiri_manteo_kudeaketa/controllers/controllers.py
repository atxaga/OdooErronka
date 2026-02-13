# from odoo import http


# class Xabier-zubiriManteoKudeaketa(http.Controller):
#     @http.route('/xabier-zubiri__manteo_kudeaketa/xabier-zubiri__manteo_kudeaketa', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xabier-zubiri__manteo_kudeaketa/xabier-zubiri__manteo_kudeaketa/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('xabier-zubiri__manteo_kudeaketa.listing', {
#             'root': '/xabier-zubiri__manteo_kudeaketa/xabier-zubiri__manteo_kudeaketa',
#             'objects': http.request.env['xabier-zubiri__manteo_kudeaketa.xabier-zubiri__manteo_kudeaketa'].search([]),
#         })

#     @http.route('/xabier-zubiri__manteo_kudeaketa/xabier-zubiri__manteo_kudeaketa/objects/<model("xabier-zubiri__manteo_kudeaketa.xabier-zubiri__manteo_kudeaketa"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xabier-zubiri__manteo_kudeaketa.object', {
#             'object': obj
#         })
