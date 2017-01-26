# -*- coding: utf-8 -*-
from gluon import *


def Coordinacion_Table(db, T):
    # Actividad
    db.define_table('Coordinacion',
                    Field('nombre', 'string', required=True),
                    Field('codigo', 'string', required=True),
                    # Field('carrera', 'reference Carrera', label="Carrera", required=True),
                    Field('sede', 'reference Sede', label='Sedes (*)'),
                    format='%(nombre)s'
                    )

    if db(db.Coordinacion.id > 0).count() == 0:
        db.Coordinacion.insert(
            nombre='Computacion',
            codigo='1000',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Mecanica',
            codigo='1001',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Coordinación de Cooperación Tecnica',
            codigo='1002',
            sede=1
        )
        db.commit()
