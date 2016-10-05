# -*- coding: utf-8 -*-
from gluon import *
def Tipo_Documento(db,T):
    db.define_table('Tipo_Documento',
        Field('nombre','string',
               label = 'Nombre'),
        format='%(nombre)s'
    )
