# -*- coding: utf-8 -*-
from Pasantias import Pasantia

import Encoder

Pasantia = Pasantia()

def listar():
    session.rows = []

    return dict(rows=session.rows)

def agregar():
    fields = ['nombre','empresa','tutor_industrial','tutor_academico','plan_trabajo','id_estudiante','materia']

    form = Pasantia.form(fields)

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
    count = Pasantia.count(obj)

    return count

def get():
    obj = Encoder.to_dict(request.vars)

    rows = Pasantia.JMaterias(obj)

    rows = rows.as_json()

    return rows

def ver():
    pasantia = db.Pasantia(request.args(0)) or redirect(URL('agregar'))
    etapa = db.Etapa(pasantia.etapa)

    response.view = 'mis_pasantias/' + etapa.nombre.lower() + '.html'
    
    return locals()


def editar():
    # Obtenemos la pasantia previamente agregada en inscripcion
    #area_proyecto = db.area_proyecto

    fields = [
        'titulo',
#        'area_proyecto',
        'resumen_proyecto',
        'objetivo',
        'confidencialidad'
    ]
    pasantia = db.Pasantia(request.args(0))

    # Cargamos el estudiante que ya esta enlazado a esta pasantia
    # db.Pasantia.estudiante.default = pasantia.estudiante['id']
    # db.Pasantia.estudiante.writable = False

    form = SQLFORM(db.Pasantia,record=pasantia,fields=fields,submit_button='Actualizar',showid=False)

    if form.process().accepted:
        session.flash = T('Pasantia actualizada exitosamente!')
        redirect(URL('editar'))
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()

    # form = SQLFORM.factory(
    #     *fields,
    #     submit_button='Submit',
    #     separator=': ',
    #     buttons=['submit'],
    #     col3={
    #         'titulo': T('Título'),
    #         'area_proyecto': T('Área del Proyecto'),
    #         'resumen_proyecto': T('Resumen del Proyecto'),
    #         'objetivo': T('Objetivo General'),
    #         'confidencialidad': T('Detalles de Confidencialidad'),
    #     }
    # )

    # if form.process().accepted:
    #     pasantia.update_record(
    #         titulo=request.vars.titulo,
    #         area_proyecto=request.vars.area_proyecto,
    #         objetivo=request.vars.objetivo,
    #         confidencialidad=request.vars.confidencialidad,
    #     )

    #     db.Plan_Trabajo.insert(
    #         pasantia=pasantia['id']
    #     )        


    # return locals()
    
# Nueva ruta    
def planes_trabajo():
    # Obtenemos la pasantia previamente agregada en inscripcion
    pasantia = db.Pasantia(request.args(0))

    return locals()
