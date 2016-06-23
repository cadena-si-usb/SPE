# -*- coding: utf-8 -*-


db.define_table('Curriculo',
    Field('estudiante','reference Estudiante',requires=IS_IN_DB(db, db.Estudiante, '%(carnet)s',error_message='Elija uno de los estudiantes.'),label='Estudiante (*)'),
    Field('electivas','string'),
    Field('cursos','string'),
    Field('aficiones','string'),
    Field('idiomas','string'),
    Field('activo','boolean')
   )

