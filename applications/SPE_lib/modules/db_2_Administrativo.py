# -*- coding: utf-8 -*-
from gluon import *


def Administrativo_Table(db, T):
    db.define_table('Administrativo',
                    Field('usuario', 'reference auth_user',
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
                          label='Correo Alternativo'))

    db.Administrativo.usuario.requires = IS_IN_DB(
        db(db.auth_user.miembro_usb == True),
        'auth_user.id', db.auth_user._format,
        zero='Seleccione un usuario USB', )

    if db(db.Administrativo.id > 0).count() == 0:
        db.Administrativo.insert(
            usuario='11',
            carnet='09-10066',
            coordinacion='3',
            correo_Alternativo='gmailaustin@gmail.com'
        )
        db.commit()
