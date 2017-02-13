# -*- coding: utf-8 -*-
from gluon import *
def Estado_Table(db,T):
    db.define_table('Estado',
        Field('first_name','string', unique=True),
        Field('Pais', 'reference Pais'),
        format=lambda r: '%s - %s' % (r.Pais.first_name, r.first_name))

    if db(db.Estado.id > 0).count() == 0:
        db.Estado.insert(
            first_name='Amazonas',
            Pais=1
        )
        db.Estado.insert(
            first_name='Anzoátegui',
            Pais=1
        )
        db.Estado.insert(
            first_name='Apure',
            Pais=1
        )
        db.Estado.insert(
            first_name='Aragua',
            Pais=1
        )
        db.Estado.insert(
            first_name='Barinas',
            Pais=1
        )
        db.Estado.insert(
            first_name='Bolívar',
            Pais=1
        )
        db.Estado.insert(
            first_name='Carabobo',
            Pais=1
        )
        db.Estado.insert(
            first_name='Cojedes',
            Pais=1
        )
        db.Estado.insert(
            first_name='Delta Amacuro',
            Pais=1
        )
        db.Estado.insert(
            first_name='Distrito Capital',
            Pais=1
        )
        db.Estado.insert(
            first_name='Falcón',
            Pais=1
        )
        db.Estado.insert(
            first_name='Guárico',
            Pais=1
        )
        db.Estado.insert(
            first_name='Lara',
            Pais=1
        )
        db.Estado.insert(
            first_name='Mérida',
            Pais=1
        )
        db.Estado.insert(
            first_name='Miranda',
            Pais=1
        )
        db.Estado.insert(
            first_name='Monagas',
            Pais=1
        )
        db.Estado.insert(
            first_name='Nueva Esparta',
            Pais=1
        )
        db.Estado.insert(
            first_name='Portuguesa',
            Pais=1
        )
        db.Estado.insert(
            first_name='Sucre',
            Pais=1
        )
        db.Estado.insert(
            first_name='Tachira',
            Pais=1
        )
        db.Estado.insert(
            first_name='Trujillo',
            Pais=1
        )
        db.Estado.insert(
            first_name='Vargas',
            Pais=1
        )
        db.Estado.insert(
            first_name='Yaracuy',
            Pais=1
        )
        db.Estado.insert(
            first_name='Zulia',
            Pais=1
        )

        db.commit()
