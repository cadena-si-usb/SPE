# -*- coding: utf-8 -*-
from gluon import *
def Pais_Table(db,T):
    db.define_table('Pais',
        Field('nombre','string'),
        format='%(nombre)s')