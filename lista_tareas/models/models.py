# -*- coding: utf-8 -*-

from odoo import models, fields, api


class lista_tareas(models.Model):
    _name = 'lista_tareas.lista_tareas'
    _description = 'lista_tareas.lista_tareas'

    tarea = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolean()
    realizada = fields.Boolean()
    fecha_tarea = fields.Date(string="Fecha")
