# -*- coding: utf-8 -*-
from gluon import *

def Area_Laboral_Table(db,T):
    db.define_table('Area_Laboral',
                    Field('first_name', 'string', required=True, ondelete='CASCADE',
                          notnull=True, label='Area Laboral'),
                    Field('descripcion', 'text', required=True, notnull=True, label=T('Descripcion del Area Laboral')),
                    format='%(first_name)s')

    db.Area_Laboral.first_name.requires=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
    db.Area_Laboral.first_name.requires+=[IS_LENGTH(512)]
    db.Area_Laboral.first_name.requires+=[IS_NOT_IN_DB(db, 'Area_Laboral.first_name',error_message=T('Area Laboral ya registrado'))]
