# -*- coding: utf-8 -*-
from gluon import *
from gluon.tools import Auth, Service, PluginManager, Mail


def spe_auth_tables(db, T):
    auth = Auth(db)

    auth.settings.extra_fields['auth_user'] = [
        Field('tipo_documento', 'reference Tipo_Documento',
              label='Tipo de Documento (*)'),
        Field('numero_documento',
              requires=[IS_MATCH('^[0-9][0-9]*$',
                                 error_message='Introduzca una cedula.')],
              label='Numero Documentacion (*)'),
        Field('telefono',
              requires=IS_MATCH('^\d{4}?[\s.-]?\d{7}$',
                                error_message='Numero no valido,ingrese numero telefonico'),
              comment='0212-111111',
              label='Telefono(*)'),
        Field('direccion', 'text',
              label='Direccion'),
        Field('sexo',
              requires=IS_IN_SET(['Masculino', 'Femenino']),
              label='Sexo (*)'),
        Field('activo', 'boolean'),
        Field('pregunta_secreta', 'text',
              requires=[IS_NOT_EMPTY
                        (error_message='Campo necesario')],
              label='Pregunta Secreta'),
        Field('respuesta_secreta', 'string',
              requires=[IS_NOT_EMPTY
                        (error_message='Campo necesario')],
              label='Respuesta Secreta'),
        Field('pais', 'reference Pais',
              label='Pais'),
        Field('estado', 'reference Estado',
              label='Estado'),
        Field('image', 'upload', uploadseparate=True, autodelete=True),
        Field('miembro_usb', 'boolean', writable=False, readable=False,
              default=True),
    ]

    return auth
