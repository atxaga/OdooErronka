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
    'depends': ['base', 'calendar'],
    'data': [
        'security/security_groups.xml',
        'security/student_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/student_views.xml',
    ],
    # 'demo': ['demo/demo.xml'],  # bakarrik bada existitzen
}
