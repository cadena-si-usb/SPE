# -*- coding: utf-8 -*-
from gluon import *
################################################################################
#                         INICIO DECLARACION BASE DE DATOS                     #
################################################################################

#------------------------------------------------------------------------------#
#                            MODULO DE INVENTARIO                              #
#------------------------------------------------------------------------------#
def Materia_Table(db,T):
    db.define_table('Materia',
        Field('codigo'),
        Field('sede','reference Sede', label='Sede', notnull=True),
        Field('tipo',requires=IS_IN_SET(['Corta', 'Mediana', 'Larga'])),
        Field('descripcion'),
        Field('duracion','integer'),
        format='%(codigo)s - %(tipo)s'
       )

#------------------------------------------------------------------------------#

################################################################################
#                          FIN DECLARACION BASE DE DATOS                       #
################################################################################
