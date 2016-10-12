# -*- coding: utf-8 -*-
from gluon import *
def Acceso_Etapa_Table(db,T):
    db.define_table('Acceso_Etapa',
        Field('rol',
              'reference auth_group', '%(role)s',
              label='Rol (*)'),
        Field('etapa','reference Etapa',
              label='Etapas (*)'))