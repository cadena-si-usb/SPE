# -*- coding: utf-8 -*-
from Inscripciones import Inscripcion

import Encoder
from applications.SPE_lib.modules.grids import simple_spe_grid

Inscripcion = Inscripcion()


def sqlform_grid():
    query = db(db.Inscripcion.pasantia == db.Pasantia.id)
    db.Estudiante._format = lambda row: row.carnet

    fields = [
        db.Pasantia.titulo,
        db.Pasantia.estudiante,
        db.Pasantia.materia,
        db.Pasantia.periodo,
        db.Inscripcion.estado,
    ]
    if not request.args:
        return simple_spe_grid(query, fields=fields, field_id=db.Inscripcion.id)
    elif request.args[-3] == 'edit':
        return modificar(request)
    else:
        return simple_spe_grid(query, fields=fields, field_id=db.Inscripcion.id)


@auth.requires(Usuario.checkUserPermission(construirAccion(request.application, request.controller)))
def listar():
    session.rows = []

    return locals()


@auth.requires(Usuario.checkUserPermission(construirAccion(request.application, request.controller)))
def agregar():
    form = SQLFORM(db.Inscripcion)

    if form.process().accepted:
        session.flash = T('La Inscripcion fue agregada exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()


@auth.requires(Usuario.checkUserPermission(construirAccion(request.application, request.controller)))
def count():
    obj = Encoder.to_dict(request.vars)
    count = Inscripcion.count(obj)

    return count


@auth.requires(Usuario.checkUserPermission(construirAccion(request.application, request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db((db.Inscripcion.pasantia == db.Pasantia.id) & (db.Pasantia.estudiante == db.Estudiante.id) & (
    db.Pasantia.id == db.Plan_Trabajo.pasantia)).select()

    # rows = Inscripcion.find(obj)

    # rows = rows.as_json()

    # print 'INICIO'
    # print db((db.Inscripcion.pasantia == db.Pasantia.id) & (db.Pasantia.estudiante == db.Estudiante.id)).select()
    # print '\n'
    # print rows
    return rows.as_json()


@auth.requires(Usuario.checkUserPermission(construirAccion(request.application, request.controller)))
def modificar(request):
    record = db.Inscripcion(request.args[-1]) or redirect(URL('agregar'))
    form = SQLFORM(db.Inscripcion, fields=['aprobacionCCT', 'comentarioCCT'], record=record, showid=False)
    if form.process().accepted:
        if request.vars.aprobacionCCT:
            pasantia = db.Pasantia(record.pasantia)
            etapa = db.Etapa(pasantia.etapa)
            existeEjecucion = db.Ejecucion(pasantia=record.pasantia)

            if not existeEjecucion:
                ejecucion = db.Ejecucion.insert(pasantia=record.pasantia)
                etapaInsc = db.Etapa(first_name='Ejecucion')
                pasantia.update_record(etapa=etapaInsc.id)
                record.update_record(estado='Aprobado')

        session.flash = T('La Inscripcion fue modificada exitosamente!')
        redirect(URL('sqlform_grid'))
    else:
        response.flash = T('Por favor llene la forma.')
    return form


@auth.requires(Usuario.checkUserPermission(construirAccion(request.application, request.controller)))
def create():
    return request.vars
