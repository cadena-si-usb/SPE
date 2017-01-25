# -*- coding: utf-8 -*-
from Colocaciones import Colocacion

import Encoder
from applications.SPE_lib.modules.grids import simple_spe_grid
Colocacion = Colocacion()

def sqlform_grid():
    if not request.args:
        return simple_spe_grid(db.Colocacion)
    elif request.args[-3]=='edit':
        return modificar(request)
    else:
        return simple_spe_grid(db.Colocacion)

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []

    return locals()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
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

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def count():
    obj = Encoder.to_dict(request.vars)
    count = Colocacion.count(obj)

    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db((db.Colocacion.pasantia == db.Pasantia.id) & (db.Pasantia.estudiante == db.Estudiante.id) & (db.Estudiante.carrera == db.Carrera.id)).select()

    return rows.as_json()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar(request):
    record = db.Colocacion(request.args[-1]) or redirect(URL('agregar'))

    pasantia = db.Pasantia(record.pasantia)
    etapaInsc = db.Etapa(first_name='Inscripcion')

    db.Colocacion.id.default = record.id
    db.Colocacion.pasantia.default = record.pasantia
    db.Colocacion.aprobacionCCT.default = record.aprobacionCCT
    db.Colocacion.comentarioCCT.default = record.comentarioCCT
    db.Colocacion.estado.default = record.estado
    db.Colocacion.fecha_creacion.default = record.fecha_creacion

    db.Pasantia.titulo.default = pasantia.titulo
    db.Pasantia.estudiante.default = pasantia.estudiante
    db.Pasantia.tutor_academico.default = pasantia.tutor_academico
    db.Pasantia.tutor_industrial.default = pasantia.tutor_industrial
    db.Pasantia.periodo.default = pasantia.periodo
    db.Pasantia.area_proyecto.default = pasantia.area_proyecto
    db.Pasantia.resumen_proyecto.default = pasantia.resumen_proyecto
    db.Pasantia.materia.default = pasantia.materia
    db.Pasantia.objetivo.default = pasantia.objetivo
    db.Pasantia.confidencialidad.default = pasantia.confidencialidad
    db.Pasantia.status.default = pasantia.status
    db.Pasantia.etapa.default = pasantia.etapa
    db.Pasantia.fecha_creacion.default = pasantia.fecha_creacion
    db.Pasantia.fecha_creacion.readable = False
    db.Pasantia.fecha_creacion.writable = False
    db.Pasantia.fecha_inicio.default = pasantia.fecha_inicio
    db.Pasantia.fecha_fin.default = pasantia.fecha_fin
    db.Pasantia.fecha_tope_jurado.default = pasantia.fecha_tope_jurado
    db.Pasantia.fecha_defensa.default = pasantia.fecha_defensa
    
    db.Colocacion.pasantia.readable = False
    db.Colocacion.pasantia.writable = False

    form = SQLFORM.factory(db.Pasantia,db.Colocacion, submit_button='Actualizar', showid=False)

    if form.process().accepted:
        # Actualizo los datos de la pasantia
        pasantia.update_record(**db.Pasantia._filter_fields(form.vars))
        # Actualizo los datos exclusivos de estudiante
        record.update_record(**db.Colocacion._filter_fields(form.vars))

        if request.vars.aprobacionCCT:
            existeInscripcion = db.Inscripcion(pasantia=record.pasantia)
            if not existeInscripcion:
                inscripcion = db.Inscripcion.insert(pasantia=record.pasantia)
                plan_trabajo = db.Plan_Trabajo.insert(pasantia=record.pasantia)

                pasantia = db.Pasantia(record.pasantia)
                etapaInsc = db(db.Etapa.first_name == 'Inscripcion').select().first()
                pasantia.update_record(etapa=etapaInsc.id)

                record.update_record(estado='Aprobado')

        session.flash = T('Perfil actualizado exitosamente!')
        redirect(URL('sqlform_grid'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return form

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def create():
    return request.vars
