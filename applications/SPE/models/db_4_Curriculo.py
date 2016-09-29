# -*- coding: utf-8 -*-


db.define_table('Curriculo',
    Field('estudiante','reference Estudiante',label='Estudiante (*)'),
    Field('electivas','string'),
    Field('cursos','string'),
    Field('aficiones','string'),
    Field('idiomas','string'),
    Field('activo','boolean')
   )

