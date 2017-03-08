# -*- coding: utf-8 -*-
from gluon import *
from datetime import datetime
def Viatico_Table(db,T):
    db.define_table('Viatico',
    	# Arreglar y poner a funcionar con el permiso correspondiente
    	Field('pasantia', 'Reference Pasantia'),
        #Field('permiso','reference Permisos', label='Permiso (*)'),
        Field('fecha_creacion','datetime',default=datetime.now(),
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('fecha_envio','datetime',
              represent=lambda v, r: 'N/A' if v is None else v),
    )
