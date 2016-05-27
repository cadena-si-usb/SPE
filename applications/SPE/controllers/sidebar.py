# -*- coding: utf-8 -*-
from Acciones_Usuario import Accion_Usuario

import Encoder

Accion_Usuario = Accion_Usuario()

def items():
    obj = Encoder.to_dict(request.vars)

    #TODO Hacer que esto filtre dependiendo del rol del usuario logeado
    #obj['filter'] = '{"rol":"1"}'
    if (session.currentUser['tipo'] == "Pregrado"):
    	rol = "Estudiante"
    else:
    	rol = "CCT"

    rows = Accion_Usuario.find(obj)

    response.view = 'sidebar/items.load.html'
    return dict(routes=rows.as_list(),id="id",rol=rol)