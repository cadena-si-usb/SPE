db.define_table('UsuarioExterno', 
                Field('nombre',
                       requires=[IS_NOT_EMPTY
                                    (error_message='Es necesario un nombre.') ],
                       label='Nombre'),
                Field('correo',
                       requires=[IS_EMPTY_OR(IS_EMAIL
                                            (error_message='Introduzca un email valido.'))],
                       label= 'Correo'),
                Field('clave', 'password',
                       requires=[IS_NOT_EMPTY
                                    (error_message='Es,necesario una contraseña.'),
                                 IS_STRONG(min=10, special=1, upper=1)],
                       label = 'Clave '
                     ),
                Field('tipo_documento',
                      requires=IS_IN_SET(['CI', 'Pasaporte']),
                      label='Tipo de Documento (*)'),
                Field('numero_documento',
                      requires=[IS_MATCH('^[0-9][0-9]*$',
                                         error_message='Introduzca una cedula.'),
                                IS_NOT_IN_DB(db, 'Empleado.cedula',
                                             error_message='Cedula ya almacenada o no introducida.')],
                      label='Numero Documentacion (*)'),
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
                       requires=IS_MATCH('^\d{4}?[\s.-]?\d{7}$',                  error_message='Numero no valido,ingrese numero telefonico'),
                       label = 'Telefono'),
                Field('direccion','text',
                       requires=[IS_NOT_EMPTY
                                    (error_message='Direccion necesaria')],
                       label='Direccion')
)