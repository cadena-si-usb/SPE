# -*- coding: utf-8 -*-
from gluon import *
def Administrativo_Table(db,T):
    db.define_table('Administrativo',
        Field('usuario','reference UsuarioUSB',
              label='Usuario (*)'),
        Field('carnet',
              requires=IS_MATCH('^\d{2}?[\s.-]?\d{5}$',
                            error_message='Introduzca un carnet valido.'),
              label='Carnet'),
        Field('coordinacion','reference Coordinacion',
              label='Coordinacion (*)'),
        Field('correo_Alternativo',  requires=IS_EMAIL(error_message='Introduzca un email valido.'),
              label='Correo Alternativo'))
