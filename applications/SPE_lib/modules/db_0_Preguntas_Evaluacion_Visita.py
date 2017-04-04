# -*- coding: utf-8 -*-
from gluon import *
from datetime import datetime


def Preguntas_Evaluacion_Visita_Table(db, T):
    db.define_table('Preguntas_Evaluacion_Visita',
        Field('pregunta_1', 'text',
              label='Pregunta 1',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('pregunta_2', 'text',
              label='Pregunta 2',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('pregunta_3', 'text',
              label='Pregunta 3',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('pregunta_4', 'text',
              label='Pregunta 4',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('pregunta_5', 'text',
              label='Pregunta 5',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('pregunta_6', 'text',
              label='Pregunta 6',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('pregunta_7', 'text',
              label='Pregunta 7',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('pregunta_8', 'text',
              label='Pregunta 8',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('pregunta_9', 'text',
              label='Pregunta 9',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('pregunta_10', 'text',
              label='Pregunta 10',
              represent=lambda v, r: 'N/A' if v is None else v),
        )
