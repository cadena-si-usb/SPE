# -*- coding: utf-8 -*-
from gluon import *
def Estudiante_Table(db,T):
    db.define_table('Estudiante',
        Field('usuario','reference auth_user',
              writable=False,
              unique=True,
              label='Usuario (*)'),
        Field('carnet',
              requires=IS_MATCH('^\d{2}?[\s.-]?\d{5}$',
                            error_message='Introduzca un carnet valido.'),
              label='Carnet'),
        Field('carrera', 'reference Carrera',
              label='Carrera'),
        Field('sede','reference Sede',
              requires=IS_IN_DB(db, db.Sede, '%(first_name)s',
              error_message='Elija una de las sedes.'),
              label='Sede (*)'),
        Field('activo','boolean'),
        format=lambda r: '%s - %s %s' % (r.usuario.username, r.usuario.first_name,r.usuario.last_name)
        )

    db.Estudiante.usuario.requires = IS_IN_DB(
        db(db.auth_user.username != None),
        'auth_user.id', '%(username)s - %(first_name)s %(last_name)s',
        zero='Seleccione un usuario USB', )

    if db(db.Estudiante.id > 0).count() == 0:
        db.Estudiante.insert(
            id='4',
            usuario='4',
            carnet='10-10102',
            carrera='1',
            sede='1',
            activo='True'
        )
        db.Estudiante.insert(
            id='7',
            usuario='7',
            carnet='10-10717',
            carrera='1',
            sede='1',
            activo='True'
        )
        db.commit()