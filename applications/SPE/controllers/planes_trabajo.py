# -*- coding: utf-8 -*-
from Planes_Trabajo import Plan_Trabajo

import Encoder

PlanTrabajo = Plan_Trabajo()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows)

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar():
    form =SQLFORM(db.Plan_Trabajo)

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
    count = PlanTrabajo.count(obj)

    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = PlanTrabajo.find(obj)

    rows = rows.as_json()

    return rows

# plan_trabajo/modificar
# Cambiar vistas para que tengan
@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar():
    record = db.Plan_Trabajo(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Plan_Trabajo, record)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()


# Crear endpoint mis_pasantias/plan_trabajo/:id
# Crear Modelo de objetivos especificos
# Modelo de actividades
@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def ver():
    record = db.Plan_Trabajo(request.args(0))

    return locals()