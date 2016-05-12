# -*- coding: utf-8 -*-
from PlanesTrabajo import PlanTrabajo

import Encoder

PlanTrabajo = PlanTrabajo()

def listar():
    session.rows = []
    return dict(rows=session.rows)

def agregar():
    fields = ['nombre']

    form = PlanTrabajo.form(fields)

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
    count = PlanTrabajo.count(obj)

    return count

def get():
    obj = Encoder.to_dict(request.vars)

    rows = PlanTrabajo.find(obj)

    rows = rows.as_json()

    return rows

def modificar():
    record = db.PlanTrabajo(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.PlanTrabajo, record)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()
