# -*- coding: utf-8 -*-
from Areas_Laborales import Area_Laboral

import Encoder

Area_Laboral = Area_Laboral()

def listar():
    session.rows = []

    return dict(rows=session.rows,id="prueba")

def agregar():
    fields = ['nombre','descripcion']

    form = Area_Laboral.form(fields)

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
    count = Area_Laboral.count(obj)

    return count

def get():
    obj = Encoder.to_dict(request.vars)

    rows = Area_Laboral.find(obj)

    rows = rows.as_json()

    return rows

def modificar():
    record = db.Area_Laboral(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Area_Laboral, record,showid=False)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()
