# -*- coding: utf-8 -*-

# Proceso de registro en el cual un tutor solicita un registro a una Empresa
from shlex import shlex

# Completar
@auth.requires(auth.is_logged_in() and not (auth.has_membership(role='Tutor Industrial')))
def verDetallePermiso():
    # Buscamos los datos necesarios
    permisoId = request.args[0]
    permiso = db(db.Permiso.id == permisoId).select().first()

    # Definimos que no se pueden editar los datos
    for field in db.Permiso:
        field.writable=False

    # Llenamos Los Campos con los datos encontrados
    db.Permiso.Tipo.default = permiso.Tipo
    db.Permiso.pasantia.default = permiso.pasantia
    db.Permiso.aprobacion_coordinacion.default = permiso.aprobacion_coordinacion
    db.Permiso.aprobacion_tutor_academico.default = permiso.aprobacion_tutor_academico
    db.Permiso.estado.default = permiso.estado
    db.Permiso.justificacion.default = permiso.justificacion

    formPermiso = SQLFORM.factory(db.Permiso, fields=None, showid=False)
    response.view = 'Permiso/Detalle_Permiso.html'
    return locals()


def generarLinks(row):
    return A('Detalle', _href=URL(c='Permiso',f='verDetallePermiso',args=[row.Permiso.id]))


@auth.requires(auth.is_logged_in() and not (auth.has_membership(role='Tutor Industrial')))
def consultarPermisos():
    userId=auth.user.id
    currentRoles = auth.user_groups.values()

    fields = (db.Permiso._id,db.Permiso.Tipo, db.Permiso.aprobacion_coordinacion, db.Permiso.aprobacion_tutor_academico, db.Permiso.pasantia, db.Permiso.estado, db.Permiso.justificacion)    
    headers = {
        ''
        'Permiso.Tipo': 'Tipo',
        'Permiso.pasantia.Nombre': 'Pasantía',
        'Permiso.aprobacion_coordinacion': 'Aprobación de Coordinación',
        'Permiso.aprobacion_tutor_academico': 'Aprobación de Tutor Académico'
    }
    default_sort_order=[db.Permiso.Tipo]
    links = [lambda row: generarLinks(row)]

    # Obtenemos todas las pasantias en los que este usuario interviene
    if 'Profesor' in currentRoles:
        tutor_academico = db.Profesor(id=userId).usuario
        permisos = db((db.Pasantia.tutor_academico == tutor_academico) & (db.Permiso.pasantia == db.Pasantia.id))
        form = SQLFORM.grid(query=permisos, fields=fields, headers=headers, orderby=default_sort_order,create=False, deletable=False, editable=False, maxtextlength=64, paginate=25,details=False,csv=False,user_signature=False,links=links)

    elif 'Estudiante' in currentRoles:
        estudiante = db.Estudiante(id=userId).usuario
        permisos = db((db.Pasantia.estudiante == estudiante) & (db.Permiso.pasantia == db.Pasantia.id))
        form = SQLFORM.grid(query=permisos, fields=fields, headers=headers, orderby=default_sort_order,create=False, deletable=False, editable=False, maxtextlength=64, paginate=25,details=False,csv=False,user_signature=False,links=links)

    elif ('CoordinadorCCT' in currentRoles) or ('Administrativo' in currentRoles):
        permisos = db((db.Permiso.pasantia == db.Pasantia.id))
        form = SQLFORM.grid(query=permisos, fields=fields, headers=headers, orderby=default_sort_order,create=False, deletable=False, editable=False, maxtextlength=64, paginate=25,details=False,csv=False,user_signature=False,links=links)

    elif 'Coordinador' in currentRoles:
        # Carrera de la coordinacion donde participa este coordinador
        idCoordinacion = db.Coordinador(id=userId).coordinacion
        carreraCoordinacion = db.Coordinacion(id=idCoordinacion).Carrera.select().first()
        
        # Estudiantes que cursan la carrera carreraCoordinacion
        queryEstudiantesCarrera = db((db.Estudiante.carrera == carreraCoordinacion)).select('id')
        estudiantes = [row.id for row in queryEstudiantesCarrera]
        
        # Permisos solicitados por estudiantes de la carrera carreraCoordinacion
        permisos = db(db.Permiso.Estudiante.belongs(estudiantes))
        ''' Deuda tecnica:
            Resolver el error que da links en este formulario, 
            por eso los separe asi, para poder mostrar funcionalidad 
            en la entrega del 100% 
        '''  
        form = SQLFORM.grid(query=permisos, fields=fields, headers=headers, orderby=default_sort_order,create=False, deletable=False, editable=False, maxtextlength=64, paginate=25,details=False,csv=False,user_signature=False)
    
        
    response.view = 'Permiso/Consultar_Permisos.html'
    return locals()


@auth.requires(auth.is_logged_in() and not (auth.has_membership(role='Tutor Industrial')))
def aprobarPermiso():
    currentRoles = auth.user_groups.values()    
    permiso = db.Permiso(id=request.args[0])

    if 'Profesor' in currentRoles:
        permiso.update_record(aprobacion_tutor_academico="Aprobado")
        redirect(URL(c='Pasantia',f='/SPE/Permiso/consultarPermisos'))
    elif ('CoordinadorCCT' in currentRoles) or ('Administrativo' in currentRoles):
        permiso.update_record(estado="Aprobado")

    elif 'Coordinador' in currentRoles:
        permiso.update_record(aprobacion_coordinacion="Aprobado")
        redirect(URL(c='Pasantia',f='/SPE/Permiso/consultarPermisos'))
    #

    redirect(URL(c='Pasantia',f='verPlanDeTrabajo', args=[request.args[0]]))