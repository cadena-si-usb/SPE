# -*- coding: utf-8 -*-
from Coordinadores import Coordinador

import Encoder
from applications.SPE_lib.modules.grids import simple_spe_grid
Coordinador = Coordinador()

def sqlform_grid():
    sqlform_grid = simple_spe_grid(db.Coordinador)
    return sqlform_grid

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows)

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar():
    fields = [
        'first_name',
        'last_name',
        'email',
        'tipo_documento',
        'numero_documento',
        'telefono',
        'direccion',
        'sexo',
        'activo',
        'carnet',
        'correo_Alternativo',
        'coordinacion'
    ]

    form = SQLFORM.factory(db.auth_user, db.auth_user, db.Coordinador, fields=fields, submit_button='Actualizar',
                           showid=False)

    if form.process().accepted:
        authId=db.auth_user.insert(first_name=form.vars.first_name,
                            last_name=form.vars.last_name,
                            email=form.vars.email,
                            username=form.vars.username,
                            tipo_documento=form.vars.tipo_documento,
                            numero_documento=form.vars.numero_documento,
                            telefono=form.vars.telefono,
                            direccion=form.vars.direccion,
                            sexo=form.vars.sexo,
                            activo=form.vars.activo,
        )
        # Actualizo los datos de usuario
        coordinadorId = db.Coordinador.insert(
            id=authId,
            usuario=authId,
            carnet=form.vars.carnet,
            correo_Alternativo=form.vars.correo_Alternativo,
            coordinacion=form.vars.coordinacion,
        )
        # Actualizo los datos exclusivos de estudiante
        session.flash = T('Perfil actualizado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def count():
    obj = Encoder.to_dict(request.vars)
    count = Coordinador.count(obj)
    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db(((db.Coordinador.usuario == db.auth_user.id) & (db.Coordinador.coordinacion == db.Coordinacion.id) &
               (db.Coordinacion.sede == db.Sede.id))).select()

    return rows.as_json()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar():
    fields = [
        'first_name',
        'last_name',
        'email',
        'tipo_documento',
        'numero_documento',
        'telefono',
        'direccion',
        'sexo',
        'activo',
        'carnet',
        'correo_Alternativo',
        'coordinacion'
    ]

    coordinador = db.Coordinador(request.args(0)) or redirect(URL('agregar'))

    usuario = db.auth_user(coordinador.usuario) or redirect(URL('agregar'))

    usuarioAuth = db.auth_user(usuario.auth_User) or redirect(URL('agregar'))

    db.auth_user.first_name.default = usuario.first_name
    db.auth_user.last_name.default = usuario.last_name
    db.auth_user.email.default = usuario.email
    db.auth_user.tipo_documento.default = usuario.tipo_documento
    db.auth_user.numero_documento.default = usuario.numero_documento
    db.auth_user.telefono.default = usuario.telefono
    db.auth_user.direccion.default = usuario.direccion
    db.auth_user.sexo.default = usuario.sexo
    db.auth_user.activo.default = usuario.activo

    db.Coordinador.carnet.default = coordinador.carnet
    db.Coordinador.correo_Alternativo.default = coordinador.correo_Alternativo
    db.Coordinador.coordinacion.default = coordinador.coordinacion

    form = SQLFORM.factory(db.auth_user,db.auth_user, db.Coordinador, fields=fields, submit_button='Actualizar', showid=False)

    if form.process().accepted:
        #
        usuarioAuth.update_record(first_name=form.vars.first_name,
                                  last_name=form.vars.last_name,
                                  email=form.vars.email)
        # Actualizo los datos de usuario
        usuario.update_record(**db.auth_user._filter_fields(form.vars))
        # Actualizo los datos exclusivos de estudiante
        coordinador.update_record(**db.Estudiante._filter_fields(form.vars))
        session.flash = T('Perfil actualizado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()