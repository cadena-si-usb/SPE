# -*- coding: utf-8 -*-
from Administrativos import Administrativo

import Encoder
from applications.SPE_lib.modules.grids import simple_spe_grid
Administrativo = Administrativo()

def sqlform_grid():
    query = db(db.Administrativo.usuario == db.auth_user.id)
    db.auth_user._format = lambda row: row.first_name + " " + row.last_name

    fields = [
        db.auth_user.username,
        db.Administrativo.usuario,
        db.Administrativo.carnet,
        db.Administrativo.coordinacion,
        db.Administrativo.correo_Alternativo,
    ]

    if not request.args:
        return simple_spe_grid(query, fields=fields, field_id=db.Administrativo.id)
    elif request.args[-2] == 'new':
        return agregar(request)
    elif request.args[-3] == 'edit':
        return modificar(request)
    elif request.args[-3] == 'delete':
        return eliminar(request)
    else:
        return simple_spe_grid(query, fields=fields, field_id=db.Administrativo.id)

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows)

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar(request):
    fields = [
        'usuario',
        'carnet',
        'coordinacion',
        'correo_Alternativo',
    ]
    db.Administrativo.usuario.writable=True
    form = SQLFORM.factory(db.Administrativo, fields=fields, submit_button='Crear', showid=False)

    if form.process().accepted:
        # Actualizo los datos de usuario
        administrativoId = db.Administrativo.insert(
            usuario=form.vars.usuario,
            carnet=form.vars.carnet,
            coordinacion=form.vars.coordinacion,
            correo_Alternativo=form.vars.correo_Alternativo,
        )
        administrativo=db.Administrativo(id=administrativoId)
        group = db.auth_group(role="Administrativo")
        # Se agrega el rol
        membership = db.auth_membership.insert(
            user_id=administrativo.usuario,
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
    count = Administrativo.count(obj)

    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db(((db.Administrativo.usuario == db.auth_user.id) & (db.Administrativo.sede == db.Sede.id)
               & (db.Administrativo.dedicacion == db.Dedicacion.id)
               & (db.Administrativo.categoria == db.Categoria.id)
               & (db.auth_user.auth_User == db.auth_user.id))).select()

    return rows.as_json()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar(request):
    fields = [
        'usuario',
        'carnet',
        'coordinacion',
        'correo_Alternativo',
    ]
    administrativo = db.Administrativo(request.args[-1]) or redirect(URL('agregar'))
    usuario = db.auth_user(administrativo.usuario)
    form = SQLFORM.factory(db.Administrativo,record=administrativo, fields=fields, submit_button='Actualizar', showid=False)

    if form.process().accepted:
        # Actualizo los datos exclusivos de administrativo
        administrativo.update_record(**db.Administrativo._filter_fields(form.vars))
        session.flash = T('Perfil actualizado exitosamente!')
        redirect(URL('sqlform_grid'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return form

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def eliminar(request):
    administrativo = db.Administrativo(request.args[-1]) or redirect(URL('agregar'))
    group = db.auth_group(role="Administrativo")
    # Se agrega el rol
    membership = db.auth_membership(
        user_id=administrativo.usuario,
        group_id=group.id,
    )
    administrativo.delete_record()
    membership.delete_record()
    redirect(URL('sqlform_grid'))