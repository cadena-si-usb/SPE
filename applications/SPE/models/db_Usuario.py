# -*- coding: utf-8 -*-

################################################################################
#                         INICIO DECLARACION BASE DE DATOS                     #
################################################################################

#------------------------------------------------------------------------------#
#                            MODULO DE INVENTARIO                              #
#------------------------------------------------------------------------------#

db.define_table('Usuario',
    Field('id', unique=True,
          requires=[IS_NOT_EMPTY(error_message='Introduzca un nombre.'),
                    IS_NOT_IN_DB(db, 'Usuario.id', error_message='ID ya\
                    esta almacenado, introduzca otro o modifique el anterior.'),
                    IS_UPPER()], label='ID (*)' ),
    Field('nombre'),
    Field('apellido'),
    Field('ci')
   )

#------------------------------------------------------------------------------#

################################################################################
#                          FIN DECLARACION BASE DE DATOS                       #
################################################################################
