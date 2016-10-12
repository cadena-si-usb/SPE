# -*- coding: utf-8 -*-
from Permisos import Permiso

import Encoder

Permiso = Permiso()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows,id="prueba")

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar():
    fields = ['Tipo','pasantia','estado']

    form = Permiso.form(fields)

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
    record = db.Permiso(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Permiso, record,showid=False)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()
