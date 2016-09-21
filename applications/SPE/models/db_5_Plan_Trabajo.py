# -*- coding: utf-8 -*-


db.define_table('Plan_Trabajo',
    Field('pasantia','reference Pasantia',
          requires=IS_IN_DB(db, db.Pasantia,
          error_message='Elija uno de las pasantías.'),
          label='Pasantia (*)'),
    Field('aprobacion_tutor_academico', 'string', default='En espera', label='Aprobacion Del Tutor Academico'),
    Field('aprobacion_tutor_industrial', 'string', default='En espera', label='Aprobacion Del Tutor Industrial'),
    Field('aprobacion_coordinacion', 'string', default='En espera', label='Aprobacion De La Coordinacion'),
    Field('fecha_creacion','datetime',default=datetime.now()),
    Field('fecha_envio','datetime'),
    Field('estado','string',default="Sin Enviar")
)
