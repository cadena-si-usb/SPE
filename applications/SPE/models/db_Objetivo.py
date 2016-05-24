db.define_table('Objetivo',
    Field('descripcion','text',
          label= 'Descripcion'),
    Field('actividad',##referencia 1 a muchos tabla Actividad
          label='Actividades')
)