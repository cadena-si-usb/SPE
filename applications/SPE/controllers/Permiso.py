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

def generarLinksCoordinador(row):
    return A('Detalle', _href=URL(c='Permiso',f='verDetallePermiso',args=[row.id]))

@auth.requires(auth.is_logged_in() and not (auth.has_membership(role='Tutor Industrial')))
def consultarPermisos():
    userId=auth.user.id
    usuario=db(db.UsuarioUSB.auth_User == userId).select().first()
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
        permisos = db((db.Permiso.Estudiante == estudiante) & (db.Permiso.pasantia == db.Pasantia.id))
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
        links = [lambda row: generarLinksCoordinador(row)]
        form = SQLFORM.grid(query=permisos, fields=fields, headers=headers, orderby=default_sort_order,create=False, deletable=False, editable=False, maxtextlength=64, paginate=25,details=False,csv=False,user_signature=False,links=links)
    
        
    response.view = 'Permiso/Consultar_Permisos.html'
    return locals()


# Colocar algun tipo de notificacion cuando se procesa el permiso
@auth.requires(auth.is_logged_in() and not (auth.has_membership(role='Tutor Industrial')))
def aprobarPermiso():
    currentRoles = auth.user_groups.values()    
    permiso = db.Permiso(id=request.args[0])
    

    if 'Profesor' in currentRoles:
        permiso.update_record(aprobacion_tutor_academico="Aprobado")
        redirect(URL(c='Permiso',f='consultarPermisos'))
    elif ('CoordinadorCCT' in currentRoles) or ('Administrativo' in currentRoles):
        pasantia = db.Pasantia(id=permiso.pasantia)
        permiso.update_record(estado="Aprobado")

        ''' Chequeamos que las otras aprobaciones hayan sido hechas
            y pasamos la pasantia de preinscripcion a Inscripcion
        ''' 
        # Caso en el que el permiso es de inscripcion
        if (permiso.aprobacion_tutor_academico == 'Aprobado') and (permiso.aprobacion_coordinacion == 'Aprobado') and (permiso.Tipo == 'Inscripcion Extemporanea'):
            etapa = db(db.Etapa.nombre == 'Inscripcion').select().first()
            pasantia.update_record(etapa=etapa.id)
            redirect(URL(c='Permiso',f='consultarPermisos'))
        # Caso en el que el permiso es de retiro
        elif (permiso.aprobacion_tutor_academico == 'Aprobado') and (permiso.aprobacion_coordinacion == 'Aprobado') and (permiso.Tipo == 'Retiro Extemporaneo'):
            # Buscamos al usuario que tiene la pasantia inscrita y quitamos la referencia hacia la pasantia
            currentUser = auth.user_id
            print("Completar caso de uso de aprobacion de permiso de retiro extemporaneo")
            redirect(URL(c='Permiso',f='consultarPermisos'))

        elif (permiso.aprobacion_tutor_academico == 'Aprobado') and (permiso.aprobacion_coordinacion == 'Aprobado') and (permiso.Tipo == 'Evaluacion Extemporanea'):
            print("Completar caso de uso de aprobacion de permiso de evaluacion extemporanea")
            redirect(URL(c='Permiso',f='consultarPermisos'))


    elif 'Coordinador' in currentRoles:
        permiso.update_record(aprobacion_coordinacion="Aprobado")
        redirect(URL(c='Permiso',f='consultarPermisos'))

