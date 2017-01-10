# -*- coding: utf-8 -*-
from gluon import *
def Curriculo_Table(db,T):
    db.define_table('Curriculo',
        Field('estudiante','reference Estudiante',label='Estudiante (*)'),
        Field('electivas','list:string'),
        Field('cursos','list:string'),
        Field('aficiones','list:string'),
        Field('idiomas','list:string'),
        Field('activo','list:string')
       )

