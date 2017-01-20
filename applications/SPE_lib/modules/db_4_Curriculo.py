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

    if db(db.Curriculo.id > 0).count() == 0:
        db.Curriculo.insert(
            estudiante='4',
            electivas=['Diseño De Piezas'],
            cursos = ['Matlab II'],
            aficiones=['Fifa 2016'],
            idiomas=['Español', 'Ingles'],
            activo=True
        )
        db.Curriculo.insert(
            estudiante='7',
            electivas=['Sistemas De Informacion II', 'Sistemas De Informacion III','Base De Datos II',
                       'Modelos Lineales II'],
            cursos = ['Codeacademy'],
            aficiones=['Musica'],
            idiomas=['Español', 'Ingles','Portugues'],
            activo=True
        )
        db.commit()


