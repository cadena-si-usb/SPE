# -*- coding: utf-8 -*-
from gluon import *

def Dedicacion_Table(db,T):
    db.define_table('Dedicacion',
        Field('first_name','string'),
        format='%(first_name)s')

    if db(db.Dedicacion.id > 0).count() == 0:
        db.Dedicacion.insert(
            first_name='Exclusiva'
        )
        db.commit()