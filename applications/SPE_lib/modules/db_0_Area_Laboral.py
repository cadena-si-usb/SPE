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

    if db(db.Area_Laboral.id > 0).count() == 0:
        db.Area_Laboral.insert(
            first_name='Tecnologia',
            descripcion='tecnológica'
        )
        db.Area_Laboral.insert(
            first_name='Informatica',
            descripcion='Consultoria, desarrollo de software,etc'
        )
        db.Area_Laboral.insert(
            first_name='Legal',
            descripcion='Asesoria legal, resolucion de casos'
        )
        db.Area_Laboral.insert(
            first_name='Electricidad',
            descripcion='Instalaciones electricas'
        )
        db.Area_Laboral.insert(
            first_name='Arquitectura',
            descripcion='Diseño de planos'
        )
        db.commit()