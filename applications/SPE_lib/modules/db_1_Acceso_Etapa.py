# -*- coding: utf-8 -*-
from gluon import *
def Acceso_Etapa(db,T):
    db.define_table('Acceso_Etapa',
        Field('rol',
              'reference auth_group', '%(nombre)s',
              label='Rol (*)'),
        Field('etapa','reference Etapa',
              label='Etapas (*)'))