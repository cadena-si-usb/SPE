# -*- coding: utf-8 -*-

db.define_table('Pasantia',
    Field('titulo',
           requires=[IS_NOT_EMPTY
                        (error_message='Es necesario un Titulo.')],
           label='Titulo'),
    Field('estudiante','reference Estudiante',
          requires=IS_IN_DB(db, db.Estudiante,
          error_message='Elija uno de los estudiantes.'),
          label='Estudiante (*)'),
    Field('tutor_academico', 'reference Profesor',
          label='Tutor Academico'),
    Field('Tutor_Industrial', 'reference Tutor_Industrial',
          label='Tutor Industrial'),
    Field('periodo',
           label ='Periodo'),
    Field('area_proyecto','string',
          requires=[IS_NOT_EMPTY
                        (error_message='Adicione Area del Proyecto.')],
          label = 'Area del Proyecto'),
    Field('resumen_proyecto','text',
          requires=[IS_NOT_EMPTY
                        (error_message='Coloque resumen del proyecto ')],
          label ='Resumen del Proyecto'),
    Field('materia','reference Materia',
          requires=IS_IN_DB(db, db.Materia, '%(codigo)s',
          error_message='Elija una de las materias.'),
          label='Materia (*)'),
    Field('objetivo',
          requires=[IS_NOT_EMPTY
                (error_message='Adicione Area del Proyecto.')],
          label ='Objetivo General'),
    Field('confidencialidad',
          requires=[IS_NOT_EMPTY
                        (error_message='Adicione Area del Proyecto.')],
          label ='Detalles de Confidencialidad'),
    Field('status','string',
          label='Estado De Pasantia'),
    Field('etapa','reference Etapa',
          requires=IS_IN_DB(db, db.Etapa, '%(nombre)s',
          error_message='Elija una de las Etapas.'),
          label='Etapa (*)')
)
