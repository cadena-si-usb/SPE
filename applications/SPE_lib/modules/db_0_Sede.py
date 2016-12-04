# -*- coding: utf-8 -*-
from gluon import *
def Sede_Table(db,T):
    db.define_table('Sede',
        Field('first_name','string',
               label = 'Nombre'),
        format='%(first_name)s'
    )
