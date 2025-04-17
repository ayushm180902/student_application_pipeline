{
    'name': 'Student Application Pipeline',
    'version': '1.0',
    'summary': 'Manage student applications to universities',
    'description': """
        This module helps educational consultants manage student applications to universities.
        Features:
        - Track student applications through different stages
        - Manage university information
        - Pipeline view similar to CRM
    """,
    'category': 'Education',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/university_views.xml',
        'views/stage_views.xml',
        'views/process_pipeline_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}