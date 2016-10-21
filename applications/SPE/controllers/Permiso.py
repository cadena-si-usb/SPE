# -*- coding: utf-8 -*-

# Proceso de registro en el cual un tutor solicita un registro a una Empresa
from shlex import shlex

# Completar
@auth.requires(auth.is_logged_in() and not (auth.has_membership(role='Tutor Industrial')))
def verDetallePermiso():
    permisoId = request.args[0]
    response.view = 'Permiso/Detalle_Permiso.html'
    return locals()


# Pulir permisologia y agregar verDetallePermiso
@auth.requires(auth.is_logged_in() and not (auth.has_membership(role='Tutor Industrial')))
def consultarPermisos():
    userId=auth.user.id
    currentRoles = auth.user_groups.values()
    permisos_pasantias = ""

    # Obtenemos todas las pasantias en los que este usuario interviene
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

    fields = (db.Permiso.Tipo, db.Permiso.aprobacion_coordinacion, db.Permiso.aprobacion_tutor_academico, db.Permiso.pasantia)    
    headers = {
        ''
        'Permiso.Tipo': 'Tipo',
        'Permiso.aprobacion_coordinacion': 'aprobacion_coordinacion',
        'Permiso.aprobacion_tutor_academico': 'aprobacion_tutor_academico',
        'Permiso.pasantia': 'pasantia'
    }
    default_sort_order=[db.Permiso.Tipo]
    links = [lambda row: A('Detalle', _href=URL(c='Permiso',f='verDetallePermiso',args=[row.id]))]
    form = SQLFORM.grid(query=permisos, fields=fields, headers=headers, orderby=default_sort_order,create=False, deletable=False, editable=False, maxtextlength=64, paginate=25,details=False,csv=False,user_signature=False)
    
    
    response.view = 'Permiso/Consultar_Permisos.html'
    return locals()