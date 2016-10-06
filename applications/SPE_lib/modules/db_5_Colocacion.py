# -*- coding: utf-8 -*-
from datetime import datetime
from gluon import *
def Colocacion(db,T):
    db.define_table('Colocacion',
        Field('pasantia', 'reference Pasantia',
              label='Pasantia'),
        Field('aprobacionCCT', 'boolean',label='Aprobacion De La CCT'),
        Field('comentarioCCT','text', label='Comentario De La CCT'),
        Field('estado', 'string',default="En Espera",
              requires=IS_IN_SET(['En espera', 'Aprobado'], zero=None,
                                error_message='Opcion Invalida')),
        Field('fecha_creacion','datetime',default=datetime.now()))

