# -*- coding: utf-8 -*-

from email.policy import default
from attr import field
from pkg_resources import require
from requests import request
from soupsieve import select
from odoo import models, fields, api


class device(models.Model):
    _name = 'invetorytic.device'
    _description = 'invetorytic.device'

    model = fields.Char(string='Modelo del activo', required=True, size=50)
    state = fields.Selection(string='Estado del dispositivo', required=True,
                             default='I', selection=[('I', 'Inactivo'), ('A', 'Activado')])
    add = fields.Date(string="Fecha de compra")
    description = fields.Text(string='Detalle del activo')
    value = fields.Integer(string='Valor monetario del activo')
    maintenance_ids = fields.Many2many(
        'invetorytic.maintenance', string='Mantenimientos')
    """Validacions por modelo"""
    #_sql_contraints = [('model_uniq', 'unique(model)', 'El modelo ya existe')]


class maintenance(models.Model):
    _name = 'invetorytic.maintenance'
    _description = 'Matenimiento de los activos'
    _order = 'date'

    date = fields.Date('Fecha', required=True, default=fields.date.today())
    type = fields.Selection(string='Tipo', selection=[
                            ('P', 'Preventivo'), ('C', 'Correctivo')])
    cost = fields.Float('Costo', (8, 2), help='Coste del mantenimiento')
    device_ids = fields.Many2many('invetorytic.device', string='Activos')
