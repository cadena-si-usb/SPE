# -*- coding: utf-8 -*-
from gluon import *
################################################################################
#                         INICIO DECLARACION BASE DE DATOS                     #
################################################################################

#------------------------------------------------------------------------------#
#                            MODULO DE INVENTARIO                              #
#------------------------------------------------------------------------------#
def Permiso_Table(db,T):
    db.define_table('Permiso',
        Field('Tipo',requires=IS_IN_SET(['Inscripcion Extemporanea','Retiro'])),
        Field('pasantia','reference Pasantia'),
        Field('estado', 'string', default="En Espera",
              requires=IS_IN_SET(['En espera', 'Aprobado'], zero=None,
                                 error_message='Opcion Invalida'))
    )

#------------------------------------------------------------------------------#

################################################################################
#                          FIN DECLARACION BASE DE DATOS                       #
################################################################################
