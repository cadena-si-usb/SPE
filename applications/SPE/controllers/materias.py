# -*- coding: utf-8 -*-
from Materias import Materia

import Encoder

Materia = Materia()

def listar():
    session.rows = []

    return dict(rows=session.rows,id="prueba")

def agregar():
    fields = ['codigo','sede','tipo','descripcion']

    form = Materia.form(fields)

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
    count = Materia.count(obj)

    return count

def get():
    obj = Encoder.to_dict(request.vars)

    rows = Materia.find(obj)

    rows = rows.as_json()

    return rows

def modificar():
    record = db.Materia(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Materia, record)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()
