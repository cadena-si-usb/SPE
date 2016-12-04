# -*- coding: utf-8 -*-
from gluon import *
def UsuarioExterno_Table(db,T):
    db.define_table('UsuarioExterno',
                    Field('auth_User', 'reference auth_user'),
                    Field('first_name',
                           requires=[IS_NOT_EMPTY
                                        (error_message='Es necesario un first_name.') ],
                           label='Nombre'),
                    Field('email',
                           requires=[IS_EMPTY_OR(IS_EMAIL
                                                (error_message='Introduzca un email valido.'))],
                           label='Correo'),
                    Field('pregunta_secreta', 'text',
                           requires=[IS_NOT_EMPTY
                                        (error_message='Campo necesario')],
                           label='Pregunta Secreta'),
                    Field('respuesta_secreta','string',
                           requires=[IS_NOT_EMPTY
                                        (error_message='Campo necesario')],
                           label='Respuesta Secreta'),
                    Field('pais','reference Pais',
                           label= 'Pais'),
                    Field('estado','reference Estado',
                           label= 'Estado'),
                    Field('telefono',
                           requires=IS_MATCH('^\d{4}?[\s.-]?\d{7}$',error_message='Numero no valido,ingrese numero telefonico'),
                           label = 'Telefono'),
                    Field('direccion','text',
                           requires=[IS_NOT_EMPTY
                                        (error_message='Direccion necesaria')],
                           label='Direccion'),
                    format='%(first_name)s - %(email)s'
    )


    db.auth_user.email.requires+=[IS_NOT_IN_DB(db, 'auth_user.email',error_message=T('Correo No Disponible'))]