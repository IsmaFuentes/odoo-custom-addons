# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Alumno(models.Model):
    # parámetros de configuración
    _name = 'ciclos.alumno'
    _description = 'Alumnos'
    _rec_name = 'nombre'

    # propiedades del modelo
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char("Apellidos", required=True)
    expediente = fields.Char("Expediente", required=True)