# -*- coding: utf-8 -*-
from gluon import *
def Profesor_Table(db,T):
    db.define_table('Profesor',
           Field('usuario','reference UsuarioUSB',
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
        format=lambda r: '%s - %s %s' % (r.usuario.usbid, r.usuario.nombre,r.usuario.apellido)
    )