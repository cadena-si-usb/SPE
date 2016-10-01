# -*- coding: utf-8 -*-
from Acciones_Usuario import Accion_Usuario

import Encoder

Accion_Usuario = Accion_Usuario()

def coordinacion():
	rows = []
	obj = Encoder.to_dict(request.vars)

	#TODO Hacer que esto filtre dependiendo del rol del usuario logeado
	if ('currentUser' in session):
		usuario = session.currentUser

		if usuario['activo']:
			rol= db((db.auth_membership.user_id == auth.user.id)
						  & (db.auth_membership.group_id == db.auth_group.id)).select().first()
			rows = db((db.Accion_Usuario.rol == rol.auth_group.id) & (db.Accion_Usuario.contexto == 'coordinacion')).select()

	response.view = 'sidebar/coordinacion.load.html'
	return dict(routes=rows,id="id")

def configuracion():
	rows = []
	obj = Encoder.to_dict(request.vars)

	#TODO Hacer que esto filtre dependiendo del rol del usuario logeado
	if ('currentUser' in session):
		usuario = session.currentUser
		rol = db((db.auth_membership.user_id == auth.user.id)
				 & (db.auth_membership.group_id == db.auth_group.id)).select().first()
		rows = db((db.Accion_Usuario.rol == rol.auth_group.id) & (db.Accion_Usuario.contexto == 'configuracion')).select()

	response.view = 'sidebar/configuracion.load.html'
	return dict(routes=rows,id="id")