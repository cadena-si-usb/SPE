# -*- coding: utf-8 -*-

################################################################################
#                         INICIO DECLARACION BASE DE DATOS                     #
################################################################################

#------------------------------------------------------------------------------#
#                            MODULO DE INVENTARIO                              #
#------------------------------------------------------------------------------#

db.define_table('Usuario',
    Field('nombre','string',
          requires=[IS_NOT_EMPTY(error_message='Es necesario un nombre.') ],
          label = 'Nombre (*)'),
    Field('cedula', 
          requires=[IS_MATCH('^[0-9][0-9]*$',
                        error_message='Introduzca una cedula.'),
                    IS_NOT_IN_DB(db, 'Empleado.cedula',
                        error_message='Cedula ya almacenada o no introducida.')], 
          label='Cedula (*)' ),
    Field('correo',
          requires=IS_EMPTY_OR(IS_EMAIL(error_message='Introduzca un email valido.')),
          comment='nombre@mail.com',
          label = 'Email(*)'),
    Field('telefono_hab',
          requires=IS_MATCH('^\d{4}?[\s.-]?\d{7}$', error_message='Numero no valido,ingrese numero telefonico'),
          comment='0212-111111',
          label = 'Telefono Habitacion (*)'),
    
    Field('telefono_cel',
          requires=IS_MATCH('^\d{4}?[\s.-]?\d{7}$', error_message='Numero no valido, recuerde colocar codigo de area'),
          comment = '0416-11111',
          label = 'Telefono Celular (*)'),
          
    Field('direcUsuario','text',
          label = 'Direccion'),
    Field('sexo',
          requires=IS_IN_SET(['M','F']),
          label = 'Sexo (*)')
)
