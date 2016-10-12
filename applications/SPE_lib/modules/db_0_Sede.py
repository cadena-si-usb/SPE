# -*- coding: utf-8 -*-
from gluon import *
def Sede_Table(db,T):
    db.define_table('Sede',
        Field('nombre','string',
               label = 'Nombre'),
        format='%(nombre)s'
    )
