# -*- coding: utf-8 -*-
from Departamentos import Departamento

import Encoder

Departamento = Departamento()

def listar():
    session.rows = []

    return dict(rows=session.rows,id="prueba")

def agregar():
    fields = ['nombre','id_division','email_dep','sede']

    form = Departamento.form(fields)

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
    count = Departamento.count(obj)

    return count

def get():
    obj = Encoder.to_dict(request.vars)

    rows = db((db.Departamento.sede==db.Sede.id) & (db.Departamento.id_division==db.Division.id)).select()

    # rows = Departamento.find(obj)

    rows = rows.as_json()

    return rows

def modificar():
    record = db.Departamento(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Departamento, record,showid=False)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()
