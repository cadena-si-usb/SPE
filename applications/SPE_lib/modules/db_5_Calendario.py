# -*- coding: utf-8 -*-
from gluon import *
from datetime import datetime
def Calendario_Table(db,T):
    db.define_table('Calendario',
    	Field('permiso', 'string'),
        #Field('permiso','reference Permisos', label='Permiso (*)'),
        Field('fecha_creacion','datetime',default=datetime.now(),
              represent=lambda v, r: 'N/A' if v is None else v),
        Field('fecha_envio','datetime',
              represent=lambda v, r: 'N/A' if v is None else v),
    )
