# -*- coding: utf-8 -*-
from gluon import *
def Coordinador_Table(db,T):
    db.define_table('Coordinador',
        Field('usuario','reference UsuarioUSB',
              label='Usuario (*)'),
        Field('carnet',
              requires=IS_MATCH('^\d{2}?[\s.-]?\d{5}$',
                            error_message='Introduzca un carnet valido.'),
              label='Carnet'),
        Field('coordinacion','reference Coordinacion',
              label='Coordinacion (*)'),
        Field('correo_Alternativo',  requires=IS_EMAIL(error_message='Introduzca un email valido.'),
              label='Correo Alternativo'),
        format = lambda r: '%s - %s %s' % (r.usuario.usbid, r.usuario.first_name, r.usuario.last_name))