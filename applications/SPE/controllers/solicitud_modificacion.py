# -*- coding: utf-8 -*-
from Solicitud_Modificacion import Solicitud_Modificacion

import Encoder
from applications.SPE_lib.modules.grids import simple_spe_grid
Solicitud_Modificacion = Solicitud_Modificacion()

def sqlform_grid():
    sqlform_grid = simple_spe_grid(db.Solicitud_Modificacion)
    return sqlform_grid

def agregar():

    currentRoles = current.auth.user_groups.values()

    # fields = ['pasantia','justificacion', 'cambios_solicitados', 'aprobacion_tutor_academico', 'aprobacion_coordinacion_carrera', 'procesado_CCT']
    fields = ['pasantia','justificacion', 'cambios_solicitados']

    if 'Estudiante' in currentRoles:
        estudiante = db.Estudiante(usuario=auth.user.id)
        pasantia_id = request.args[0]
        db.Solicitud_Modificacion.pasantia.default = pasantia_id
        db.Solicitud_Modificacion.pasantia.writable = False

        form = Solicitud_Modificacion.form(fields)

    if form.process().accepted:
        session.flash = T('La solicitud fue procesada exitosamente!')
        # print(response.vars)
        redirect(URL('ver', args=[form.vars.id]))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')
    response.view = 'solicitud_modificacion/solicitar_modificacion.html'
    return locals()

def listar():
    session.rows = []
    return dict(rows=session.rows)

def count():
    obj = Encoder.to_dict(request.vars)
    query = "db.Estudiante"
    if 'searchTerm' in obj and obj['searchTerm'] != '{}':
        query = dict()
        search = ast.literal_eval(obj['searchTerm'])
        query = "db.Estudiante.carnet.startswith('" + search["value"] + "')"

    count = db(eval(query) & (db.Pasantia.estudiante == db.Estudiante.id)).count()
    return count

def modificar():

    currentRoles = current.auth.user_groups.values()
    record = (db.Solicitud_Modificacion(request.args(0)) or redirect(URL('agregar')))

    if 'Estudiante' in currentRoles:
        fields = ['justificacion', 'cambios_solicitados']
        form = SQLFORM(db.Solicitud_Modificacion,record,fields=fields,showid=False)
    if 'Profesor' in currentRoles:
        fields = ['aprobacion_tutor_academico']
        form = SQLFORM(db.Solicitud_Modificacion,record,fields=fields,showid=False)
    elif 'Coordinador' in currentRoles:
        fields = ['aprobacion_coordinacion_carrera']
        form = SQLFORM(db.Solicitud_Modificacion,record,fields=fields,showid=False)
    elif 'CoordinadorCCT' in currentRoles:
        fields = ['procesado_CCT']
        form = SQLFORM(db.Solicitud_Modificacion,record,fields=fields,showid=False)
    else:
        redirect(URL(c='default', f='index'))

    if form.process().accepted:
        session.flash = T('El material fue agregado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()

def ver():
    print(request.args(0))
    solicitud = db.Solicitud_Modificacion(request.args(0)) or redirect(URL('agregar'))
    response.view = 'solicitud_modificacion/ver.html'
    return locals()
