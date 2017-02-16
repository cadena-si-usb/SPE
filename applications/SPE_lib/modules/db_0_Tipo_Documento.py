# -*- coding: utf-8 -*-
from gluon import *


def Tipo_Documento_Table(db, T):
    db.define_table('Tipo_Documento',
                    Field('first_name', 'string',
                          label='Nombre', unique=True),
                    format='%(first_name)s'
                    )

    if db(db.Tipo_Documento.id > 0).count() == 0:
        db.Tipo_Documento.insert(
            first_name='Cedula'
        )
        db.Tipo_Documento.insert(
            first_name='Pasaporte'
        )
        db.Tipo_Documento.insert(
            first_name='RIF'
        )
        db.commit()
