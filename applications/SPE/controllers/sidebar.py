# -*- coding: utf-8 -*-
from Acciones_Usuario import Accion_Usuario

import Encoder

Accion_Usuario = Accion_Usuario()

def items():
	rows = []
	obj = Encoder.to_dict(request.vars)

	#TODO Hacer que esto filtre dependiendo del rol del usuario logeado
	if ('currentUser' in session):
		usuario = session.currentUser
		if usuario['activo']:
			obj['filter'] = '{"rol":"' + str(usuario['rol']) + '"}'
			rows = Accion_Usuario.find(obj).as_list()

	response.view = 'sidebar/items.load.html'
	return dict(routes=rows,id="id")