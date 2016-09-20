from datetime import datetime
# -*- coding: utf-8 -*-

db.define_table('Colocacion',
    Field('pasantia', 'reference Pasantia',
          requires=IS_IN_DB(db, db.Pasantia,
                            error_message='Elija una de las Pasantia.'),
          label='Pasantia'),
    Field('aprobacionCCT', 'boolean',label='Aprobacion De La CCT'),
    Field('comentarioCCT','text', label='Comentario De La CCT'),
    Field('estado', 'string',default="En Espera"),
    Field('fecha_creacion','datetime',default=datetime.now()))

