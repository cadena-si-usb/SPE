# -*- coding: utf-8 -*-
from Preinscripciones import Preinscripcion

import Encoder

Preinscripcion = Preinscripcion()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []

    return locals()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar():
    form = SQLFORM(db.Preinscripcion)

    if form.process().accepted:
        session.flash = T('La preinscripcion fue agregada exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def count():
    obj = Encoder.to_dict(request.vars)
    count = Preinscripcion.count(obj)

    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db((db.Preinscripcion.pasantia == db.Pasantia.id) & (db.Pasantia.estudiante == db.Estudiante.id)).select()

    return rows.as_json()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar():
    record = db.Preinscripcion(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Preinscripcion, fields=['aprobacionCCT','comentarioCCT'],record=record,showid=False)
    if form.process().accepted:
        if request.vars.aprobacionCCT:
            existeColocacion = db(db.Colocacion.pasantia == record.pasantia).select().first()
            if not existeColocacion:
                colocacion = db.Colocacion.insert(pasantia=record.pasantia)

                pasantia = db.Pasantia(record.pasantia)
                etapaCol = db(db.Etapa.first_name == 'Colocacion').select().first()
                pasantia.update_record(etapa=etapaCol.id)

                record.update_record(estado='Aprobado')

        session.flash = T('La preinscripcion fue modificada exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def create():
    return request.vars
