# -*- coding: utf-8 -*-
from Planes_Trabajo import Plan_Trabajo
from datetime import datetime

import Encoder

PlanTrabajo = Plan_Trabajo()

def listar():
    session.rows = []
    return dict(rows=session.rows)

def count():
    obj = Encoder.to_dict(request.vars)
    count = PlanTrabajo.count(obj)

    return count

# plan_trabajo/listar
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db((db.Plan_Trabajo.pasantia == db.Pasantia.id) & (db.Pasantia.estudiante == db.Estudiante.id)).select()

    return rows.as_json()

# plan_trabajo/modificar
# Cambiar vistas para que tengan 
def modificar():
    record = db.Plan_Trabajo(request.args(0)) or redirect(URL('agregar'))

    if record.estado == 'Enviado':
        redirect(URL(f='ver',args=record.id))

    pasantia = db.Pasantia(record.pasantia)

    fields = ['tutor_academico','titulo','resumen_proyecto','objetivo','area_proyecto']

    form = SQLFORM(db.Pasantia, fields=fields, record=pasantia, showid=False)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL(c='mis_pasantias',f='ver',args=pasantia.id))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()


# Crear endpoint mis_pasantias/plan_trabajo/:id
# Crear Modelo de objetivos especificos
# Modelo de actividades


def ver():
    record = db.Plan_Trabajo(request.args(0))

    pasantia = db((db.Pasantia.id == record.pasantia) & (db.Pasantia.area_proyecto == db.Area_Proyecto.id)).select().first()

    return locals()

def enviar():
    plan_trabajo = db.Plan_Trabajo(request.args(0))

    plan_trabajo.update_record(estado="Enviado",fecha_envio=datetime.now())

    redirect(URL(c='mis_pasantias',f='ver',args=plan_trabajo.pasantia))