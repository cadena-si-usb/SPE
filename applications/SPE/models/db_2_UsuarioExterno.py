db.define_table('UsuarioExterno',
                Field('auth_User', 'reference auth_user'),
                Field('nombre',
                       requires=[IS_NOT_EMPTY
                                    (error_message='Es necesario un nombre.') ],
                       label='Nombre'),
                Field('correo',
                       requires=[IS_EMPTY_OR(IS_EMAIL
                                            (error_message='Introduzca un email valido.'))],
                       label='Correo'),
                Field('clave', 'password',
                       requires=[IS_NOT_EMPTY
                                    (error_message='Es,necesario una contraseña.'),
                                 IS_STRONG(min=10, special=1, upper=1)],
                       label = 'Clave '
                     ),
                Field('pregunta_secreta', 'text',
                       requires=[IS_NOT_EMPTY
                                    (error_message='Campo necesario')],
                       label='Pregunta Secreta'),
                Field('respuesta_secreta','string',
                       requires=[IS_NOT_EMPTY
                                    (error_message='Campo necesario')],
                       label='Respuesta Secreta'),
                Field('pais','reference Pais',
                       label= 'Pais'),
                Field('estado','reference Estado',
                       label= 'Estado'), 
                Field('telefono',
                       requires=IS_MATCH('^\d{4}?[\s.-]?\d{7}$',error_message='Numero no valido,ingrese numero telefonico'),
                       label = 'Telefono'),
                Field('direccion','text',
                       requires=[IS_NOT_EMPTY
                                    (error_message='Direccion necesaria')],
                       label='Direccion'),
                format='%(nombre)s - %(correo)s'
)


db.UsuarioExterno.correo.requires+=[IS_NOT_IN_DB(db, 'UsuarioExterno.correo',error_message=T('Correo No Disponible'))]