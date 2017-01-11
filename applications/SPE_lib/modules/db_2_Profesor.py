# -*- coding: utf-8 -*-
from gluon import *
def Profesor_Table(db,T):
    db.define_table('Profesor',
           Field('usuario','reference auth_user',
              label='Usuario (*)'),
        Field('categoria','reference Categoria',
              label='Categoria (*)'),
        Field('dedicacion','reference Dedicacion',
              label='Dedicacion (*)'),
        Field('departamento','reference Departamento',
              label='Departamento (*)'),
        Field('sede','reference Sede',
              label='Sede (*)'),
        Field('activo','boolean'),
        format=lambda r: '%s - %s %s' % (r.usuario.username, r.usuario.first_name,r.usuario.last_name)
    )

    db.Profesor.usuario.requires = IS_IN_DB(
        db(db.auth_user.username != None),
        'auth_user.id', '%(username)s - %(first_name)s %(last_name)s',
        zero='Seleccione un usuario USB', )

    if db(db.Profesor.id > 0).count() == 0:
        db.Profesor.insert(
            id='3',
            usuario='3',
            categoria='1',
            dedicacion='1',
            departamento='1',
            sede='1',
            activo='True'
        )
        db.Profesor.insert(
            id='5',
            usuario='5',
            categoria='1',
            dedicacion='1',
            departamento='1',
            sede='1',
            activo='True'
        )
        db.Profesor.insert(
            id='9',
            usuario='9',
            categoria='1',
            dedicacion='1',
            departamento='1',
            sede='1',
            activo='True'
        )
        db.Profesor.insert(
            id='10',
            usuario='10',
            categoria='1',
            dedicacion='1',
            departamento='1',
            sede='1',
            activo='True'
        )
        db.commit()