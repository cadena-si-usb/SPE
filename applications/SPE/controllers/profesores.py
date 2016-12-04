# -*- coding: utf-8 -*-
from Profesores import Profesor

import Encoder

Profesor = Profesor()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows)

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar():
    fields = [
        'usbid',
        'first_name',
        'last_name',
        'email',
        'tipo_documento',
        'numero_documento',
        'telefono',
        'direcUsuario',
        'sexo',
        'activo',
        'categoria',
        'dedicacion',
        'departamento',
        'sede'
    ]

    form = SQLFORM.factory(db.auth_user,db.UsuarioUSB, db.Profesor, fields=fields, submit_button='Crear', showid=False)

    if form.process().accepted:
        authId=db.auth_user.insert(first_name=form.vars.first_name,
                            last_name=form.vars.last_name,
                            email=form.vars.email)
        # Actualizo los datos de usuario
        usuarioUSBId=db.UsuarioUSB.insert(
            id=authId,
            auth_User=authId,
            usbid=form.vars.usbid,
            first_name=form.vars.first_name,
            last_name=form.vars.last_name,
            email=form.vars.email,
            tipo_documento=form.vars.tipo_documento,
            numero_documento=form.vars.numero_documento,
            telefono=form.vars.telefono,
            direcUsuario=form.vars.direcUsuario,
            sexo=form.vars.sexo,
            activo=form.vars.activo,
        )
        # Actualizo los datos de usuario
        profesorId = db.Profesor.insert(
            id=authId,
            usuario=usuarioUSBId,
            categoria=form.vars.categoria,
            dedicacion=form.vars.dedicacion,
            departamento=form.vars.departamento,
            sede=form.vars.sede,
            activo=form.vars.activo,
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
    count = Profesor.count(obj)

    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db(((db.Profesor.usuario == db.UsuarioUSB.id) & (db.Profesor.sede == db.Sede.id)
               & (db.Profesor.dedicacion == db.Dedicacion.id)
               & (db.Profesor.categoria == db.Categoria.id)
               & (db.UsuarioUSB.auth_User == db.auth_user.id))).select()

    return rows.as_json()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar():
    fields = [
        'usbid',
        'first_name',
        'last_name',
        'email',
        'tipo_documento',
        'numero_documento',
        'telefono',
        'direcUsuario',
        'sexo',
        'activo',
        'categoria',
        'dedicacion',
        'departamento',
        'sede'
    ]
    profesor = db.Profesor(request.args(0)) or redirect(URL('agregar'))
    usuario = db.UsuarioUSB(profesor.usuario)
    usuarioAuth = db.auth_user(usuario.auth_User)

    db.UsuarioUSB.first_name.default = usuario.first_name
    db.UsuarioUSB.last_name.default = usuario.last_name
    db.UsuarioUSB.email.default = usuario.email
    db.UsuarioUSB.tipo_documento.default = usuario.tipo_documento
    db.UsuarioUSB.numero_documento.default = usuario.numero_documento
    db.UsuarioUSB.telefono.default = usuario.telefono
    db.UsuarioUSB.direcUsuario.default = usuario.direcUsuario
    db.UsuarioUSB.sexo.default = usuario.sexo
    db.UsuarioUSB.activo.default = usuario.activo

    db.Profesor.categoria.default = profesor.categoria
    db.Profesor.dedicacion.default = profesor.dedicacion
    db.Profesor.departamento.default = profesor.departamento
    db.Profesor.sede.default = profesor.sede
    form = SQLFORM.factory(db.auth_user,db.UsuarioUSB, db.Profesor, fields=fields, submit_button='Actualizar', showid=False)

    if form.process().accepted:
        #
        usuarioAuth.update_record(first_name=form.vars.first_name,
                                  last_name=form.vars.last_name,
                                  email=form.vars.email)
        # Actualizo los datos de usuario
        usuario.update_record(**db.UsuarioUSB._filter_fields(form.vars))
        # Actualizo los datos exclusivos de profesor
        profesor.update_record(**db.Profesor._filter_fields(form.vars))
        session.flash = T('Perfil actualizado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()