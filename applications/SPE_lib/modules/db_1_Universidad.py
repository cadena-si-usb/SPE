# -*- coding: utf-8 -*-
from gluon import *
def Universidad_Table(db,T):
    db.define_table('Universidad',
                    Field('nombre','string',required=True,ondelete='CASCADE',
                        notnull=True, label='Universidad'),
                    Field('id_pais','reference Pais', required=True, notnull=True,label=T('Pais')),
                    format='%(nombre)s')

    db.Universidad.nombre.requires=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
    db.Universidad.nombre.requires+=[IS_LENGTH(512)]
    db.Universidad.nombre.requires+=[IS_NOT_IN_DB(db, 'Universidad.nombre',error_message=T('Universidad ya registrada'))]
