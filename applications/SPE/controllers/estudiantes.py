# -*- coding: utf-8 -*-
from Estudiantes import Estudiante

import Encoder

Estudiante = Estudiante()

def listar():
    session.rows = []
    return dict(rows=session.rows)

def agregar():
    form = SQLFORM(db.Estudiante)

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
    count = Estudiante.count(obj)

    return count

def get():
    obj = Encoder.to_dict(request.vars)

    rows = db(((db.Estudiante.usuario == db.UsuarioUSB.id) & (db.Estudiante.carrera == db.Carrera.id))).select()

    return rows.as_json()

def modificar():
    record = db.Estudiante(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Estudiante, record)
    if form.process().accepted:
        session.flash = T('El Estudiante fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()