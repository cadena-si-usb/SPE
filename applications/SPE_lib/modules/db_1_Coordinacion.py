# -*- coding: utf-8 -*-
from gluon import *


def Coordinacion_Table(db, T):
    # Actividad
    db.define_table('Coordinacion',
                    Field('nombre', 'string', required=True),
                    Field('usb_id', 'string', required=True, unique=True),
                    # Field('carrera', 'reference Carrera', label="Carrera", required=True),
                    Field('sede', 'reference Sede', label='Sedes (*)'),
                    format='%(nombre)s'
                    )

    if db(db.Coordinacion.id > 0).count() == 0:
        db.Coordinacion.insert(
            nombre='Coordinación de Cooperación Tecnica',
            usb_id='1000', #no sale en el archivo
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Administración Aduanera',
            usb_id='coord-aduanera',
            sede=2
        )
        db.Coordinacion.insert(
            nombre='Administración del Transporte y Organización Empresarial',
            usb_id='coord-admtroe',
            sede=2
        )
        db.Coordinacion.insert(
            nombre='Arquitectura',
            usb_id='coord-arq',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Comercio Exterior y Lic. Comercio Internacional',
            usb_id='coord-cext',
            sede=2
        )
        db.Coordinacion.insert(
            nombre='Estudios Gerenciales y Económicos',
            usb_id='alexislo',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Ingeniería de Mantenimiento',
            usb_id='cctmma',
            sede=2
        )
        db.Coordinacion.insert(
            nombre='Ingeniería de Producción y Organización Empresarial',
            usb_id='coord-prod',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Ingeniería de Telecomunicaciones',
            usb_id='post-eltr',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Ingeniería Electrónica',
            usb_id='coord-electronica',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Ingeniería en Computación',
            usb_id='coord-comp',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Ingeniería en Materiales',
            usb_id='coord-mt',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Ingeniería Geofísica',
            usb_id='coord-geo',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Ingeniería Mecánica',
            usb_id='coord-mc',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Ingeniería Química',
            usb_id='coord-iq',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Licenciatura en Biología',
            usb_id='coord-bio',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Licenciatura en Física',
            usb_id='coord-fis',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Licenciatura en Matemáticas',
            usb_id='coord-ma',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Licenciatura en Química',
            usb_id='coord-qm',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Tecnología e Ing. Eléctrica',
            usb_id='coord-el',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Tecnología Eléctrica y Electrónica',
            usb_id='coord-tee',
            sede=2
        )
        db.Coordinacion.insert(
            nombre='Tecnología Mecánica, Mantenimiento Aeronáutico e Ing. de Mantenimiento',
            usb_id='coord-tmma',
            sede=2
        )
        db.Coordinacion.insert(
            nombre='Turismo, Hotelería y Hospitalidad',
            usb_id='coord-thnul',
            sede=2
        )
        db.Coordinacion.insert(
            nombre='Urbanismo',
            usb_id='coord-urb',
            sede=1
        )

        #no salen en el archivo
        db.Coordinacion.insert(
            nombre='Coordinación de Ciclo Básico',
            usb_id='coord-ciclobasico',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Coordinación de Comercio Exterior',
            usb_id='coord-coex',
            sede=2
        )
        db.commit()
