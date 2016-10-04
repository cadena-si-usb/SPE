# -*- coding: utf-8 -*-
from gluon import *
def Materia_Periodo(db,T):
    db.define_table('Materia_Periodo',
        Field('materia','reference Materia',
              label='Materia (*)'),
        Field('periodo','reference Periodo',
              label='Periodo (*)')
    )

