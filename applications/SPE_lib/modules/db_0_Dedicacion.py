# -*- coding: utf-8 -*-
from gluon import *

def Dedicacion(db,T):
    db.define_table('Dedicacion',
        Field('nombre','string'),
        format='%(nombre)s')