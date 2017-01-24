# -*- coding: utf-8 -*-
from gluon import *


def Empresa_Table(db, T):
    db.define_table('Empresa',
                    Field('usuario', 'reference auth_user',
                          writable=False,
                          unique=True,
                          requires=[IS_NOT_EMPTY(error_message='Es necesario un email.'), IS_EMAIL
                          (error_message='Introduzca un email valido.')],
                          label='Usuario(*)'),
                    Field('area_laboral', 'reference Area_Laboral',
                          label='Area Laboral'),
                    Field('descripcion',
                          label='Descripcion'),
                    Field('direccion_web',  ##verificador de urls
                          label='Pagina Web'),
                    Field('contacto_RRHH',
                          label='Contactos De Recursos Humanos',
                          requires=[IS_NOT_EMPTY(error_message='Es necesario un email.'), IS_EMAIL
                          (error_message='Introduzca un email valido.')]),
                    format=lambda r: '%s %s' % (r.usuario.first_name, r.usuario.email))

    db.Empresa.usuario.requires = IS_IN_DB(
        db(db.auth_user.username == None),
        'auth_user.id', '%(tipo_documento)s-%(numero_documento)s : %(first_name)s %(last_name)s',
        zero='Seleccione un usuario', )

    if db(db.Empresa.id > 0).count() == 0:
        db.Empresa.insert(
            id='1',
            usuario='1',
            area_laboral='2',
            descripcion='Soluciones De Software',
            direccion_web='www.ecorp.com',
            contacto_RRHH='www.ecorp-rrhh@ecorp.com'
        )
        db.commit()
