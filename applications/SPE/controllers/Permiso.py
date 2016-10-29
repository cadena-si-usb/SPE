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


# Pulir permisologia y agregar verDetallePermiso
@auth.requires(auth.is_logged_in() and not (auth.has_membership(role='Tutor Industrial')))
def consultarPermisos():
    userId=auth.user.id
    currentRoles = auth.user_groups.values()

    # Obtenemos todas las pasantias en los que este usuario interviene
    ''' Generar SQLFORM.grid con campos en selectable puestos en writable
        dependiendo del rol del actor, ademas de algun hover que despliegue
        el texto de la justificacion y que el nombre de la pasantía sea un link
        a ver en detalle esa pasantia. Cambiar aprobaciones a booleanos en el modelo
    '''

    if 'Profesor' in currentRoles:
        tutor_academico = db.Profesor(id=userId).usuario
        permisos = db((db.Pasantia.tutor_academico == tutor_academico) & (db.Permiso.pasantia == db.Pasantia.id))
    elif 'Estudiante' in currentRoles:
        estudiante = db.Estudiante(id=userId).usuario
        permisos = db((db.Pasantia.estudiante == estudiante) & (db.Permiso.pasantia == db.Pasantia.id))
    elif ('CoordinadorCCT' in currentRoles) or ('Administrativo' in currentRoles):
        permisos = db((db.Permiso.pasantia == db.Pasantia.id))
    

    ''' Hacer caso de la coordinacion, determinar de que carrera es la coordinacion
        y luego buscar todas las pasantias inscritas por estudiantes de esa carrera 
    elif 'Coordinador' in currentRoles:
    '''

    # Colocar solicitante tambien en la tablita
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
    #checkboxes = 
    form = SQLFORM.grid(query=permisos, fields=fields, headers=headers, orderby=default_sort_order,create=False, deletable=False, editable=False, maxtextlength=64, paginate=25,details=False,csv=False,user_signature=False,links=links)
        
    response.view = 'Permiso/Consultar_Permisos.html'
    return locals()


    