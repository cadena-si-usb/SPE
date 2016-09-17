# -*- coding: utf-8 -*-
from Colocaciones import Colocacion

import Encoder

Colocacion = Colocacion()

def listar():
    session.rows = []

    return locals()

def agregar():
    form = SQLFORM(db.Colocacion)

    if form.process().accepted:
        session.flash = T('La Colocacion fue agregada exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()

def count():
    obj = Encoder.to_dict(request.vars)
    count = Colocacion.count(obj)

    return count

def get():
    obj = Encoder.to_dict(request.vars)

    rows = db((db.Colocacion.pasantia == db.Pasantia.id) & (db.Pasantia.estudiante == db.Estudiante.id) & (db.Estudiante.carrera == db.Carrera.id)).select()

    return rows.as_json()


# -*- coding: utf-8 -*-

def modificar():
    record = db.Colocacion(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Colocacion, fields=['aprobacionCCT','comentarioCCT'],record=record,showid=False)
    if form.process().accepted:
        if request.vars.aprobacionCCT:
            existeInscripcion = db(db.Inscripcion.pasantia == record.pasantia).select().first()
            if not existeInscripcion:
                inscripcion = db.Inscripcion.insert(pasantia=record.pasantia)
                plan_trabajo = db.Plan_Trabajo.insert(pasantia=record.pasantia)

                pasantia = db.Pasantia(record.pasantia)
                etapaInsc = db(db.Etapa.nombre == 'Inscripcion').select().first()
                pasantia.update_record(etapa=etapaInsc.id)

                record.update_record(estado='Aprobado')

        session.flash = T('La Colocacion fue modificada exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()

def create():
    return request.vars
