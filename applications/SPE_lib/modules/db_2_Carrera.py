# -*- coding: utf-8 -*-
from gluon import *
def Carrera_Table(db,T):
    # Estudiante
    db.define_table('Carrera',
                    Field('codigo','string',
                          required=True,
                          ondelete='CASCADE',
                          notnull=True,
                          label='Código'),
                    Field('first_name','string',required=True, requires=[IS_LENGTH(100)], label='Nombre'),
                    Field('duracion','string',required=True, requires=IS_IN_SET(['Larga','Corta']), label="Duración", notnull=True),
                    Field('usb_id', 'string'), #required?
                    Field('coordinacion','reference Coordinacion', label="Coordinación", required=True),
                    Field('sede', 'reference Sede', label='Sedes (*)'),
                    format='%(codigo)s %(first_name)s'
                   )
    db.Carrera.codigo.requires = [IS_LENGTH(4)
            ,IS_NOT_EMPTY(error_message='Campo Obligatorio')
            ,IS_NOT_IN_DB(db, 'Carrera.codigo',error_message=T('Carrera ya existe'))
            ,IS_MATCH('[0-9]{4}',error_message=T('Solo se permiten numeros de cuatro digitos'))]

    if db(db.Carrera.id > 0).count() == 0:
        db.Carrera.insert(
            first_name='Ciclo Básico',
            codigo='0',
            usb_id='coord-ciclobasico',
            duracion='Larga',
            coordinacion=1,
            sede=1
        )
        db.Carrera.insert(
            first_name='Tecnología Eléctrica - Litoral',
            codigo='1',
            usb_id='coord-tee',
            duracion='Corta',
            coordinacion=21,
            sede=2
        )
        db.Carrera.insert(
            first_name='Tecnología Electrónica - Litoral',
            codigo='2',
            usb_id='coord-tee',
            duracion='Corta',
            coordinacion=21,
            sede=2
        )
        db.Carrera.insert(
            first_name='Tecnología Mecánica - Litoral',
            codigo='3',
            usb_id='coord-tmma',
            duracion='Corta',
            coordinacion=22,
            sede=2
        )
        db.Carrera.insert(
            first_name='Mantenimiento Aeronáutico - Litoral',
            codigo='4',
            usb_id='coord-tmma',
            duracion='Corta',
            coordinacion=22,
            sede=2
        )
        db.Carrera.insert(
            first_name='Administración del Turismo - Litoral',
            codigo='5',
            usb_id='coord-thnul',
            duracion='Corta',
            coordinacion=23,
            sede=2
        )
        db.Carrera.insert(
            first_name='Administración Hotelera - Litoral',
            codigo='6',
            usb_id='coord-thnul',
            duracion='Corta',
            coordinacion=23,
            sede=2
        )
        db.Carrera.insert(
            first_name='Administración del Transporte - Litoral',
            codigo='7',
            usb_id='coord-admtroe',
            duracion='Corta',
            coordinacion=3,
            sede=2
        )
        db.Carrera.insert(
            first_name='Organización Empresarial - Litoral',
            codigo='8',
            usb_id='coord-admtroe',
            duracion='Corta',
            coordinacion=3,
            sede=2
        )
        db.Carrera.insert(
            first_name='Comercio Exterior - Litoral',
            codigo='9',
            usb_id='coord-cext',
            duracion='Corta',
            coordinacion=5,
            sede=2
        )
        db.Carrera.insert(
            first_name='Administración Aduanera - Litoral',
            codigo='10',
            usb_id='coord-aduanera',
            duracion='Larga',
            coordinacion=2,
            sede=2
        )
        db.Carrera.insert(
            first_name='Licenciatura en Gestión de la Hospitalidad',
            codigo='11',
            usb_id='coord-thnul',
            duracion='Larga',
            coordinacion=23,
            sede=2
        )
        db.Carrera.insert(
            first_name='Ingeniería de Mantenimiento - Litoral',
            codigo='14',
            usb_id='cctmma',
            duracion='Larga',
            coordinacion=7,
            sede=2
        )
        db.Carrera.insert(
            first_name='Licenciatura en Comercio Internacional - Litoral',
            codigo='15',
            usb_id='coord-cext',
            duracion='Larga',
            coordinacion=5,
            sede=2
        )
        db.Carrera.insert(
            first_name='Ingeniería Eléctrica',
            codigo='100',
            usb_id='coord-el',
            duracion='Larga',
            coordinacion=20,
            sede=1
        )
        db.Carrera.insert(
            first_name='Ingeniería Mecánica',
            codigo='200',
            usb_id='coord-mc',
            duracion='Larga',
            coordinacion=14,
            sede=1
        )
        db.Carrera.insert(
            first_name='Ingeniería Química',
            codigo='300',
            usb_id='coord-iq',
            duracion='Larga',
            coordinacion=15,
            sede=1
        )
        db.Carrera.insert(
            first_name='Licenciatura en Química',
            codigo='400',
            usb_id='coord-qm',
            duracion='Larga',
            coordinacion=19,
            sede=1
        )
        db.Carrera.insert(
            first_name='Licenciatura en Matemáticas',
            codigo='500',
            usb_id='coord-ma',
            duracion='Larga',
            coordinacion=18,
            sede=1
        )
        db.Carrera.insert(
            first_name='Licenciatura en Matemáticas, opc. Estadística y M.Computacionales',
            codigo='501',
            usb_id='coord-ma',
            duracion='Larga',
            coordinacion=18,
            sede=1
        )
        db.Carrera.insert(
            first_name='Licenciatura en Matemáticas, opc. Didáctica de las Matemáticas',
            codigo='502',
            usb_id='coord-ma',
            duracion='Larga',
            coordinacion=18,
            sede=1
        )
        db.Carrera.insert(
            first_name='Ingeniería Electrónica',
            codigo='600',
            usb_id='coord-electronica',
            duracion='Larga',
            coordinacion=10,
            sede=1
        )
        db.Carrera.insert(
            first_name='Arquitectura',
            codigo='700',
            usb_id='coord-arq',
            duracion='Larga',
            coordinacion=4,
            sede=1
        )
        db.Carrera.insert(
            first_name='Ingeniería de la Computación',
            codigo='800',
            usb_id='coord-comp',
            duracion='Larga',
            coordinacion=11,
            sede=1
        )
        db.Carrera.insert(
            first_name='Licenciatura en Física',
            codigo='1000',
            usb_id='coord-fis',
            duracion='Larga',
            coordinacion=17,
            sede=1
        )
        db.Carrera.insert(
            first_name='Urbanismo',
            codigo='1100',
            usb_id='coord-urb',
            duracion='Larga',
            coordinacion=24,
            sede=1
        )
        db.Carrera.insert(
            first_name='Ingeniería Geofísica',
            codigo='1200',
            usb_id='coord-geo',
            duracion='Larga',
            coordinacion=13,
            sede=1
        )
        db.Carrera.insert(
            first_name='Ingeniería de Materiales',
            codigo='1500',
            usb_id='coord-mt',
            duracion='Larga',
            coordinacion=12,
            sede=1
        )
        db.Carrera.insert(
            first_name='Ingeniería de Producción',
            codigo='1700',
            usb_id='coord-prod',
            duracion='Larga',
            coordinacion=8,
            sede=1
        )
        db.Carrera.insert(
            first_name='Ingeniería de Telecomunicaciones',
            codigo='1800',
            usb_id='post-eltr',
            duracion='Larga',
            coordinacion=9,
            sede=1
        )
        db.Carrera.insert(
            first_name='Licenciatura en Biología',
            codigo='1900',
            usb_id='coord-bio',
            duracion='Larga',
            coordinacion=16,
            sede=1
        )
        db.Carrera.insert(
            first_name='Licenciatura en Gestión de la Hospitalidad - Sartenejas',
            codigo='3000',
            usb_id='coord-thnul',
            duracion='Larga',
            coordinacion=23,
            sede=1
        )
        db.Carrera.insert(
            first_name='Licenciatura en Comercio Internacional - Sartenejas',
            codigo='3200',
            usb_id='coord-cext',
            duracion='Larga',
            coordinacion=5,
            sede=1
        )
        db.Carrera.insert(
            first_name='Tecnología Eléctrica - Sartenejas',
            codigo='4000',
            usb_id='coord-el',
            duracion='Corta',
            coordinacion=20,
            sede=1
        )
        db.Carrera.insert(
            first_name='Tecnología Electrónica - Sartenejas',
            codigo='4100',
            usb_id='coord-electronica',
            duracion='Corta',
            coordinacion=10,
            sede=1
        )
        db.Carrera.insert(
            first_name='Organización Empresarial - Sartenejas',
            codigo='4200',
            usb_id='coord-prod',
            duracion='Corta',
            coordinacion=8,
            sede=1
        )
        db.Carrera.insert(
            first_name='Comercio Exterior - Sartenejas',
            codigo='4300',
            usb_id='coord-coex',
            duracion='Corta',
            coordinacion=1,
            sede=1
        )
        db.commit()
