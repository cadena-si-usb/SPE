db.define_table('Materia_Periodo',
    Field('materia','reference Materia',
          label='Materia (*)'),
    Field('periodo','reference Periodo',
          label='Periodo (*)')
)

