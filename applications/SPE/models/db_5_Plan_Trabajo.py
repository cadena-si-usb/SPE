# -*- coding: utf-8 -*-


db.define_table('Plan_Trabajo',
    Field('pasantia','reference Pasantia',
          requires=IS_IN_DB(db, db.Pasantia, '%(titulo)s',
          error_message='Elija uno de las pasantías.'),
          label='Pasantia (*)'),
    Field('aprobacion_tutor_academico', 'integer', default=0, requires=IS_INT_IN_RANGE(minimum=0, maximum=1),
          label='Obejtivos Especificos'),
    Field('aprobacion_Tutor_Industrial', 'integer', default=0,requires=IS_INT_IN_RANGE(minimum=0, maximum=1),
          label='Obejtivos Especificos'),
    Field('aprobacion_coordinacion', 'integer', default=0, requires=IS_INT_IN_RANGE(minimum=0, maximum=1),
          label='Obejtivos Especificos'),
)
