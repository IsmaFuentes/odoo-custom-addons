# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Profesor(models.Model):
    # parámetros de configuración
    _name = 'ciclos.profesor'
    _description = 'Profesores'
    _rec_name = 'nombre'

    # propiedades del modelo
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char("Apellidos", required=True)
    modulos = fields.One2many('ciclos.modulo', 'profesor', string="Modulos")