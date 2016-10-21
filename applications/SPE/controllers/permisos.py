# -*- coding: utf-8 -*-
from Permisos import Permiso
from Permisos_Evaluacion import Permiso_Evaluacion
from gluon import current

import Encoder

Permiso = Permiso()
Permiso_Evaluacion = Permiso_Evaluacion()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows,id="prueba")

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar():
    currentRoles = current.auth.user_groups.values()
    permisoBD = db.Permiso
    fieldsEstudiante = ['Tipo','pasantia','justificacion']
    fieldsCoordinadorCCT = ['Estudiante', 'Tipo', 'pasantia', 'justificacion']
    
    
    if 'Estudiante' in currentRoles:
        permisoBD.Estudiante.writable = False
        permisoBD.Estudiante.default = current.auth.user_id
        form = Permiso.form(fieldsEstudiante)
    elif 'CoordinadorCCT' in currentRoles:
        form = Permiso.form(fieldsCoordinadorCCT)
    else:
        redirect(URL(c='default', f='index'))


    if form.process().accepted:
        session.flash = T('El material fue agregado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')
  
    return locals()



@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar_evaluacion():
    currentRoles = current.auth.user_groups.values()
    permisoBD = db.Permiso_Evaluacion
    fieldsEstudiante = ['pasantia','justificacion','calendario_compromisos']
    fieldsCoordinadorCCT = ['Estudiante', 'Tipo', 'pasantia', 'justificacion', 'calendario_compromisos']

    permisoBD.Tipo.writable = False
    permisoBD.Tipo.default = 'Evaluacion Extemporanea'

    if 'Estudiante' in currentRoles:
        permisoBD.Estudiante.writable = False
        permisoBD.Estudiante.default = current.auth.user_id
        #form = SQLFORM.factory(permisoBD,fields=fields,showid=False)
        form = Permiso_Evaluacion.form(fieldsEstudiante)
    elif 'CoordinadorCCT' in currentRoles:
        #form = SQLFORM.factory(permisoBD,fields=None,showid=False)
        form = Permiso_Evaluacion.form(fieldsCoordinadorCCT)
    else:
        redirect(URL(c='default',f='index'))

    if form.process().accepted:
        session.flash = T('El material fue agregado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()


@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def count():
    obj = Encoder.to_dict(request.vars)
    count = Permiso.count(obj)
    return count


@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db(
        (db.Permiso.pasantia == db.Pasantia.id) & (db.Pasantia.estudiante == db.Estudiante.id) &
        (db.UsuarioUSB.id == db.Estudiante.usuario) & (db.auth_user.id == db.UsuarioUSB.auth_User)).select(
        orderby=db.auth_group.role)
    rows = rows.as_json()
    return rows


@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar():

    currentRoles = current.auth.user_groups.values()
    record = (db.Permiso(request.args(0)) or db.Permiso_Evaluacion(request.args(0))) or redirect(URL('agregar'))

    # Agregar caso en el que el permiso es de evaluacion
    if 'Estudiante' in currentRoles:
        fields = ['justificacion']
        form = SQLFORM(db.Permiso,record,fields=fields,showid=False)
    if 'Profesor' in currentRoles:
        fields = ['aprobacion_tutor_academico']
        form = SQLFORM(db.Permiso,record,fields=fields,showid=False)
    elif 'Coordinador' in currentRoles:
        fields = ['aprobacion_coordinacion']
        form = SQLFORM(db.Permiso,record,fields=fields,showid=False)
    elif 'CoordinadorCCT' in currentRoles:
        form = SQLFORM(db.Permiso,record,fields=None,showid=False)
    else:
        redirect(URL(c='default', f='index'))


    if form.process().accepted:
        session.flash = T('El material fue agregado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')
    
    return locals()



    # record = db.Permiso(request.args(0)) or redirect(URL('agregar'))
    # form = SQLFORM(db.Permiso, record,showid=False)
    # if form.process().accepted:
    #     session.flash = T('El material fue modificado exitosamente!')
    #     redirect(URL('listar'))
    # else:
    #     response.flash = T('Por favor llene la forma.')
    # return locals()


@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def ver():
    # Hacer try/catch y que saque el permiso de la tabla de permisos o permiso_evaluacion
    record = db.Permiso(request.args(0))
    return locals()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def ver_evaluacion():
    record = db.Permiso_Evaluacion(request.args(0))
    return locals()