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

    if db(db.Materia.id > 0).count() == 0:
        db.Materia.insert(
            codigo='EP3420',
            sede='1',
            tipo='Larga',
            descripcion='Lograr que el estudiante se integre a las actividades de la empresa o institución y actúe dentro de la misma como un recurso capaz de intervenir en el desarrollo completo de trabajos, tareas o proyectos a nivel profesional, utilizando para ello los conocimientos y la formación de que dispone.',
            duracion='20'
        )
        db.Materia.insert(
            codigo='EP1420',
            sede='1',
            tipo='Corta',
            descripcion='En las primeras cuatro semanas (semana 1 a semana 4) de cada trimestre académico se llevará a cabo el Proceso de Preinscripción de la Pasantía . Los estudiantes que desean optar a una pasantía deben preinscribirse al trimestre anterior al período de la pasantía a cursar. La preinscripción tendrá carácter obligatorio y el estudiante deberá consignar ante la CCTDS, o ante la CCCE según sea el caso, específicamente al personal de Atención al Estudiante, los siguientes recaudos:',
            duracion='6'
        )
        db.commit()

#------------------------------------------------------------------------------#

################################################################################
#                          FIN DECLARACION BASE DE DATOS                       #
################################################################################
