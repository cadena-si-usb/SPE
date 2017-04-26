# -*- coding: utf-8 -*-

################################################################################
#                         INICIO DECLARACION BASE DE DATOS                     #
################################################################################

#------------------------------------------------------------------------------#
#                            MODULO DE INVENTARIO                              #
#------------------------------------------------------------------------------#
from gluon import *

def Accion_Table(db,T):

    db.define_table('Accion',
        Field('nombre', ),
        Field('destino', unique=True),
        format='%(nombre)s - %(destino)s'
       )

    if db(db.Accion.id > 0).count() == 0:

        # 1
        db.Accion.insert(
            nombre='Acciones',
            destino='/SPE/acciones_usuario/listar',
        )
        # 2
        db.Accion.insert(
            nombre='Personal Administrativo',
            destino='/SPE/administrativos/listar',
        )
        # 3
        db.Accion.insert(
            nombre='Tutores Industriales',
            destino='/SPE/tutores_industriales/listar',
        )
        # 4
        db.Accion.insert(
            nombre='Usuarios',
            destino='/SPE/usuarios/listar',
        )
        # 5
        db.Accion.insert(
            nombre='Estudiantes',
            destino='/SPE/estudiantes/listar',
        )
        # 6
        db.Accion.insert(
            nombre='Profesores',
            destino='/SPE/profesores/listar',
        )
        # 7
        db.Accion.insert(
            nombre='Roles',
            destino='/SPE/roles/listar',
        )
        # 8
        db.Accion.insert(
            nombre='Asignar Roles',
            destino='/SPE/membresias/listar',
        )
        # 9
        db.Accion.insert(
            nombre='Configurar Accesos',
            destino='/SPE/accesos_etapa/listar',
        )
        # 10
        db.Accion.insert(
            nombre='Coordinadores',
            destino='/SPE/coordinadores/listar',
        )
        # 11
        db.Accion.insert(
            nombre='Curriculos',
            destino='/SPE/curriculos/listar',
        )
        # 12
        db.Accion.insert(
            nombre='Empresas',
            destino='/SPE/empresas/listar',
        )
        # 13
        db.Accion.insert(
            nombre='Preinscripciones',
            destino='/SPE/preinscripciones/listar',
        )
        # 14
        db.Accion.insert(
            nombre='Colocaciones',
            destino='/SPE/colocaciones/listar',
        )
        # 15
        db.Accion.insert(
            nombre='Inscripciones',
            destino='/SPE/inscripciones/listar',
        )
        # 16
        db.Accion.insert(
            nombre='Planes De Trabajo',
            destino='/SPE/planes_trabajo/listar',
        )
        # 17
        db.Accion.insert(
            nombre='Pasantias',
            destino='/SPE/pasantias/listar',
        )
        # 18
        db.Accion.insert(
            nombre='Ejecuciones',
            destino='/SPE/ejecuciones/listar',
        )
        # 19
        db.Accion.insert(
            nombre='Permisos',
            destino='/SPE/permisos/listar',
        )
        # 20
        db.Accion.insert(
            nombre='Retiros',
            destino='/SPE/retiros/listar',
        )
        # 21
        db.Accion.insert(
            nombre='Periodos',
            destino='/SPE/periodos/listar',
        )
        # 22
        db.Accion.insert(
            nombre='Paises',
            destino='/SPE/paises/listar',
        )
        # 23
        db.Accion.insert(
            nombre='Areas Laborales',
            destino='/SPE/areas_laborales/listar',
        )
        # 24
        db.Accion.insert(
            nombre='Universidades',
            destino='/SPE/universidades/listar',
        )
        # 25
        db.Accion.insert(
            nombre='Areas De Proyecto',
            destino='/SPE/areas_proyecto/listar',
        )
        # 26
        db.Accion.insert(
            nombre='Carreras',
            destino='/SPE/carreras/listar',
        )
        # 27
        db.Accion.insert(
            nombre='Etapas',
            destino='/SPE/etapas/listar',
        )
        # 28
        db.Accion.insert(
            nombre='Tipos De Documentos',
            destino='/SPE/tipos_documento/listar',
        )
        # 29
        db.Accion.insert(
            nombre='Categorias',
            destino='/SPE/categorias/listar',
        )
        # 30
        db.Accion.insert(
            nombre='Sedes',
            destino='/SPE/sedes/listar',
        )
        # 31
        db.Accion.insert(
            nombre='Dedicaciones',
            destino='/SPE/dedicaciones/listar',
        )
        # 32
        db.Accion.insert(
            nombre='Departamentos',
            destino='/SPE/departamentos/listar',
        )
        # 33
        db.Accion.insert(
            nombre='Divisiones',
            destino='/SPE/divisiones/listar',
        )
        # 34
        db.Accion.insert(
            nombre='Materias',
            destino='/SPE/materias/listar',
        )
        # 35
        db.Accion.insert(
            nombre='coordinaciones',
            destino='/SPE/coordinaciones/listar',
        )
        # 36
        db.Accion.insert(
            nombre='Estados',
            destino='/SPE/estados/listar',
        )
        # 37
        db.Accion.insert(
            nombre='Materias Periodo',
            destino='/SPE/materias_periodo/listar',
        )
        # 38
        db.Accion.insert(
            nombre='Editar Perfil',
            destino='/SPE/mi_perfil/configuracion',
        )
        # 39
        db.Accion.insert(
            nombre='Mis Pasantias',
            destino='/SPE/mis_pasantias/consultar_pasantias_estudiante',
        )
        # 40
        db.Accion.insert(
            nombre='Mis Pasantias',
            # destino='/SPE/Coordinador/consultarPasantias',
            destino='/SPE/mis_pasantias/consultar_pasantias_coordinador',
        )
        # 41
        db.Accion.insert(
            nombre='Editar Curriculo',
            destino='/SPE/mi_perfil/editar_curriculo',
        )
        # 42
        db.Accion.insert(
            nombre='Mis Permisos',
            destino='/SPE/mis_permisos/listar',
        )
        # 43
        db.Accion.insert(
            nombre='Mi Perfil',
            destino='/SPE/mi_perfil/ver',
        )
        # 44
        db.Accion.insert(
            nombre='Mi Currículo',
            destino='/SPE/mi_perfil/ver_curriculo',
        )
        # 45
        db.Accion.insert(
            nombre='Solicitudes de modificación',
            destino='/SPE/solicitud_modificacion/listar',
        )
        # 46
        db.Accion.insert(
            nombre='Mis solicitudes de modificación',
            destino='/SPE/mis_solicitudes_modificacion/consultar_solicitudes_modificacion_profesor',
        )
        # 47
        db.Accion.insert(
            nombre='Mis solicitudes de modificación',
            destino='/SPE/mis_solicitudes_modificacion/consultar_solicitudes_modificacion_coordinador',
        )





#------------------------------------------------------------------------------#

################################################################################
#                          FIN DECLARACION BASE DE DATOS                       #
################################################################################
