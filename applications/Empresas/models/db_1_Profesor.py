db.define_table('Profesor',
    Field('categoria',##referencia tabla categoria
          label='Categoria'),
    Field('dedicacion',##referencia a tabla Dedicacion
          label='Dedicacion'),
    Field('departamento', ##referencia a tabla Departamento
          label='Departamento')
)