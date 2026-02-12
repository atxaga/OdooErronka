{
    'name': "Xabier Zubiri Manteo Kudeaketa",
    'technical_name': 'xabier_zubiri_manteo_kudeaketa',
    'summary': "Module to manage students, equipment, and incidents",
    'description': """
Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/security_groups.xml', 
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/incident_views.xml',
        'views/menu.xml',
    ],
    # 'demo': ['demo/demo.xml'],  # bakarrik bada existitzen
}
