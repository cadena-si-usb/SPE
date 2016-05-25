db.define_table('Empresa',
    Field('correo', 'reference UsuarioExterno',
          requires=[IS_NOT_EMPTY(error_message='Es necesario un email.'),IS_EMAIL
                               (error_message='Introduzca un email valido.') ],
          label='Email(*)'),
    Field('nombre','string',
          requires=[IS_NOT_EMPTY(error_message='Es necesario un nombre.') ],
          label = 'Nombre (*)',
          comment='nombre@mail.com',
          ),
    Field('area_laboral','reference Area_Laboral',
          label = 'Area Laboral'),    
    Field('direccion_web',##verificador de urls
          label = 'Pagina Web')
)

