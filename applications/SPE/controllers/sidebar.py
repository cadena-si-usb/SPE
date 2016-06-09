# -*- coding: utf-8 -*-
from Acciones_Usuario import Accion_Usuario

import Encoder

Accion_Usuario = Accion_Usuario()

def items():
    obj = Encoder.to_dict(request.vars)

    #TODO Hacer que esto filtre dependiendo del rol del usuario logeado
    if ('currentUser' in session):
        usuario = session.currentUser
        if usuario['activo']:
        	obj['filter'] = '{"rol":"' + str(usuario['rol']) + '"}'
    		rows = Accion_Usuario.find(obj).as_list()
    	else:
    		rows = []
        	



    response.view = 'sidebar/items.load.html'
    return dict(routes=rows,id="id")