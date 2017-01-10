# -*- coding: utf-8 -*-
from Carreras import Carrera
from applications.SPE_lib.modules.grids import single_table_spe_grid
import Encoder

Carrera = Carrera()

def sqlform_grid():
    sqlform_grid = single_table_spe_grid(db.Carrera)
    return sqlform_grid

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []

    return dict(rows=session.rows,id="prueba")

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar():
    fields = ['codigo','sede','tipo','descripcion']

    form = Carrera.form(fields)

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
    count = Carrera.count(obj)

    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db((db.Carrera.coordinacion == db.Coordinacion.id) & (db.Sede.id == db.Coordinacion.sede)).select()

    # rows = Carrera.find(obj)

    rows = rows.as_json()

    return rows

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar():
    record = db.Carrera(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Carrera, record,showid=False)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()
