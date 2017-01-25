# -*- coding: utf-8 -*-
from gluon import *


def Curriculo_Table(db, T):
    db.define_table('Curriculo',
                    Field('estudiante', 'reference Estudiante', label='Estudiante (*)', unique=True),
                    Field('electivas', 'list:string',label='Electivas', default=[]),
                    Field('cursos', 'list:string',label='Cursos', default=[]),
                    Field('aficiones', 'list:string',label='Aficciones', default=[]),
                    Field('idiomas', 'list:string',label='Idiomas', default=[]),
                    Field('voluntariados', 'list:string',label='Voluntariados', default=[]),
                    Field('educacion', 'list:string',label='Educacion', default=[]),
                    Field('experiencias', 'list:string',label='Experiencias', default=[]),
                    Field('proyectos', 'list:string', label='Proyectos', default=[]),
                    Field('activo', 'list:string', default=[])
                    )

    if db(db.Curriculo.id > 0).count() == 0:
        db.Curriculo.insert(
            estudiante='1',
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
            estudiante='2',
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
