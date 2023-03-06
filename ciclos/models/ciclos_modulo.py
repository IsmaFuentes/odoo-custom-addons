# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Modulo(models.Model):
    # parámetros de configuración
    _name = 'ciclos.modulo'
    _description = 'Módulos'
    _rec_name = 'nombre'

    # propiedades del modelo
    nombre = fields.Char('Nombre', required=True)
    descripcion = fields.Text('Descripción', required=True)
    ciclo = fields.Many2one('ciclos.ciclo')
    profesor = fields.Many2one('ciclos.profesor')
    alumnos = fields.Many2many('ciclos.alumno', string="Alumnos")