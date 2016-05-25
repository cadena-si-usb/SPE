# -*- coding: utf-8 -*-
# Division
db.define_table('Division',
                Field('nombre','string',required=True),
                format='%(nombre)s'
               )

db.Division.nombre.requires+=[IS_LENGTH(100)]
db.Division.nombre.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
