# -*- coding: utf-8 -*-
from gluon import *
def Periodo(db,T):
    db.define_table('Periodo',
        Field('mes_inicio','string'),
        Field('mes_final','string'),
        format='%(mes_inicio)s - %(mes_final)s'
    )