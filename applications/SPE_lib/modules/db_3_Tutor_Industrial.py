# -*- coding: utf-8 -*-
from gluon import *
def Tutor_Industrial(db,T):
    # Tutor Industrial
    db.define_table('Tutor_Industrial',
                        Field('usuario','reference UsuarioExterno',label=T('Usuario'),),
                        Field('apellido','string',label=T('Apellido'),),
                        Field('Empresa','reference Empresa',required=True, notnull=True,label=T('Empresa')),
                        Field('profesion','string',label=T('Profesion')),
                        Field('tipo_documento','reference Tipo_Documento',
                              label='Tipo de Documento (*)'),
                        Field('numero_documento',
                              requires=[IS_MATCH('^[0-9][0-9]*$',
                                                 error_message='Introduzca una cedula.')],
                              label='Numero Documentacion (*)'),
                        Field('cargo','string',label=T('Cargo')),
                        Field('departamento','string',label=T('Departamento')),
                        Field('universidad','reference Universidad',label=T('Universidad')),
                        Field('comfirmado_Por_Empresa','integer',label=T('Comfirmado Por Empresa'), default=0, requires=IS_IN_SET([0,1],zero=None),represent=lambda v, r: 'Aprobado' if v==1 else 'No Aprobado'),
                        format = lambda r: '%s %s - %s' % (r.usuario.nombre, r.apellido,r.usuario.correo))

    # Validadores
    db.Tutor_Industrial.apellido.requires=[IS_LENGTH(512)]
    db.Tutor_Industrial.apellido.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
