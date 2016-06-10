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

def editar():
    response.view = 'curriculos/editar.load.html'

    fields = [
        'electivas',
        'cursos',
        'aficiones',
        'idiomas'         
    ]

    userid = str(auth.user['username'])

    estudiante = db.Estudiante(db.Estudiante.carnet == userid)

    curriculo = db.Curriculo(db.Curriculo.estudiante == estudiante['id'])

    form = SQLFORM(db.Curriculo,record=curriculo,fields=fields,submit_button='Actualizar',showid=False)

    if form.process().accepted:
        session.flash = T('Perfil actualizado exitosamente!')
        curriculo.update_record(activo=True)
        redirect(URL('curriculo'))
    else:
        response.flash = T('Por favor llene la forma.')

    return dict(form=form)