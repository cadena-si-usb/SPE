# -*- coding: utf-8 -*-
from Membresias import Membresia

import Encoder
from applications.SPE_lib.modules.grids import simple_spe_grid
Membresia = Membresia()

def sqlform_grid():
    sqlform_grid = simple_spe_grid(db.auth_membership)
    return sqlform_grid

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []

    return dict(rows=session.rows,id="prueba")

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar():
    fields = ['user_id','group_id']
    db.auth_membership.user_id.requires=IS_IN_DB(db,'auth_user.id','%(first_name)s %(last_name)s - %(username)s - %(email)s')
    form = Membresia.form(fields)

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
    count = Membresia.count(obj)

    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db((db.auth_membership.user_id==db.auth_user.id) & (db.auth_membership.group_id==db.auth_group.id)).select(orderby=db.auth_group.role)

    # rows = Rol.find(obj)

    rows = rows.as_json()

    return rows

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar():
    db.auth_membership.user_id.requires = IS_IN_DB(db, 'auth_user.id',
                                                   '%(first_name)s %(last_name)s - %(username)s - %(email)s')
    record = db.auth_membership(request.args(0)) or redirect(URL('agregar'))

    form = SQLFORM(db.auth_membership, record,showid=False)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()
