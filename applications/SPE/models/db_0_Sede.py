# -*- coding: utf-8 -*-

db.define_table('Sede',
    Field('nombre','string',
           label = 'Nombre'),
    format='%(nombre)s'
)
