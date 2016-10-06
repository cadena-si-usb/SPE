# -*- coding: utf-8 -*-
from Roles import Rol

import Encoder

Rol = Rol()

def listar():
    session.rows = []

    return dict(rows=session.rows,id="prueba")

def agregar():
    fields = ['role', 'description']

    form = Rol.form(fields)

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
    count = Rol.count(obj)

    return count

def get():
    obj = Encoder.to_dict(request.vars)

    rows = db(db.auth_group).select(orderby=db.auth_group.role)

    # rows = Rol.find(obj)

    rows = rows.as_json()

    return rows

def modificar():
    record = db.auth_group(request.args(0)) or redirect(URL('agregar'))
    # Si es uno de los roles por defecto evitamos que se puedan editar
    if ((record.role=='Estudiante') or (record.role=='Profesor') or (record.role=='Coordinador') or
        (record.role == 'Empresa') or (record.role=='Tutor Industrial') or (record.role=='CoordinadorCCT')):
        db.auth_group.role.writable=False

    form = SQLFORM(db.auth_group, record,showid=False)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()
