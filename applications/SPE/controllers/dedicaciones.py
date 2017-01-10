# -*- coding: utf-8 -*-
from Dedicaciones import Dedicacion

import Encoder
from applications.SPE_lib.modules.grids import single_table_spe_grid
Dedicacion = Dedicacion()

def sqlform_grid():
    sqlform_grid = single_table_spe_grid(db.Dedicacion)
    return sqlform_grid

def listar():
    session.rows = []

    return dict(rows=session.rows,id="prueba")

def agregar():
    fields = ['first_name']

    form = Dedicacion.form(fields)

    if form.process().accepted:
        session.flash = T('El material fue agregado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()

def count():
    obj = Encoder.to_dict(request.vars)
    count = Dedicacion.count(obj)

    return count

def get():
    obj = Encoder.to_dict(request.vars)

    rows = Dedicacion.find(obj)

    rows = rows.as_json()

    return rows

def modificar():
    record = db.Dedicacion(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Dedicacion, record,showid=False)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()
