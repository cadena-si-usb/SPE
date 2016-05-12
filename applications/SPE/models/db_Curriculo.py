# -*- coding: utf-8 -*-

################################################################################
#                         INICIO DECLARACION BASE DE DATOS                     #
################################################################################

#------------------------------------------------------------------------------#
#                            MODULO DE INVENTARIO                              #
#------------------------------------------------------------------------------#

db.define_table('Curriculo',
    Field('nombre', unique=True,
          requires=[IS_NOT_EMPTY(error_message='Introduzca un nombre.'),
                    IS_NOT_IN_DB(db, 'Usuario.nombre', error_message='Nombre ya\
                    esta almacenado, introduzca otro o modifique el anterior.'),
                    IS_UPPER()], label='Nombre (*)' )
   )

#------------------------------------------------------------------------------#

################################################################################
#                          FIN DECLARACION BASE DE DATOS                       #
################################################################################
