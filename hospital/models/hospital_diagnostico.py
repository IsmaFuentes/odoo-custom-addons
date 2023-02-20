# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Diagnostico(models.Model):
    # parámetros de configuración
    _name = 'hospital.diagnostico'
    _description = 'Diagnostico del paciente'
    _rec_name = "paciente"

    # propiedades del modelo
    medico = fields.Many2one('hospital.medico', string="Médico")
    paciente = fields.Many2one('hospital.paciente', string="Paciente")
    descripcion = fields.Text("Descripción", required=True)