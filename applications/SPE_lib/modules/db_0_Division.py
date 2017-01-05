# -*- coding: utf-8 -*-
from gluon import *
# Division
def Division_Table(db,T):
    db.define_table('Division',
                    Field('first_name','string',required=True),
                    format='%(first_name)s'
                   )

    db.Division.first_name.requires+=[IS_LENGTH(100)]
    db.Division.first_name.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
