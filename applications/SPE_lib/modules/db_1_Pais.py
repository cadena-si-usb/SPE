# -*- coding: utf-8 -*-
from gluon import *
def Pais_Table(db,T):
    db.define_table('Pais',
        Field('first_name','string'),
        Field('ddi', 'string'),
        format='%(first_name)s')

    if db(db.Pais.id > 0).count() == 0:
        db.Pais.insert(
            first_name='Venezuela',
            ddi='',
        )
        db.Pais.insert(
            first_name='U.S.A.',
            ddi='',
        )
        db.commit()