from datetime import datetime

# -*- coding: utf-8 -*-

db.define_table('Inscripcion',
    Field('pasantia', 'reference Pasantia',
          label='Pasantia'),
    Field('aprobacionCCT', 'boolean',label='Aprobacion De La CCT'),
    Field('comentarioCCT','text', label='Comentario De La CCT'),

    Field('fecha_creacion','datetime',default=datetime.now()),
    Field('estado', 'string',default="En Espera"))

