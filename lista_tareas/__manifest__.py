# -*- coding: utf-8 -*-
{
    'name': "Lista Tareas",
    'summary': "Lista de tareas sencilla",
    'description': "Modulo de ODOO para crear tareas",
    'author': "SGE - Ismael Fuentes",
    'website': "http://www.google.com",
    'category': 'Productivity',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml'
        # 'views/templates.xml',
    ]
}
