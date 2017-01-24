# -*- coding: utf-8 -*-
from gluon import *


def Curriculo_Table(db, T):
    db.define_table('Curriculo',
                    Field('estudiante', 'reference Estudiante', label='Estudiante (*)'),
                    Field('electivas', 'list:string',label='Electivas'),
                    Field('cursos', 'list:string',label='Cursos'),
                    Field('aficiones', 'list:string',label='Aficciones'),
                    Field('idiomas', 'list:string',label='Idiomas'),
                    Field('voluntariados', 'list:string',label='Voluntariados'),
                    Field('educacion', 'list:string',label='Educacion'),
                    Field('experiencias', 'list:string',label='Experiencias'),
                    Field('proyectos', 'list:string', label='Proyectos'),
                    Field('activo', 'list:string')
                    )

    if db(db.Curriculo.id > 0).count() == 0:
        db.Curriculo.insert(
            estudiante='4',
            electivas=['Diseño De Piezas'],
            cursos=['Matlab II'],
            aficiones=['Fifa 2016'],
            idiomas=['Español', 'Ingles'],
            voluntariados=['Videojuego Educativo "Borrados"'],
            educacion=['Liceo Los Arcos'],
            experiencias=['Desarrollador En Integra Consultores por 17 meses'],
            proyectos=['Proyecto Dime'],
            activo=True
        )
        db.Curriculo.insert(
            estudiante='7',
            electivas=['Sistemas De Informacion II', 'Sistemas De Informacion III', 'Base De Datos II',
                       'Modelos Lineales II'],
            cursos=['Codeacademy'],
            aficiones=['Musica'],
            idiomas=['Español', 'Ingles', 'Portugues'],
            voluntariados=['Videojuego Educativo "Borrados"'],
            educacion=['Liceo Los Arcos'],
            experiencias=['Desarrollador En Integra Consultores por 17 meses'],
            proyectos=['Proyecto Dime'],
            activo=True
        )
        db.commit()
