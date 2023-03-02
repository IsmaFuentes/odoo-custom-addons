# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CicloFormativo(models.Model):
    # parámetros de configuración
    _name = 'ciclos.ciclo'
    _description = 'Ciclos formativos'
    _rec_name = 'nombre'

    # propiedades del modelo
    nombre = fields.Char('Nombre', required=True)
    descripcion = fields.Text('Descripción', required=True)
    modulos = fields.One2many('ciclos.modulo', 'ciclo', string="Modulos")