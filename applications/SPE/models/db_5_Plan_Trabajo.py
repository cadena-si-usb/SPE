# -*- coding: utf-8 -*-


db.define_table('Plan_Trabajo',
    Field('pasantia','reference Pasantia',
          requires=IS_IN_DB(db, db.Pasantia,
          error_message='Elija uno de las pasantías.'),
          label='Pasantia (*)'),
    Field('aprobacion_tutor_academico', 'boolean', label='Aprobar'),
    Field('aprobacion_tutor_industrial', 'boolean', label='Aprobar'),
    Field('aprobacion_coordinacion', 'boolean', label='Aprobar')
)
