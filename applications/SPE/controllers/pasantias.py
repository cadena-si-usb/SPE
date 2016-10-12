# -*- coding: utf-8 -*-
from Pasantias import Pasantia

import Encoder

Pasantia = Pasantia()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows)

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar():
    form = Pasantia.form(['titulo','estudiante','materia'])

    if form.process().accepted:
        session.flash = T('El material fue agregado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def count():
    obj = Encoder.to_dict(request.vars)
    count = Pasantia.count(obj)

    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = Pasantia.find(obj)

    rows = rows.as_json()

    return rows

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar():
    record = db.Pasantia(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Pasantia, fields=['etapa'],record=record,showid=False)
    if form.process().accepted:
        etapa=db.Etapa(id=record.etapa)
        if etapa.nombre=='Inscripcion':
            planes=db.Plan_Trabajo(pasantia=request.args(0))
            if not planes:
                db.Plan_Trabajo.insert(
                    id=request.args(0),
                    pasantia=request.args(0)
                )
            inscripcion=db.Inscripcion(pasantia=request.args(0))
            if not inscripcion:
                # Registramos el usuario externo
                db.Inscripcion.insert(
                    id=request.args(0),
                    pasantia=request.args(0)
                )
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def create():
    return request.vars
