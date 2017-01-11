# -*- coding: utf-8 -*-
from Estudiantes import Estudiante

import Encoder
from applications.SPE_lib.modules.grids import simple_spe_grid
Estudiante = Estudiante()

def sqlform_grid():
    sqlform_grid = simple_spe_grid(db.Estudiante)
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
        'carrera',
        'sede'
    ]

    form = SQLFORM.factory(db.auth_user, db.Estudiante, fields=fields, submit_button='Crear', showid=False)

    if form.process().accepted:
        authId=db.auth_user.insert(
                            username=form.vars.username,
                            first_name=form.vars.first_name,
                            last_name=form.vars.last_name,
                            email=form.vars.email,
                            tipo_documento=form.vars.tipo_documento,
                            numero_documento=form.vars.numero_documento,
                            telefono=form.vars.telefono,
                            direccion=form.vars.direccion,
                            sexo=form.vars.sexo,
                            activo=form.vars.activo,
        )
        # Actualizo los datos de usuario
        estudianteId = db.Estudiante.insert(
            id=authId,
            usuario=authId,
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

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def count():
    obj = Encoder.to_dict(request.vars)
    count = Estudiante.count(obj)

    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db(((db.Estudiante.usuario == db.auth_user.id) & (db.Estudiante.carrera == db.Carrera.id) &
               (db.Estudiante.sede == db.Sede.id))).select()

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
        'activo'
    ]
    estudiante = db.Estudiante(request.args(0)) or redirect(URL('agregar'))
    usuario = db.auth_user(estudiante.usuario) or redirect(URL('agregar'))
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


    fields.append('carnet')
    fields.append('carrera')
    fields.append('sede')
    db.Estudiante.carnet.default = estudiante.carnet
    db.Estudiante.carrera.default = estudiante.carrera
    db.Estudiante.sede.default = estudiante.sede
    form = SQLFORM.factory(db.auth_user, db.Estudiante, fields=fields, submit_button='Actualizar', showid=False)

    if form.process().accepted:
        #
        usuarioAuth.update_record(first_name=form.vars.first_name,
                                  last_name=form.vars.last_name,
                                  email=form.vars.email)
        # Actualizo los datos de usuario
        usuario.update_record(**db.auth_user._filter_fields(form.vars))
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