# -*- coding: utf-8 -*-

# Tutor Industrial
db.define_table('Tutor_Industrial',
                    Field('usuario','reference UsuarioExterno',label=T('Usuario'),),
                    Field('apellido','string',label=T('Apellido'),),
                    Field('Empresa','reference Empresa',required=True, notnull=True,label=T('Empresa')),
                    Field('profesion','string',label=T('Profesion')),
                    Field('tipo_documento',
                          requires=IS_IN_SET(['CI', 'Pasaporte']),
                          label='Tipo de Documento (*)'),
                    Field('numero_documento',
                          requires=[IS_MATCH('^[0-9][0-9]*$',
                                             error_message='Introduzca una cedula.')],
                          label='Numero Documentacion (*)'),
                    Field('cargo','string',label=T('Cargo')),
                    Field('departamento','string',label=T('Departamento')),
                    Field('universidad','reference Universidad',label=T('Universidad')),
                    Field('comfirmado_Por_Empresa','integer',label=T('Comfirmado Por Empresa'), default=0, requires=IS_INT_IN_RANGE(minimum=0, maximum=1)))

# Validadores
db.Tutor_Industrial.apellido.requires=[IS_LENGTH(512)]
db.Tutor_Industrial.apellido.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]

#db.Tutor_Industrial.Empresa.requires=IS_IN_DB(db,db.Empresa.id,'%(usuario)s',error_message=T('Elija Una Empresa Valida'),zero=None)

db.Tutor_Industrial.universidad.requires=IS_IN_DB(db,db.Universidad.id,'%(nombre)s',error_message=T('Elija Una Universidad Valida'),zero=None)
