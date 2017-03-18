# -*- coding: utf-8 -*-
from Solicitud_Modificacion import Solicitud_Modificacion

import Encoder
from applications.SPE_lib.modules.grids import simple_spe_grid
Solicitud_Modificacion = Solicitud_Modificacion()

def sqlform_grid():
    sqlform_grid = simple_spe_grid(db.Solicitud_Modificacion)
    return sqlform_grid

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar():

    currentRoles = current.auth.user_groups.values()
    etapa = db(db.Etapa.nombre == 'Ejecucion').select().first()

    fields = ['pasantia','justificacion', 'cambios_solicitados', 'aprobacion_tutor_academico', 'aprobacion_coordinacion_carrera', 'procesado_CCT']

    if 'Estudiante' in currentRoles:
        estudiante = db.Estudiante(usuario=auth.user.id)
        pasantia_id = request.args[0]
        db.Solicitud_Modificacion.pasantia.default = pasantia_id

        form = SQLFORM(db.Solicitud_Modificacion, pasantia, showid=False)

    if form.process().accepted:
        session.flash = T('La solicitud fue procesada exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')
    response.view = 'solicitud_modificacion/solicitar_modificacion.html'
    return locals()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows)

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def count():
    obj = Encoder.to_dict(request.vars)
    count = Solicitud_Modificacion.count(obj)

    return count
