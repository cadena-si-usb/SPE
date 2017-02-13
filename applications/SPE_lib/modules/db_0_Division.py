# -*- coding: utf-8 -*-
from gluon import *


# Division
def Division_Table(db, T):
    db.define_table('Division',
                    Field('first_name', 'string', required=True, unique=True),
                    format='%(first_name)s'
                    )

    db.Division.first_name.requires += [IS_LENGTH(100)]
    db.Division.first_name.requires += [IS_NOT_EMPTY(error_message='Campo Obligatorio')]

    if db(db.Division.id > 0).count() == 0:
        db.Division.insert(
            first_name='Ciencias Físicas y Matemáticas'
        )
        db.Division.insert(
            first_name='Ciencias Biológicas'
        )
        db.Division.insert(
            first_name='Ciencias Sociales y Humanidades'
        )
        db.Division.insert(
            first_name='Externo a la USB'
        )
        db.Division.insert(
            first_name='Ciencias y Tecnologías Administrativas e Industriales'
        )
        db.commit()
