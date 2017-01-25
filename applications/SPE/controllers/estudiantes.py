# -*- coding: utf-8 -*-
from Estudiantes import Estudiante

import Encoder
from applications.SPE_lib.modules.grids import simple_spe_grid
Estudiante = Estudiante()


def sqlform_grid():
    if not request.args:
        return simple_spe_grid(db.Estudiante)
    elif request.args[-2]=='new':
        return agregar(request)
    elif request.args[-3]=='edit':
        return modificar(request)
    elif request.args[-3]=='delete':
        return eliminar(request)
    else:
        return simple_spe_grid(db.Estudiante)

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows)

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar(request):
    fields = [
        'usuario',
        'carnet',
        'carrera',
        'sede'
    ]
    db.Estudiante.usuario.writable=True
    form = SQLFORM.factory(db.Estudiante, fields=fields, submit_button='Crear', showid=False)

    if form.process().accepted:
        # Actualizo los datos de usuario
        estudianteId = db.Estudiante.insert(
            usuario=form.vars.usuario,
            carnet=form.vars.carnet,
            carrera=form.vars.carrera,
            sede=form.vars.sede,
            activo=form.vars.activo,
        )
        estudiante=db.Estudiante(id=estudianteId)
        group = db.auth_group(role="Estudiante")
        # Se agrega el rolProfesor
        membership = db.auth_membership.insert(
            user_id=estudiante.usuario,
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
    count = Estudiante.count(obj)

    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db(((db.Estudiante.usuario == db.auth_user.id) & (db.Estudiante.carrera == db.Carrera.id) &
               (db.Estudiante.sede == db.Sede.id))).select()

    return rows.as_json()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar(request):
    fields = [
        'usuario',
        'carnet',
        'carrera',
        'sede'
    ]
    estudiante = db.Estudiante(request.args[-1]) or redirect(URL('agregar'))
    form = SQLFORM.factory(db.Estudiante,record=estudiante,fields=fields, submit_button='Actualizar', showid=False)

    if form.process().accepted:
        # Actualizo los datos exclusivos de estudiante
        estudiante.update_record(**db.Estudiante._filter_fields(form.vars))
        session.flash = T('Perfil actualizado exitosamente!')
        redirect(URL('sqlform_grid'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return form

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def eliminar(request):
    estudiante = db.Estudiante(request.args[-1]) or redirect(URL('agregar'))
    group = db.auth_group(role="Estudiante")
    # Se agrega el rol
    membership = db.auth_membership(
        user_id=estudiante.usuario,
        group_id=group.id,
    )
    estudiante.delete_record()
    membership.delete_record()
    redirect(URL('sqlform_grid'))