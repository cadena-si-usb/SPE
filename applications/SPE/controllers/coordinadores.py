# -*- coding: utf-8 -*-
from Coordinadores import Coordinador

import Encoder
from applications.SPE_lib.modules.grids import simple_spe_grid
Coordinador = Coordinador()

def sqlform_grid():
    query = db(db.Coordinador.usuario == db.auth_user.id)
    db.auth_user._format = lambda row: row.first_name + " " + row.last_name

    fields = [
        db.auth_user.username,
        db.Coordinador.usuario,
        db.Coordinador.carnet,
        db.Coordinador.coordinacion,
        db.Coordinador.correo_Alternativo,
    ]

    if not request.args:
        return simple_spe_grid(query, fields=fields, field_id=db.Coordinador.id)
    elif request.args[-2] == 'new':
        return agregar(request)
    elif request.args[-3] == 'edit':
        return modificar(request)
    elif request.args[-3] == 'delete':
        return eliminar(request)
    else:
        return simple_spe_grid(query, fields=fields, field_id=db.Coordinador.id)


@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows)

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar(request):
    fields = [
        'usuario',
        'carnet',
        'correo_Alternativo',
        'coordinacion'
    ]
    db.Coordinador.usuario.writable=True
    form = SQLFORM.factory(db.Coordinador, fields=fields, submit_button='Crear', showid=False)

    if form.process().accepted:
        # Actualizo los datos de usuario
        coordinadorId = db.Coordinador.insert(
            usuario=form.vars.usuario,
            carnet=form.vars.carnet,
            correo_Alternativo=form.vars.correo_Alternativo,
            coordinacion=form.vars.coordinacion,
        )
        coordinador=db.Coordinador(id=coordinadorId)
        group = db.auth_group(role="Coordinador")
        # Se agrega el rol
        membership = db.auth_membership.insert(
            user_id=coordinador.usuario,
            group_id=group.id,
        )
        # Actualizo los datos exclusivos de estudiante
        session.flash = T('Perfil actualizado exitosamente!')
        redirect(URL('sqlform_grid'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return form

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def count():
    obj = Encoder.to_dict(request.vars)
    count = Coordinador.count(obj)

    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db(((db.Coordinador.usuario == db.auth_user.id) & (db.Coordinador.sede == db.Sede.id)
               & (db.Coordinador.dedicacion == db.Dedicacion.id)
               & (db.Coordinador.categoria == db.Categoria.id)
               & (db.auth_user.auth_User == db.auth_user.id))).select()

    return rows.as_json()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar(request):
    fields = [
        'usuario',
        'carnet',
        'correo_Alternativo',
        'coordinacion'
    ]
    coordinador = db.Coordinador(request.args[-1]) or redirect(URL('agregar'))
    usuario = db.auth_user(coordinador.usuario)
    form = SQLFORM.factory(db.Coordinador,record=coordinador, fields=fields, submit_button='Actualizar', showid=False)

    if form.process().accepted:
        # Actualizo los datos exclusivos de coordinador
        coordinador.update_record(**db.Coordinador._filter_fields(form.vars))
        session.flash = T('Perfil actualizado exitosamente!')
        redirect(URL('sqlform_grid'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return form

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def eliminar(request):
    coordinador = db.Coordinador(request.args[-1]) or redirect(URL('agregar'))
    group = db.auth_group(role="Coordinador")
    # Se agrega el rol
    membership = db.auth_membership(
        user_id=coordinador.usuario,
        group_id=group.id,
    )
    coordinador.delete_record()
    membership.delete_record()
    redirect(URL('sqlform_grid'))