# -*- coding: utf-8 -*-
from datetime import datetime

db.define_table('Preinscripcion',
    Field('pasantia','reference Pasantia',
          requires=IS_IN_DB(db, db.Pasantia,
                            error_message='Elija una de las Pasantia.'),
           label='Pasantia'),
    Field('estado', 'string',default="En Espera"),
    Field('aprobacionCCT', 'boolean',label='Aprobacion De La CCT'),
    Field('comentarioCCT','text', label='Comentario De La CCT'),
    Field('fecha_creacion','datetime',default=datetime.now()), migrate='Preinscripcion.table')

