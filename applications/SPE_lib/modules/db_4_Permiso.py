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
        Field('Estudiante', 'reference Estudiante', label='Estudiante (*)',writable=False),
        Field('Tipo',requires=IS_IN_SET(['Inscripcion Extemporanea','Retiro Extemporaneo','Evaluacion Extemporanea'])),
        Field('pasantia','reference Pasantia', label='Pasantia (*)',writable=False),
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
        Field('justificacion', 'text', label='Justificacion del permiso'),
        Field('calendario_compromisos', 'string', label='Calendario de compromisos')
        #Field('calendario_compromisos', 'reference Calendario')
    )

#------------------------------------------------------------------------------#

################################################################################
#                          FIN DECLARACION BASE DE DATOS                       #
################################################################################
