# -*- coding: utf-8 -*-
from gluon import *
def Evaluacion_Visita_Table(db,T):
    db.define_table('Evaluacion_Visita',
    	# Arreglar y poner a funcionar con el permiso correspondiente
    	Field('pasantia', 'Reference Pasantia'),
        #Field('permiso','reference Permisos', label='Permiso (*)'),
        Field('respuesta_1','text',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('respuesta_2', 'text',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('respuesta_3', 'text',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('respuesta_4', 'text',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('respuesta_5', 'text',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('respuesta_6', 'text',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('respuesta_7', 'text',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('respuesta_8', 'text',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('respuesta_9', 'text',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('respuesta_10', 'text',
              represent=lambda v, r: 'N/A' if v is None else v),
    )
