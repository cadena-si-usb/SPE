# -*- coding: utf-8 -*-

db.define_table('Rol',
    Field('nombre','string',
           label = 'Nombre Rol'),
    format='%(nombre)s'
)
