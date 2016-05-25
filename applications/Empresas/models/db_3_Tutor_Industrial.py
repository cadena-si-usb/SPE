# -*- coding: utf-8 -*-

# Tutor Industrial
db.define_table('tutor_industrial',
                    Field('correo','reference UsuarioExterno',label=T('Correo'),),
                    Field('apellido','string',label=T('Apellido'),),
                    Field('id_empresa','reference Empresa',required=True, notnull=True,label=T('Empresa')),
                    Field('profesion','string',label=T('Profesion')),
                    Field('cargo','string',label=T('Cargo')),
                    Field('departamento','string',label=T('Departamento')),
                    Field('id_universidad','reference Universidad',label=T('Universidad')),
                    format='%(correo)s %(nombre)s %(apellido)s')

# Validadores
db.tutor_industrial.apellido.requires=[IS_LENGTH(512)]
db.tutor_industrial.apellido.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]

db.tutor_industrial.id_empresa.requires=IS_IN_DB(db,db.Empresa.id,'%(log)s - %(nombre)s',error_message=T('Elija Una Empresa Valida'),zero=None)

db.tutor_industrial.id_universidad.requires=IS_IN_DB(db,db.Universidad.id,'%(nombre)s',error_message=T('Elija Una Universidad Valida'),zero=None)
