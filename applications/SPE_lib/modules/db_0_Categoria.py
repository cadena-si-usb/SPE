# -*- coding: utf-8 -*-
from gluon import *

def Categoria(db,T):
    db.define_table('Categoria',
        Field('nombre','string'),
        format='%(nombre)s')