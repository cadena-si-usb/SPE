# -*- coding: utf-8 -*-
from datetime import datetime
from gluon import *
def Preinscripcion(db,T):
    db.define_table('Preinscripcion',
        Field('pasantia','reference Pasantia',
               label='Pasantia'),
        Field('estado', 'string',default="En Espera"),
        Field('aprobacionCCT', 'boolean',label='Aprobacion De La CCT'),
        Field('comentarioCCT','text', label='Comentario De La CCT'),
        Field('fecha_creacion','datetime',default=datetime.now()))

