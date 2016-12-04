# -*- coding: utf-8 -*-
from gluon import *
def Coordinacion_Table(db,T):
    # Actividad
    db.define_table('Coordinacion',
                    Field('first_name','string',required=True),
                    Field('usbid','string',required=True),
                    #Field('carrera', 'reference Carrera', label="Carrera", required=True),
                    Field('sede','reference Sede', label='Sedes (*)'),
                    format='%(first_name)s'
                   )

    db.Coordinacion.usbid.requires+=[IS_NOT_IN_DB(db, 'Coordinacion.usbid',error_message=T('Coordinacion ya registrado'))]
