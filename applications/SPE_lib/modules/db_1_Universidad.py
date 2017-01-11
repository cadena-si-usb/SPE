# -*- coding: utf-8 -*-
from gluon import *
def Universidad_Table(db,T):
    db.define_table('Universidad',
                    Field('first_name','string',required=True,ondelete='CASCADE',
                        notnull=True, label='Universidad'),
                    Field('id_pais','reference Pais', required=True, notnull=True,label=T('Pais')),
                    format='%(first_name)s')

    db.Universidad.first_name.requires=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
    db.Universidad.first_name.requires+=[IS_LENGTH(512)]
    db.Universidad.first_name.requires+=[IS_NOT_IN_DB(db, 'Universidad.first_name',error_message=T('Universidad ya registrada'))]

    if db(db.Universidad.id > 0).count() == 0:
        db.Universidad.insert(
            first_name='Universidad Simón Bolívar',
            id_pais=1
        )
        db.Universidad.insert(
            first_name='Universidad Católica Andrés Bello',
            id_pais=1
        )
        db.Universidad.insert(
            first_name='Universidad Metropolitana',
            id_pais=1
        )
        db.Universidad.insert(
            first_name='Universidad De Florida',
            id_pais=2
        )
        db.commit()
