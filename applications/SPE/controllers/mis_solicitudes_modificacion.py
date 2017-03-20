# -*- coding: utf-8 -*-
from Solicitud_Modificacion import Solicitud_Modificacion

import Encoder
from applications.SPE_lib.modules.grids import simple_spe_grid

@auth.requires(auth.is_logged_in() and auth.has_membership(role='Profesor'))
def consultar_solicitudes_modificacion_profesor():
    response.view = 'solicitud_modificacion/consultar_solicitudes_modificacion_profesor.html'
    return locals()

@auth.requires(auth.is_logged_in() and auth.has_membership(role='Profesor'))
def solicitudes_modificacion_grid_profesor():
    userId = auth.user.id
    profesor = db.Profesor(usuario=userId)
    email = auth.user.email
    query = (profesor.id == db.Pasantia.tutor_academico) & (db.Pasantia.id == db.Solicitud_Modificacion.pasantia)
    solicitudes = db(query)

    # Define the fields to show on grid. Note: (you need to specify id field in fields section in 1.99.2
    # this is not required in later versions)
    fields = [
        db.Solicitud_Modificacion.pasantia,
        db.Solicitud_Modificacion.aprobacion_tutor_academico,
        db.Solicitud_Modificacion.aprobacion_coordinacion_carrera,
        db.Solicitud_Modificacion.procesado_CCT
    ]

    # Define headers as tuples/dictionaries
    headers = {
        ''
        # 'Solicitud_Modificacion.pasantia': 'Titulo Pasantía',
        'Solicitud_Modificacion.aprobacion_tutor_academico': 'Aprobacion del Tutor Academico',
        'Solicitud_Modificacion.aprobacion_coordinacion_carrera': 'Aprobación de la Coordinacion de carrera',
        'Solicitud_Modificacion.procesado_CCT': 'Procesado por la CCT'
    }

    # Let's specify a default sort order on date_of_birth column in grid
    default_sort_order = [db.Pasantia.titulo]
    links = []

    # Creating the grid object
    form = SQLFORM.grid(query=solicitudes, fields=fields, headers=headers, orderby=default_sort_order,
                        create=False, deletable=False, editable=False, maxtextlength=64, paginate=25, details=False,
                        links=links, csv=False, user_signature=False)

    return form

@auth.requires(auth.is_logged_in() and auth.has_membership(role='Coordinador'))
def consultar_solicitudes_modificacion_coordinador():
    userId = auth.user.id
    coordinador = db.Coordinador(id=userId)
    coordinacion = db.Coordinacion(id=coordinador.coordinacion)
    response.view = 'solicitud_modificacion/consultar_solicitudes_modificacion_coordinador.html'
    return locals()

@auth.requires(auth.is_logged_in() and auth.has_membership(role='Coordinador'))
def solicitudes_modificacion_grid_coordinador():
    userId = auth.user.id
    coordinador = db.Coordinador(id=userId)
    coordinacion = db.Coordinacion(id=coordinador.coordinacion)
    carrera = db.Carrera(coordinacion=coordinacion)
    email = auth.user.email
    solicitudes = db((db.Estudiante.id == db.Pasantia.estudiante) & (db.Estudiante.carrera == carrera.id) & (db.Pasantia.id == db.Solicitud_Modificacion.pasantia))

    # Define the fields to show on grid. Note: (you need to specify id field in fields section in 1.99.2
    # this is not required in later versions)
    fields = [
        db.Solicitud_Modificacion.pasantia,
        db.Solicitud_Modificacion.aprobacion_tutor_academico,
        db.Solicitud_Modificacion.aprobacion_coordinacion_carrera,
        db.Solicitud_Modificacion.procesado_CCT
    ]

    # Define headers as tuples/dictionaries
    headers = {
        ''
        # 'Solicitud_Modificacion.pasantia': 'Titulo Pasantía',
        'Solicitud_Modificacion.aprobacion_tutor_academico': 'Aprobacion del Tutor Academico',
        'Solicitud_Modificacion.aprobacion_coordinacion_carrera': 'Aprobación de la Coordinacion de carrera',
        'Solicitud_Modificacion.procesado_CCT': 'Procesado por la CCT'
    }

    # Let's specify a default sort order on date_of_birth column in grid
    default_sort_order = [db.Pasantia.titulo]
    links = []

    # Creating the grid object
    form = SQLFORM.grid(query=solicitudes, fields=fields, headers=headers, orderby=default_sort_order,
                        create=False, deletable=False, editable=False, maxtextlength=64, paginate=25, details=False,
                        links=links, csv=False, user_signature=False)

    return form
