# -*- coding: utf-8 -*-
from gluon import *


def Coordinador_Table(db, T):
    db.define_table('Coordinador',
                    Field('usuario', 'reference auth_user',
                          writable=False,
                          unique=True,
                          label='Usuario (*)'),
                    Field('carnet',
                          requires=IS_MATCH('^\d{2}?[\s.-]?\d{5}$',
                                            error_message='Introduzca un carnet valido.'),
                          label='Carnet',
                          unique=True,
                          required=True,
                          ),
                    Field('coordinacion', 'reference Coordinacion',
                          label='Coordinacion (*)'),
                    Field('correo_Alternativo', requires=IS_EMAIL(error_message='Introduzca un email valido.'),
                          label='Correo Alternativo'),
                    format=lambda r: '%s - %s %s' % (r.usuario.username, r.usuario.first_name, r.usuario.last_name))

    db.Coordinador.usuario.requires = IS_IN_DB(
        db(db.auth_user.miembro_usb == True),
        'auth_user.id', db.auth_user._format,
        zero='Seleccione un usuario USB', )

    if db(db.Coordinador.id > 0).count() == 0:
        db.Coordinador.insert(
            id='6',
            usuario='6',
            carnet='10-10330',
            coordinacion='3',
            correo_Alternativo='danielarturomt@gmail.com'
        )
        db.Coordinador.insert(
            id='8',
            usuario='8',
            carnet='10-10193',
            coordinacion='1',
            correo_Alternativo='coord@copt.com'
        )
        db.Coordinador.insert(
            id='9',
            usuario='9',
            carnet='10-10292',
            coordinacion='2',
            correo_Alternativo='asd@asd.com'
        )
        db.commit()
