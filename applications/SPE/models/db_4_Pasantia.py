# -*- coding: utf-8 -*-

db.define_table('Pasantia',
    Field('titulo',
           requires=[IS_NOT_EMPTY
                        (error_message='Es necesario un Titutlo.')],
           label='Titulo'),
    Field('estudiante', 'reference Estudiante',
          label='Estudiante'),
    Field('tutor_academico', 'reference Profesor',
          label='Tutor Academico'),
    Field('Tutor_Industrial', 'reference Tutor_Industrial',
          label='Tutor Industrial'),
    Field('periodo',##referencia a tabla Periodo
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
          label ='Materia'),
    Field('obejtivo',
          requires=[IS_NOT_EMPTY
                (error_message='Adicione Area del Proyecto.')],
          label ='Objetivo General'),
    Field('confidencialidad',
          requires=[IS_NOT_EMPTY
                        (error_message='Adicione Area del Proyecto.')],
          label ='Detalles de Confidencialidad'),
    Field('status','string',
          label='Estado De Pasantia'),
    Field('etapa', 'string',
          label='Estado De Pasantia'),
)
