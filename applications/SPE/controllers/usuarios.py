# -*- coding: utf-8 -*-
from Usuarios import Usuario
from Carreras import Carrera
from Sedes import Sede
from Tipos_Documento import Tipo_Documento

import json
import Encoder
from applications.SPE_lib.modules.grids import single_table_spe_grid
Usuario = Usuario()
Carrera = Carrera()
Sede = Sede()
Tipo_Documento = Tipo_Documento()

def sqlform_grid():
    sqlform_grid = single_table_spe_grid(db.auth_user)
    return sqlform_grid

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows)

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar():
   # fields = ['id','first_name','last_name','ci']

    form = SQLFORM(db.auth_user)

    if form.process().accepted:
        session.flash = T('El usuario fue agregado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def count():
    obj = Encoder.to_dict(request.vars)
    count = Usuario.count(obj)

    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db(
        (db.auth_membership.user_id == db.auth_user.id) & (db.auth_membership.group_id == db.auth_group.id)).select()
    prueba=rows.as_json()
    return rows.as_json()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar():
    record = db.auth_user(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.auth_user,fields=['activo'], record=record, showid=False)
    
    if form.process().accepted:
        session.flash = T('El usuario fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    
    return locals()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def getCurrentUser():
    if not 'currentUser' in session:
        return json.dumps([])

    user = {}

    user['datos'] = session.currentUser.as_dict()

    if auth.has_membership(role='Estudiante'):
        estudiante = db(db.Estudiante.usuario == session.currentUser.id).select().first()
        user['estudiante'] = estudiante.as_dict()

    return json.dumps(user)
