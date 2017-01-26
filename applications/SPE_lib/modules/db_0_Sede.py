# -*- coding: utf-8 -*-
from gluon import *


def Sede_Table(db, T):
    db.define_table('Sede',
                    Field('first_name', 'string',
                          label='Nombre', unique=True),
                    format='%(first_name)s'
                    )

    if db(db.Sede.id > 0).count() == 0:
        db.Sede.insert(
            first_name='Sartenejas'
        )
        db.Sede.insert(
            first_name='Litoral'
        )
        db.commit()
