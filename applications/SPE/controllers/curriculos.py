# -*- coding: utf-8 -*-
from Curriculos import Curriculo

import Encoder

Curriculo = Curriculo()

def listar():
    session.rows = []
    return dict(rows=session.rows)

def agregar():
    fields = ['nombre']

    form = Curriculo.form(fields)

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
    count = Curriculo.count(obj)

    return count

def get():
    obj = Encoder.to_dict(request.vars)

    rows = Curriculo.find(obj)

    rows = rows.as_json()

    return rows

def modificar():
    record = db.Curriculo(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Curriculo, record)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()
