# -*- coding: utf-8 -*-
from gluon import *


def Area_Proyecto_Table(db, T):
    db.define_table('Area_Proyecto',
                    Field('first_name', 'string', required=True, ondelete='CASCADE',
                          notnull=True, label='Área del Proyecto', unique=True),
                    Field('descripcion', 'text', required=True, notnull=True,
                          label=T('Descripcion del Area del Proyecto')),
                    format='%(first_name)s', migrate="Area_Proyecto.table")

    db.Area_Proyecto.first_name.requires = [IS_NOT_EMPTY(error_message='Campo Obligatorio')]
    db.Area_Proyecto.first_name.requires += [IS_LENGTH(512)]
    db.Area_Proyecto.first_name.requires += [
        IS_NOT_IN_DB(db, 'Area_Proyecto.first_name', error_message=T('Area de Proyecto ya registrada'))]

    if db(db.Area_Proyecto.id > 0).count() == 0:
        db.Area_Proyecto.insert(
            first_name='Informatica Forense',
            descripcion=''
        )
        db.Area_Proyecto.insert(
            first_name='Sistema De Informacion',
            descripcion=''
        )
        db.commit()
