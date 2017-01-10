# -*- coding: utf-8 -*-
from gluon import *
def Coordinador_Table(db,T):
    db.define_table('Coordinador',
                    Field('usuario','reference auth_user',
                          label='Usuario (*)'),
                    Field('carnet',
                          requires=IS_MATCH('^\d{2}?[\s.-]?\d{5}$',
                                            error_message='Introduzca un carnet valido.'),
                          label='Carnet'),
                    Field('coordinacion','reference Coordinacion',
                          label='Coordinacion (*)'),
                    Field('correo_Alternativo',  requires=IS_EMAIL(error_message='Introduzca un email valido.'),
                          label='Correo Alternativo'),
                    format = lambda r: '%s - %s %s' % (r.usuario.username, r.usuario.first_name, r.usuario.last_name))

    db.Coordinador.usuario.requires = IS_IN_DB(
        db(db.auth_user.username != None),
        'auth_user.id', '%(username)s - %(first_name)s %(last_name)s',
        zero='Seleccione un usuario USB',)
