db.define_table('Profesor',
    Field('categoria','reference Categoria',
          label='Categoria'),
    Field('dedicacion','reference Dedicacion',
          label='Dedicacion'),
    Field('departamento','reference Departamento',
          label='Departamento')
)