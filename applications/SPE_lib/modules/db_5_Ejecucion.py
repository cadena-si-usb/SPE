# -*- coding: utf-8 -*-
from datetime import datetime
from gluon import *
def Ejecucion(db,T):
    db.define_table('Ejecucion',
        Field('pasantia', 'reference Pasantia',
              label='Pasantia'),
        Field('aprobacionCCT', 'boolean',label='Aprobacion De La CCT',default=False,
              represent=lambda v, r: 'Aprobado' if v==True else 'En Espera'),
        Field('comentarioCCT','text', label='Comentario De La CCT'),

        Field('fecha_creacion','datetime',default=datetime.now()),
        Field('estado', 'string',default="En Espera"))

