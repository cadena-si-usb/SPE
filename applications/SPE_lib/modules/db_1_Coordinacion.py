# -*- coding: utf-8 -*-
from gluon import *
def Coordinacion_Table(db,T):
    # Actividad
    db.define_table('Coordinacion',
                    Field('first_name','string',required=True),
                    Field('username','string',required=True),
                    #Field('carrera', 'reference Carrera', label="Carrera", required=True),
                    Field('sede','reference Sede', label='Sedes (*)'),
                    format='%(first_name)s'
                   )

    db.Coordinacion.username.requires+=[IS_NOT_IN_DB(db, 'Coordinacion.username',error_message=T('Coordinacion ya registrado'))]

    if db(db.Coordinacion.id > 0).count() == 0:
        db.Coordinacion.insert(
            first_name='Computacion',
            username='1000',
            sede=1
        )
        db.Coordinacion.insert(
            first_name='Mecanica',
            username='1001',
            sede=1
        )
        db.Coordinacion.insert(
            first_name='Coordinación de Cooperación Tecnica',
            username='1002',
            sede=1
        )
        db.commit()