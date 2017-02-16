# -*- coding: utf-8 -*-
from Acceso_Etapa import Acceso_Etapa
from Usuarios import Usuario
import Encoder
from applications.SPE_lib.modules.grids import simple_spe_grid
Acceso_Etapa = Acceso_Etapa()
Usuario = Usuario()

def sqlform_grid():
    sqlform_grid = simple_spe_grid(db.Acceso_Etapa)
    return sqlform_grid

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows,id="prueba")
@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar():
    fields = ['rol','etapa']

    form = Acceso_Etapa.form(fields)

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
    count = Acceso_Etapa.count(obj)

    return count
@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db(
        (db.Acceso_Etapa.rol == db.auth_group.id) & (db.Etapa.id == db.Acceso_Etapa.etapa)).select(
        orderby=db.auth_group.role)

    # rows = Acceso_Etapa.find(obj)

    rows = rows.as_json()

    return rows
@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar():
    record = db.Acceso_Etapa(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Acceso_Etapa, record,showid=False)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()
