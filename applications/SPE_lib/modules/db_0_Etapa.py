# -*- coding: utf-8 -*-
from gluon import *
def Etapa_Table(db,T):
    db.define_table('Etapa',
        Field('first_name','string'),
        Field('procedimientos','string'),
        Field('descripcion','string'),
        format='%(first_name)s')