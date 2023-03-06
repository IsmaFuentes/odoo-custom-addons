# -*- coding: utf-8 -*-
{
    'name': "Ciclos formativos", 
    'summary': "Gestor de ciclos formativos",
    'description': "Gestiona tus própios ciclos formativos, crea módulos, añade alumnos y profesores.",  
    'application': True,
    'author': "Ismael Fuentes Sintes",
    'website': "http://iesjoanramis.org",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/ciclos_ciclo.xml',
        'views/ciclos_alumno.xml',
        'views/ciclos_modulo.xml',
        'views/ciclos_profesor.xml'
    ],
}
