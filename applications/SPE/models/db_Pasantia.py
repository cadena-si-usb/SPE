# -*- coding: utf-8 -*-

################################################################################
#                         INICIO DECLARACION BASE DE DATOS                     #
################################################################################

#------------------------------------------------------------------------------#
#                            MODULO DE INVENTARIO                              #
#------------------------------------------------------------------------------#

db.define_table('Pasantia',
    Field('nombre'),
    Field('id_estudiante'),
    Field('empresa'),
    Field('tutor_academico'),
    Field('tutor_industrial'),
    Field('plan_trabajo'),
    Field('materia',db.Materia,
        requires=IS_IN_DB(db, db.Materia, '%(codigo)s',
        error_message='Elija una de las materias.'),
        label='Materia (*)')
   )

#------------------------------------------------------------------------------#

################################################################################
#                          FIN DECLARACION BASE DE DATOS                       #
################################################################################
