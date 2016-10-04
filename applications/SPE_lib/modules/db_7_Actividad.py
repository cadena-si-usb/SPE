# -*- coding: utf-8 -*-
from gluon import *
def Actividad(db,T):
    db.define_table('Actividad',
        Field('fase','reference Fase',
            label = 'Fase'),
        Field('numero','integer',
              requires=[IS_NOT_EMPTY
                            (error_message='Es necesario un numero de identificacion')],
              label = 'Numero'),
        Field('descripcion','text',
              requires=[IS_NOT_EMPTY
                       (error_message='Es necesario una descripcion.')]),
        Field('semana_inicio','string',
             requires=[IS_IN_SET([0,1,2,3,4,5,6,7,8,9,10,11,12,13])]),
        Field('semana_fin','string',
             requires=[IS_IN_SET([0,1,2,3,4,5,6,7,8,9,10,11,12,13])]),
    )

