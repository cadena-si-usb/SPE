# -*- coding: utf-8 -*-
from Acceso_Etapa import Acceso_Etapa
from Usuarios import Usuario
import Encoder

Acceso_Etapa = Acceso_Etapa()
Usuario = Usuario()

@auth.requires(Usuario.checkUserPermission('/'+request.application+'/'+request.controller+'/'+'listar'))
def listar():
    session.rows = []
    return dict(rows=session.rows,id="prueba")
@auth.requires(Usuario.checkUserPermission('/'+request.application+'/'+request.controller+'/'+'listar'))
def agregar():
    fields = ['rol','etapa']

    form = Acceso_Etapa.form(fields)

    if form.process().accepted:
        session.flash = T('El material fue agregado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()
@auth.requires(Usuario.checkUserPermission('/'+request.application+'/'+request.controller+'/'+'listar'))
def count():
    obj = Encoder.to_dict(request.vars)
    count = Acceso_Etapa.count(obj)

    return count
@auth.requires(Usuario.checkUserPermission('/'+request.application+'/'+request.controller+'/'+'listar'))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db(
        (db.Acceso_Etapa.rol == db.auth_group.id) & (db.Etapa.id == db.Acceso_Etapa.etapa)).select(
        orderby=db.auth_group.role)

    # rows = Acceso_Etapa.find(obj)

    rows = rows.as_json()

    return rows
@auth.requires(Usuario.checkUserPermission('/'+request.application+'/'+request.controller+'/'+'listar'))
def modificar():
    record = db.Acceso_Etapa(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Acceso_Etapa, record,showid=False)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()
