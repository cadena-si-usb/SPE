# -*- coding: utf-8 -*-
from gluon import *
def Tipo_Documento_Table(db,T):
    db.define_table('Tipo_Documento',
        Field('first_name','string',
               label = 'Nombre'),
        format='%(first_name)s'
    )
