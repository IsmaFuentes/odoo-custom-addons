# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Medico(models.Model):
    # parámetros de configuración
    _name = 'hospital.medico'
    _description = 'Médico del hospital'
    _rec_name = "nombre"

    # propiedades del modelo
    nombre = fields.Char("Nombre", required=True)
    apellidos = fields.Char("Apellidos", required=True)
    id_colegiado = fields.Char("Número colegiado", required=True)
