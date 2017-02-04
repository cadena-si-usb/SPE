# -*- coding: utf-8 -*-
from Acciones_Usuario import Accion_Usuario

import Encoder

Accion_Usuario = Accion_Usuario()
contextos = ['coordinacion', 'pasantias', 'catalogos', 'configuracion']

def sidebar():

    obj = Encoder.to_dict(request.vars)
    if (auth.is_logged_in()):
        usuario = auth.user
        roles = db(db.auth_membership.user_id == auth.user.id).select()
        roles_id = []
        accion = []
        sidebar = []
        for rol in roles:
            roles_id.append(rol.group_id)
            names = db(db.auth_group.id == rol.group_id.id).select(db.auth_group.role)

        for name in names:
            contextos_usuario = []
            # PROBAR: cuando haya un rol multiperfil
            for contexto in contextos:
                accion = db((db.Accion_Usuario.rol.belongs(roles_id)) & (db.Accion_Usuario.contexto ==
                                                                    contexto)).select(
                    orderby=db.Accion_Usuario.first_name)
                contextos_usuario.append({'contexto': contexto, 'acciones': accion})

            sidebar.append({'rol': name.role, 'contextos': contextos_usuario})

    response.view = 'sidebar/sidebar.html'
    return dict(sidebar=sidebar)

def coordinacion():
    if (auth.is_logged_in()):
        usuario = auth.user
        roles = db(db.auth_membership.user_id==auth.user.id).select()
        roles_id=[]
        for rol in roles:
            roles_id.append(rol.group_id)
        rows = db((db.Accion_Usuario.rol.belongs(roles_id)) & (db.Accion_Usuario.contexto ==
                                                            'coordinacion')).select(
            orderby=db.Accion_Usuario.first_name)

    response.view = 'sidebar/coordinacion.load.html'
    return dict(routes=rows, id="id")


def pasantias():
    rows = []
    obj = Encoder.to_dict(request.vars)

    # TODO Hacer que esto filtre dependiendo del rol del usuario logeado
    if (auth.is_logged_in()):
        usuario = auth.user
        roles = db(db.auth_membership.user_id==auth.user.id).select()
        roles_id=[]
        for rol in roles:
            roles_id.append(rol.group_id)
        rows = db((db.Accion_Usuario.rol.belongs(roles_id)) & (db.Accion_Usuario.contexto ==
                                                            'pasantias')).select(
            orderby=db.Accion_Usuario.first_name)

    response.view = 'sidebar/pasantias.load.html'
    return dict(routes=rows, id="id")


def catalogos():
    rows = []
    obj = Encoder.to_dict(request.vars)

    # TODO Hacer que esto filtre dependiendo del rol del usuario logeado
    if (auth.is_logged_in()):
        usuario = auth.user
        roles = db(db.auth_membership.user_id==auth.user.id).select()
        roles_id=[]
        for rol in roles:
            roles_id.append(rol.group_id)
        rows = db((db.Accion_Usuario.rol.belongs(roles_id)) & (db.Accion_Usuario.contexto ==
                                                            'catalogos')).select(
            orderby=db.Accion_Usuario.first_name)

    response.view = 'sidebar/catalogos.load.html'
    return dict(routes=rows, id="id")


def configuracion():
    rows = []
    obj = Encoder.to_dict(request.vars)

    # TODO Hacer que esto filtre dependiendo del rol del usuario logeado
    if (auth.is_logged_in()):
        usuario = auth.user
        roles = db(db.auth_membership.user_id==auth.user.id).select()
        roles_id=[]
        for rol in roles:
            roles_id.append(rol.group_id)
        rows = db((db.Accion_Usuario.rol.belongs(roles_id)) & (db.Accion_Usuario.contexto ==
                                                            'configuracion')).select(
            orderby=db.Accion_Usuario.first_name)
    response.view = 'sidebar/configuracion.load.html'
    return dict(routes=rows, id="id")
