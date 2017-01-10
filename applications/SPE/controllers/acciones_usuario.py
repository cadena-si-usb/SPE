# -*- coding: utf-8 -*-
from Acciones_Usuario import Accion_Usuario
from applications.SPE_lib.modules.grids import single_table_spe_grid
import Encoder

Accion_Usuario = Accion_Usuario()

def sqlform_grid():
    sqlform_grid = single_table_spe_grid(db.Accion_Usuario)
    return sqlform_grid

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []

    return dict(rows=session.rows,id="prueba")

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar():
    fields = ['first_name','destino','rol','contexto']

    form = Accion_Usuario.form(fields)

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
    count = Accion_Usuario.count(obj)

    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db((db.Accion_Usuario.rol==db.auth_group.id)).select()

    #rows = Accion_Usuario.find(obj)

    rows = rows.as_json()

    return rows

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar():
    record = db.Accion_Usuario(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Accion_Usuario, record,showid=False)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()
