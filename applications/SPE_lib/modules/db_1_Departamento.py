# -*- coding: utf-8 -*-
from gluon import *
def Departamento_Table(db,T):
    # Departamento
    db.define_table('Departamento',
                    Field('first_name','string', requires=IS_NOT_EMPTY(), default='', label="Nombre del Departamento"),
                    Field('id_division','reference Division', notnull=True, label='Nombre de División'),
                    Field('email_dep','string',label='Correo Electrónico del Departamento'),
                    Field('sede','reference Sede'))


    # Validadores
    db.Departamento.email_dep.requires=[IS_EMAIL(error_message=T('Este no es un email valido'))]
    db.Departamento.email_dep.requires+=[IS_LENGTH(100)]
    db.Departamento.email_dep.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
