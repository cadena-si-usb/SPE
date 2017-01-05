# -*- coding: utf-8 -*-
from gluon import *

def Dedicacion_Table(db,T):
    db.define_table('Dedicacion',
        Field('first_name','string'),
        format='%(first_name)s')