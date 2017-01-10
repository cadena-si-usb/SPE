# -*- coding: utf-8 -*-
from Materias_Periodo import Materia_Periodo

import Encoder
from applications.SPE_lib.modules.grids import single_table_spe_grid
Materia_Periodo = Materia_Periodo()

def sqlform_grid():
    sqlform_grid = single_table_spe_grid(db.Materia_Periodo)
    return sqlform_grid

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows,id="prueba")

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar():
    fields = ['materia','periodo']

    form = Materia_Periodo.form(fields)

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
    count = Materia_Periodo.count(obj)

    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db((db.Materia_Periodo.materia == db.Materia.id) & (db.Periodo.id == db.Materia_Periodo.periodo)).select()

    rows = rows.as_json()

    return rows

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar():
    record = db.Materia_Periodo(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Materia_Periodo, record,showid=False)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()
