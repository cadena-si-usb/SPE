# -*- coding: utf-8 -*-
from Curriculos import Curriculo

import Encoder

Curriculo = Curriculo()

# Verifica que se accedan a los recursos asignados al actor correspondiente 
def chequear_permisologia():
    try:
        userid = str(auth.user['username'])
        estudiante = db.Estudiante(db.Estudiante.carnet == userid)
        curriculo = db.Curriculo(db.Curriculo.estudiante == estudiante['id'])
    except Exception as e:
        return False

    return True

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows)

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar():
    fields = ['nombre']

    form = Curriculo.form(fields)

    if form.process().accepted:
        session.flash = T('El curriculo fue agregado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def count():
    obj = Encoder.to_dict(request.vars)
    count = Curriculo.count(obj)

    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = Curriculo.find(obj)

    rows = rows.as_json()

    return rows

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar():
    record = db.Curriculo(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Curriculo, record)
    if form.process().accepted:
        session.flash = T('El curriculo fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()


@auth.requires(chequear_permisologia())
def editar():
    response.view = 'curriculos/editar.load.html'

    fields = [
        'electivas',
        'cursos',
        'aficiones',
        'idiomas'         
    ]

    userid = str(auth.user['username'])

    estudiante = db.Estudiante(db.Estudiante.carnet == userid)

    curriculo = db.Curriculo(db.Curriculo.estudiante == estudiante['id'])

    form = SQLFORM(db.Curriculo,record=curriculo,fields=fields,submit_button='Actualizar',showid=False)

    if form.process().accepted:
        session.flash = T('Perfil actualizado exitosamente!')
        curriculo.update_record(activo=True)
    else:
        response.flash = T('Por favor llene la forma.')

    return dict(form=form)

@auth.requires(chequear_permisologia())
def ver():
    record = db.Curriculo(request.args(0))
    return locals()