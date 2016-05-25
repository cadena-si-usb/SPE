db.define_table('Estudiante',
    Field('carnet',
          requires=IS_MATCH('^\d{2}?[\s.-]?\d{5}$',
                        error_message='Introduzca un carnet valido.'),
          label='Carnet'),
    Field('carrera', ##referencia a tabla Carrera
          label='Carrera')
)