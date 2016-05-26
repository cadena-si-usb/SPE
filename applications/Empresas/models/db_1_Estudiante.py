db.define_table('Estudiante',
    Field('usuario','reference UsuarioUSB',  ##referencia a tabla Carrera
          label='Carrera'),
    Field('carnet',
          requires=IS_MATCH('^\d{2}?[\s.-]?\d{5}$',
                        error_message='Introduzca un carnet valido.'),
          label='Carnet'),
    Field('carrera', 'reference Carrera',
          label='Carrera'),
    Field('correo_Alternativo',  requires=IS_EMAIL(error_message='Introduzca un email valido.'),
          label='Correo Alternativo'),
    format=lambda r: '%s %s' % (r.usuario.usbid, r.usuario.nombre)
)