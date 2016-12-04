# -*- coding: utf-8 -*-
from gluon import *
def Estudiante_Table(db,T):
    db.define_table('Estudiante',
        Field('usuario','reference auth_user',
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