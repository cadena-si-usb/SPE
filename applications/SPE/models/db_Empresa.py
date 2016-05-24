db.define_table('Empresa',
    Field('nombre','string',
          requires=[IS_NOT_EMPTY(error_message='Es necesario un nombre.') ],
          label = 'Nombre (*)'),
    Field('correo',
          requires=IS_EMPTY_OR(IS_EMAIL
                               (error_message='Introduzca un email valido.')),
          comment='nombre@mail.com',
          label = 'Email(*)'),
    Field('area_laboral',
          label = 'Area Laboral'),    
    Field('direccion_web',##verificador de urls
          label = 'Pagina Web')
)

