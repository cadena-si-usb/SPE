# -*- coding: utf-8 -*-
from gluon import *
def Tutor_Industrial_Table(db,T):
    # Tutor Industrial
    db.define_table('Tutor_Industrial',
                        Field('usuario','reference auth_user',label=T('Usuario'),writable=False),
                        Field('last_name','string',label=T('Apellido'),),
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
                        format = lambda r: '%s %s - %s' % (r.usuario.first_name, r.last_name,r.usuario.email))

    # Validadores
    db.Tutor_Industrial.last_name.requires=[IS_LENGTH(512)]
    db.Tutor_Industrial.last_name.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]

    if db(db.Tutor_Industrial.id > 0).count() == 0:
        db.Tutor_Industrial.insert(
            id='2',
            usuario='2',
            last_name='Sucre González',
            Empresa='1',
            profesion='Consultor De Software',
            tipo_documento='1',
            numero_documento='19564959',
            cargo='Administrador De Base De Datos',
            departamento='Tecnologia De La Informacion',
            universidad='1',
            comfirmado_Por_Empresa='1'
        )
        db.commit()