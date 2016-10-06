# -*- coding: utf-8 -*-
from Acciones_Usuario import Accion_Usuario

import Encoder

Accion_Usuario = Accion_Usuario()

def listar():
    session.rows = []

    return dict(rows=session.rows,id="prueba")

def agregar():
    fields = ['nombre','destino','rol','contexto']

    form = Accion_Usuario.form(fields)

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
    count = Accion_Usuario.count(obj)

    return count

def get():
    obj = Encoder.to_dict(request.vars)

    rows = db((db.Accion_Usuario.rol==db.auth_group.id)).select()

    #rows = Accion_Usuario.find(obj)

    rows = rows.as_json()

    return rows

def modificar():
    record = db.Accion_Usuario(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Accion_Usuario, record,showid=False)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()
