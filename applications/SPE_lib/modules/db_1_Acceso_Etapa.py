# -*- coding: utf-8 -*-
from gluon import *
def Acceso_Etapa_Table(db,T):
    db.define_table('Acceso_Etapa',
        Field('rol',
              'reference auth_group', '%(role)s',
              label='Rol (*)'),
        Field('etapa','reference Etapa',
              label='Etapas (*)'))

    if db(db.Acceso_Etapa.id > 0).count() == 0:
        db.Acceso_Etapa.insert(
            rol=3,
            etapa=3
        )
        db.Acceso_Etapa.insert(
            rol=6,
            etapa=2
        )
        db.Acceso_Etapa.insert(
            rol=6,
            etapa=4
        )
        db.Acceso_Etapa.insert(
            rol=6,
            etapa=3
        )
        db.Acceso_Etapa.insert(
            rol=6,
            etapa=1
        )
        db.commit()