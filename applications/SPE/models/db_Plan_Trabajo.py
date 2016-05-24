# -*- coding: utf-8 -*-


db.define_table('PlanTrabajo',
    Field('estudiante',##referencia a tabla Estudiante 
          label='Estudiante' ), 
    Field('tutor_academico',##referencia a tabla Profesor
          label = 'Tutor Academico'),
    Field('tutor_industrial',##refrencia a tabla Tutor Industrial
          label = 'Tutor Industrial'),
    Field('objetivo', ##referencia a tabla Objetivos
          label='Obejtivos Especificos')
)
