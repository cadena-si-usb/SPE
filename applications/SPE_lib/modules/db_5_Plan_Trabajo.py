# -*- coding: utf-8 -*-
from gluon import *
from datetime import datetime
def Plan_Trabajo_Table(db,T):
    db.define_table('Plan_Trabajo',
        Field('pasantia','reference Pasantia',
              label='Pasantia (*)'),
        Field('aprobacion_tutor_academico', 'string',
              requires=IS_IN_SET(['En espera', 'Aprobado'],zero=None,
                                error_message='Opcion Invalida'),
              default='En espera', label='Aprobacion Del Tutor Academico',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('aprobacion_tutor_industrial', 'string',
              requires=IS_IN_SET(['En espera', 'Aprobado'], zero=None,
                                error_message='Opcion Invalida'),
              default='En espera', label='Aprobacion Del Tutor Industrial',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('aprobacion_coordinacion', 'string',
              requires=IS_IN_SET(['En espera', 'Aprobado'], zero=None,
                                error_message='Opcion Invalida'),
              default='En espera', label='Aprobacion De La Coordinacion',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('fecha_creacion','datetime',default=datetime.now(),
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('fecha_envio','datetime',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('estado','string',requires=IS_IN_SET(['Sin Enviar', 'Enviado'],zero=None,
                                error_message='Opcion Invalida'),
              default="Sin Enviar",
              represent=lambda v, r: 'N/A' if v is None else v),
        format=lambda r: 'Plan De Trabajo De La Pasantia "%s"' % (r.pasantia.titulo)
    )
