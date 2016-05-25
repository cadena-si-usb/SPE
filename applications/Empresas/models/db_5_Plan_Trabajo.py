# -*- coding: utf-8 -*-


db.define_table('PlanTrabajo',
    Field('pasantia','reference Pasantia',
          label='Estudiante' ), 
    Field('tutor_academico','reference Profesor',
          label = 'Tutor Academico'),
    Field('tutor_industrial','reference Tutor_Industrial',
          label = 'Tutor Industrial'),
    Field('objetivo_general','String',
          label='Obejtivos Especificos')
)