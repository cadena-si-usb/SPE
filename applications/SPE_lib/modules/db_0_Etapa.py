# -*- coding: utf-8 -*-
from gluon import *
def Etapa(db,T):
    db.define_table('Etapa',
        Field('nombre','string'),
        Field('procedimientos','string'),
        Field('descripcion','string'),
        format='%(nombre)s')