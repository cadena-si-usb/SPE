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
        Field('Estudiante', 'reference UsuarioUSB', label='Estudiante (*)'),
        Field('Tipo',requires=IS_IN_SET(['Inscripcion Extemporanea','Retiro Extemporaneo'])),
        Field('pasantia','reference Pasantia', label='Pasantia (*)'),
        Field('estado', 'string', default="En Espera",
              requires=IS_IN_SET(['En espera', 'Aprobado'], zero=None,
                                 error_message='Opcion Invalida')),
        Field('aprobacion_tutor_academico', 'string',
              requires=IS_IN_SET(['En espera', 'Aprobado'],zero=None,
                                error_message='Opcion Invalida'),
              default='En espera', label='Aprobacion Del Tutor Academico',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('aprobacion_coordinacion', 'string',
              requires=IS_IN_SET(['En espera', 'Aprobado'], zero=None,
                                error_message='Opcion Invalida'),
              default='En espera', label='Aprobacion De La Coordinacion',
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('justificacion', 'string', label='Justificacion del permiso')
        #Field('calendario_compromisos', 'reference Calendario')
    )

#------------------------------------------------------------------------------#

################################################################################
#                          FIN DECLARACION BASE DE DATOS                       #
################################################################################
