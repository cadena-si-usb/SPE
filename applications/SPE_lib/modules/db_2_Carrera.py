# -*- coding: utf-8 -*-
from gluon import *
def Carrera_Table(db,T):
    # Estudiante
    db.define_table('Carrera',
                    Field('codigo','string',
                          required=True,
                          ondelete='CASCADE',
                          notnull=True,
                          label='Código'),
                    Field('first_name','string',required=True, requires=[IS_LENGTH(100)], label='Nombre'),
                    Field('duracion','string',required=True, requires=IS_IN_SET(['Larga','Corta']), label="Duración", notnull=True),
                    Field('coordinacion','reference Coordinacion', label="Coordinación", required=True),
                    format='%(codigo)s %(first_name)s'
                   )
    db.Carrera.codigo.requires = [IS_LENGTH(4)
            ,IS_NOT_EMPTY(error_message='Campo Obligatorio')
            ,IS_NOT_IN_DB(db, 'Carrera.codigo',error_message=T('Carrera ya existe'))
            ,IS_MATCH('[0-9]{4}',error_message=T('Solo se permiten numeros de cuatro digitos'))]

    if db(db.Carrera.id > 0).count() == 0:
        db.Carrera.insert(
            first_name='Ingenieria de la Computacion',
            codigo='0800',
            duracion='Larga',
            coordinacion=1
        )
        db.Carrera.insert(
            first_name='Ingenieria de Mecanica',
            codigo='0200',
            duracion='Larga',
            coordinacion=1
        )
        db.commit()