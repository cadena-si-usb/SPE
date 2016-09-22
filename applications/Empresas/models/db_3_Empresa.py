db.define_table('Empresa',
    Field('usuario', 'reference UsuarioExterno',
          requires=[IS_NOT_EMPTY(error_message='Es necesario un email.'),IS_EMAIL
                               (error_message='Introduzca un email valido.') ],
          label='Email(*)'),
    Field('area_laboral','reference Area_Laboral',
          label = 'Area Laboral'),
    Field('descripcion',
          label='Descripcion'),
    Field('direccion_web',##verificador de urls
          label = 'Pagina Web'),
    Field('contacto_RRHH',
          label='Contactos De Recursos Humanos',requires=[IS_NOT_EMPTY(error_message='Es necesario un email.'),IS_EMAIL
                               (error_message='Introduzca un email valido.')]),
    format=lambda r: '%s %s' % (r.usuario.nombre, r.usuario.correo)

)

db.Empresa.area_laboral.requires=IS_IN_DB(db,db.Area_Laboral.id,'%(nombre)s')
db.Empresa.usuario.requires=IS_IN_DB(db,db.UsuarioExterno.id,'%(nombre)s')