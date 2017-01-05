# -*- coding: utf-8 -*-
from gluon import *
def Estado_Table(db,T):
    db.define_table('Estado',
        Field('first_name','string'),
        Field('Pais', 'reference Pais'),
        format=lambda r: '%s - %s' % (r.Pais.first_name, r.first_name))