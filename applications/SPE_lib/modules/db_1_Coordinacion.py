# -*- coding: utf-8 -*-
from gluon import *
def Coordinacion(db,T):
    # Actividad
    db.define_table('Coordinacion',
                    Field('nombre','string',required=True),
                    Field('usbid','string',required=True),
                    Field('sede','reference Sede', label='Sedes (*)'),
                    format='%(nombre)s'
                   )

    db.Coordinacion.usbid.requires+=[IS_NOT_IN_DB(db, 'Coordinacion.usbid',error_message=T('Coordinacion ya registrado'))]
