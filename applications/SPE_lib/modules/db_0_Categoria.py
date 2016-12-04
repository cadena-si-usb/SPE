# -*- coding: utf-8 -*-
from gluon import *

def Categoria_Table(db,T):
    db.define_table('Categoria',
        Field('first_name','string'),
        format='%(first_name)s')