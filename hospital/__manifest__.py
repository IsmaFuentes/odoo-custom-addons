# -*- coding: utf-8 -*-
{
    'name': "Hospital", 
    'summary': "Gestor Hospital",
    'description': "Gestión de pacientes y médicos de un hospital",  
    'application': True,
    'author': "Ismael Fuentes Sintes",
    'website': "http://iesjoanramis.org",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_medico.xml',
        'views/hospital_paciente.xml',
        'views/hospital_diagnostico.xml'
    ],
}
