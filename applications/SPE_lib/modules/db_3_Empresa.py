# -*- coding: utf-8 -*-
from gluon import *
def Empresa_Table(db,T):
    db.define_table('Empresa',
        Field('usuario', 'reference auth_user',
              requires=[IS_NOT_EMPTY(error_message='Es necesario un email.'),IS_EMAIL
                                   (error_message='Introduzca un email valido.') ],
              label='Email(*)'),
        Field('area_laboral','reference Area_Laboral',
              label = 'Area Laboral'),
        Field('descripcion',
              label='Descripcion'),
        Field('direccion_web',##verificador de urls
              label = 'Pagina Web'),
        Field('contacto_RRHH',
              label='Contactos De Recursos Humanos',requires=[IS_NOT_EMPTY(error_message='Es necesario un email.'),IS_EMAIL
                                   (error_message='Introduzca un email valido.')]),
        format=lambda r: '%s %s' % (r.usuario.first_name, r.usuario.email))
