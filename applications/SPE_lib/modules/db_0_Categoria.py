# -*- coding: utf-8 -*-
from gluon import *


def Categoria_Table(db, T):
    db.define_table('Categoria',
                    Field('first_name', 'string', unique=True),
                    format='%(first_name)s')

    if db(db.Categoria.id > 0).count() == 0:
        db.Categoria.insert(
            first_name='Asociado'
        )
        db.Categoria.insert(
            first_name='Titular'
        )
        db.Categoria.insert(
            first_name='Agregado'
        )
        db.Categoria.insert(
            first_name='Asistente'
        )
        db.commit()
