# -*- coding: utf-8 -*-
from Administrativos import Administrativo

import Encoder

Administrativo = Administrativo()

def listar():
    session.rows = []
    return dict(rows=session.rows)

def agregar():

    fields = [
        'nombre',
        'apellido',
        'correo',
        'tipo_documento',
        'numero_documento',
        'telefono',
        'direcUsuario',
        'sexo',
        'activo',
        'carnet',
        'coordinacion',
        'correo_Alternativo',
    ]

    form = SQLFORM.factory(db.UsuarioUSB, db.Administrativo, fields=fields, submit_button='Crear', showid=False)

    if form.process().accepted:
        authId=db.auth_user.insert(first_name=form.vars.nombre,
                            last_name=form.vars.apellido,
                            email=form.vars.correo)
        # Actualizo los datos de usuario
        usuarioUSBId=db.UsuarioUSB.insert(
            id=authId,
            auth_User=authId,
            usbid=form.vars.usbid,
            nombre=form.vars.nombre,
            apellido=form.vars.apellido,
            correo=form.vars.correo,
            tipo_documento=form.vars.tipo_documento,
            numero_documento=form.vars.numero_documento,
            telefono=form.vars.telefono,
            direcUsuario=form.vars.direcUsuario,
            sexo=form.vars.sexo,
            activo=form.vars.activo,
        )
        # Actualizo los datos de usuario
        administrativosId = db.Administrativo.insert(
            id=authId,
            usuario=usuarioUSBId,
            carnet=form.vars.carnet,
            coordinacion=form.vars.coordinacion,
            correo_Alternativo=form.vars.correo_Alternativo
        )
        # Actualizo los datos exclusivos de estudiante
        session.flash = T('Perfil actualizado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()

def count():
    obj = Encoder.to_dict(request.vars)
    count = Administrativo.count(obj)

    return count

def get():
    obj = Encoder.to_dict(request.vars)

    rows = db(((db.Administrativo.usuario == db.UsuarioUSB.id) & (db.auth_user.id == db.UsuarioUSB.auth_User) &
               (db.Administrativo.coordinacion == db.Coordinacion.id) & (db.Coordinacion.sede == db.Sede.id))).select()

    return rows.as_json()

def modificar():
    fields = [
        'nombre',
        'apellido',
        'correo',
        'tipo_documento',
        'numero_documento',
        'telefono',
        'direcUsuario',
        'sexo',
        'activo',
        'carnet',
        'coordinacion',
        'correo_Alternativo',
    ]
    administrativo = db.Administrativo(request.args(0)) or redirect(URL('agregar'))
    usuario = db.UsuarioUSB(administrativo.usuario) or redirect(URL('agregar'))
    usuarioAuth = db.auth_user(usuario.auth_User) or redirect(URL('agregar'))

    db.UsuarioUSB.nombre.default = usuario.nombre
    db.UsuarioUSB.apellido.default = usuario.apellido
    db.UsuarioUSB.correo.default = usuario.correo
    db.UsuarioUSB.tipo_documento.default = usuario.tipo_documento
    db.UsuarioUSB.numero_documento.default = usuario.numero_documento
    db.UsuarioUSB.telefono.default = usuario.telefono
    db.UsuarioUSB.direcUsuario.default = usuario.direcUsuario
    db.UsuarioUSB.sexo.default = usuario.sexo
    db.UsuarioUSB.activo.default = usuario.activo


    db.Administrativo.carnet.default = administrativo.carnet
    db.Administrativo.coordinacion.default = administrativo.coordinacion
    db.Administrativo.correo_Alternativo.default = administrativo.correo_Alternativo

    form = SQLFORM.factory(db.auth_user,db.UsuarioUSB, db.Administrativo, fields=fields, submit_button='Actualizar', showid=False)

    if form.process().accepted:
        #
        usuarioAuth.update_record(first_name=form.vars.nombre,
                                  last_name=form.vars.apellido,
                                  email=form.vars.correo)
        # Actualizo los datos de usuario
        usuario.update_record(**db.UsuarioUSB._filter_fields(form.vars))
        # Actualizo los datos exclusivos de estudiante
        administrativo.update_record(**db.Administrativo._filter_fields(form.vars))
        session.flash = T('Perfil actualizado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()