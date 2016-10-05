# -*- coding: utf-8 -*-
from Estudiantes import Estudiante

import Encoder

Estudiante = Estudiante()

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
        'activo'
    ]

    fields.append('carnet')
    fields.append('carrera')
    fields.append('sede')
    form = SQLFORM.factory(db.UsuarioUSB, db.Estudiante, fields=fields, submit_button='Crear', showid=False)

    if form.process().accepted:
        authId=db.auth_user.insert(first_name=form.vars.nombre,
                            last_name=form.vars.apellido,
                            email=form.vars.correo)
        # Actualizo los datos de usuario
        usuarioUSBId=db.UsuarioUSB.insert(
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
        estudianteId = db.Estudiante.insert(
            usuario=usuarioUSBId,
            carnet=form.vars.carnet,
            carrera=form.vars.carrera,
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

def count():
    obj = Encoder.to_dict(request.vars)
    count = Estudiante.count(obj)

    return count

def get():
    obj = Encoder.to_dict(request.vars)

    rows = db(((db.Estudiante.usuario == db.UsuarioUSB.id) & (db.Estudiante.carrera == db.Carrera.id))).select()

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
        'activo'
    ]

    usuario = db.UsuarioUSB(request.args(0)) or redirect(URL('agregar'))

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

    estudiante = db.Estudiante(request.args(0)) or redirect(URL('agregar'))
    fields.append('carnet')
    fields.append('carrera')
    fields.append('sede')
    db.Estudiante.carnet.default = estudiante.carnet
    db.Estudiante.carrera.default = estudiante.carrera
    db.Estudiante.sede.default = estudiante.sede
    form = SQLFORM.factory(db.UsuarioUSB, db.Estudiante, fields=fields, submit_button='Actualizar', showid=False)

    if form.process().accepted:
        #
        usuarioAuth.update_record(first_name=form.vars.nombre,
                                  last_name=form.vars.apellido,
                                  email=form.vars.correo)
        # Actualizo los datos de usuario
        usuario.update_record(**db.UsuarioUSB._filter_fields(form.vars))
        # Actualizo los datos exclusivos de estudiante
        estudiante.update_record(**db.Estudiante._filter_fields(form.vars))
        usuario.update_record(activo=True)
        session.flash = T('Perfil actualizado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()