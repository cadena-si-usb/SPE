# -*- coding: utf-8 -*-
from Coordinaciones import Coordinacion

import Encoder

Coordinacion = Coordinacion()

def listar():
    session.rows = []

    return dict(rows=session.rows,id="prueba")

def agregar():
    fields = ['nombre','usbid','sede']

    form = Coordinacion.form(fields)

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
    count = Coordinacion.count(obj)

    return count

def get():
    obj = Encoder.to_dict(request.vars)

    rows = db((db.Coordinacion.sede == db.Sede.id)).select()

    # rows = Coordinacion.find(obj)

    rows = rows.as_json()

    return rows

def modificar():
    record = db.Coordinacion(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Coordinacion, record,showid=False)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()
