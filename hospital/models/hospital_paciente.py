# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Paciente(models.Model):
    # parámetros de configuración
    _name = 'hospital.paciente'
    _description = 'Paciente del hospital'
    _rec_name = "nombre"

    # propiedades del modelo
    nombre = fields.Char("Nombre", required=True)
    apellidos = fields.Char("Apellidos", required=True)
    sintomas = fields.Text("Síntomas", required=True)