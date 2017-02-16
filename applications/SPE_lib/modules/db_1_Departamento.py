# -*- coding: utf-8 -*-
from gluon import *


def Departamento_Table(db, T):
    # Departamento
    db.define_table('Departamento',
                    Field('first_name', 'string', requires=IS_NOT_EMPTY(), default='', unique=True,
                          label="Nombre del Departamento"),
                    Field('id_division', 'reference Division', notnull=True, label='Nombre de División'),
                    Field('usb_id', 'string', unique=True), #required?
                    Field('email_dep', 'string', label='Correo Electrónico del Departamento'),
                    Field('sede', 'reference Sede'))

    # Validadores
    db.Departamento.email_dep.requires = [IS_EMAIL(error_message=T('Este no es un email valido'))]
    db.Departamento.email_dep.requires += [IS_LENGTH(100)]
    db.Departamento.email_dep.requires += [IS_NOT_EMPTY(error_message='Campo Obligatorio')]

    if db(db.Departamento.id > 0).count() == 0:
        db.Departamento.insert(
            first_name='Ciencias de los Materiales',
            id_division='1',
            usb_id='dep-mt',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Ciencias de la Tierra',
            id_division='1',
            usb_id='dep-gc',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Computación y Tecnología de la Información',
            id_division='1',
            usb_id='dep-ci',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Conversión y Transporte de Energía',
            id_division='1',
            usb_id='dep-ct',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Electrónica y Circuitos',
            id_division='1',
            usb_id='usb-ec',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Mecánica',
            id_division='1',
            usb_id='dep-mc',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Procesos y Sistemas',
            id_division='1',
            usb_id='dep-ps',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Tecnología de Procesos Biológicos y Bioquímicos',
            id_division='2',
            usb_id='depto-pb',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Termodinámica y Fenómenos de Transferencia',
            id_division='1',
            usb_id='teryfem',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Biología Celular',
            id_division='2',
            usb_id='dep-bc',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Biología de Organismos',
            id_division='2',
            usb_id='dep-bo',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Cómputo Científico y Estadística',
            id_division='1',
            usb_id='dep-co',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Estudios Ambientales',
            id_division='2',
            usb_id='dep-ea',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Física',
            id_division='1',
            usb_id='dep-fs',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Matemáticas Puras y Aplicadas',
            id_division='1',
            usb_id='jefemat',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Química',
            id_division='1',
            usb_id='dep-qm',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Ciencias Económicas y Administrativas',
            id_division='3',
            usb_id='dep-ce',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Ciencias Sociales',
            id_division='3',
            usb_id='dep-cs',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Ciencia y Tecnología del Comportamiento',
            id_division='3',
            usb_id='dep-cc',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Diseño, Arquitectura y Artes Plásticas',
            id_division='3',
            usb_id='dpto-da',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Filosofía',
            id_division='3',
            usb_id='dep-filo',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Idiomas',
            id_division='3',
            usb_id='dep-id',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Lengua y Literatura',
            id_division='3',
            usb_id='dep-ll',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Planificación Urbana',
            id_division='3',
            usb_id='dep-pl',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.Departamento.insert(
            first_name='Profesional externo a la USB (INTERNACIONAL)',
            id_division='4',
            usb_id='',
            email_dep='ci@usb.ve',
            sede='1', #INTERNACIONAL
        )
        db.Departamento.insert(
            first_name='Tecnología Industrial',
            id_division='5',
            usb_id='sdl-dti',
            email_dep='ci@usb.ve',
            sede='2',
        )
        db.Departamento.insert(
            first_name='Formación General y Ciencias Básicas',
            id_division='5',
            usb_id='dpto-fgcb',
            email_dep='ci@usb.ve',
            sede='2',
        )
        db.Departamento.insert(
            first_name='Tecnología de Servicios',
            id_division='5',
            usb_id='dep-tsmt',
            email_dep='ci@usb.ve',
            sede='2',
        )
        db.Departamento.insert(
            first_name='Profesional externo a la USB (en VENEZUELA)',
            id_division='1',
            usb_id='-',
            email_dep='ci@usb.ve',
            sede='1', #VENEZUELA
        )
        db.commit()
