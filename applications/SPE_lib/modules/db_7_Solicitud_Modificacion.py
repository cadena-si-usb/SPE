# -*- coding: utf-8 -*-
from gluon import *
def Solicitud_Modificacion_Table(db,T):
    db.define_table('Solicitud_Modificacion',
                    Field('pasantia', 'reference Pasantia', label='Pasantia (*)'),
                    Field('justificacion','text',label='Justificacion'),
                    Field('cambios_solicitados','text', label='Cambios solicitados'),
                    Field('aprobacion_tutor_academico','boolean', label='Aprobacion del Tutor Academico'),
                    Field('aprobacion_coordinacion_carrera','boolean', label='Aprobacion de la Coordinacion de carrera'),
                    Field('procesado_CCT','boolean', label='Procesado por la CCT'),
                   )
    db.commit()
