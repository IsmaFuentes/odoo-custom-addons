# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Tareas(models.Model):
    _name = 'tareas.tareas'
    _description = 'tareas.tareas'

    tarea = fields.Char()
    prioridad = fields.Integer()
    realizada = fields.Boolean()
    fecha = fields.Date()