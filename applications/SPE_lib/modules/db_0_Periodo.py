# -*- coding: utf-8 -*-
from gluon import *
def Periodo_Table(db,T):
    db.define_table('Periodo',
        Field('mes_inicio','string'),
        Field('mes_final','string'),
        format='%(mes_inicio)s - %(mes_final)s'
    )

    if db(db.Periodo.id > 0).count() == 0:
        db.Periodo.insert(
            mes_inicio='Abril',
            mes_final='Septiembre'
        )
        db.Periodo.insert(
            mes_inicio='Abril',
            mes_final='Septiembre'
        )
        db.Periodo.insert(
            mes_inicio='Octubre',
            mes_final='Enero'
        )
        db.commit()