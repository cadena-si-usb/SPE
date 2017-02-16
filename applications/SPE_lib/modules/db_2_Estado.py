# -*- coding: utf-8 -*-
from gluon import *
def Estado_Table(db,T):
    db.define_table('Estado',
        Field('first_name','string', unique=True),
        Field('Pais', 'reference Pais'),
        format=lambda r: '%s - %s' % (r.Pais.first_name, r.first_name))

    if db(db.Estado.id > 0).count() == 0:
        db.Estado.insert(
            first_name='Distrito Capital',
            Pais=1
        )
        db.Estado.insert(
            first_name='Aragua',
            Pais=1
        )
        db.commit()