# -*- coding: utf-8 -*-
from gluon import *
def correo_por_verificar_Table(db,T):
    db.define_table('correo_por_verificar',
                       Field('correo','string',required=True,ondelete='CASCADE',
                             notnull=True, label='Correo'),
                       Field('codigo','string',required=True,ondelete='CASCADE',
                             notnull=True, label='Codigo'),format='%(correo)s - %(codigo)s')

    db.correo_por_verificar.correo.requires=[IS_EMAIL(error_message=T('Este no es un correo valido'))]
