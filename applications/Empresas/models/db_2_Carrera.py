# -*- coding: utf-8 -*-

# Estudiante
db.define_table('Carrera',
                Field('codigo','string',required=True, ondelete='CASCADE', notnull=True, label='Código'),
                Field('nombre','string',required=True, requires=[IS_LENGTH(100)], label='Nombre'),
                Field('duracion','string',required=True, requires=IS_IN_SET(['Larga','Corta']), label="Duración", notnull=True),
                Field('coordinacion','reference Coordinacion', label="Coordinación", required=True),
                format='%(codigo)s %(nombre)s'
               )
db.Carrera.codigo.requires = [IS_LENGTH(4)
        ,IS_NOT_EMPTY(error_message='Campo Obligatorio')
        ,IS_NOT_IN_DB(db, 'Carrera.codigo',error_message=T('Carrera ya existe'))
        ,IS_MATCH('[0-9]{4}',error_message=T('Solo se permiten numeros de cuatro digitos'))]
