db.define_table('Materia_Periodo',
    Field('materia','reference Materia',
          requires=IS_IN_DB(db, db.Materia,
          error_message='Elija uno de los materias.'),
          label='Materia (*)'),
    Field('periodo','reference Periodo',
          requires=IS_IN_DB(db, db.Periodo,
          error_message='Elija uno de los Periodos.'),
          label='Periodo (*)')
)

