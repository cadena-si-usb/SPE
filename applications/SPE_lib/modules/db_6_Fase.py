# -*- coding: utf-8 -*-
from gluon import *
def Fase(db,T):
    db.define_table('Fase',
        Field('numero','integer',
              requires=[IS_NOT_EMPTY
                            (error_message='Es necesario un numero de identificacion')],
              label = 'Numero'),
        Field('plan_trabajo', 'reference Plan_Trabajo',
              label='Pasantía (*)'),
        Field('descripcion','text',
              requires=[IS_NOT_EMPTY
                            (error_message='Es necesario una Descripcion')],
              label = 'Descripcón'),
        format=lambda r: 'Fase "%s" De La Pasantia "%s"' % (r.numero,r.plan_trabajo.pasantia.titulo)
    )