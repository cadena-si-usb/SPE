# -*- coding: utf-8 -*-

db.define_table('Tipo_Documento',
    Field('nombre','string',
           label = 'Nombre'),
    format='%(nombre)s'
)
