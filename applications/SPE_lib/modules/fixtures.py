# -*- coding: utf-8 -*-
def load_auth_fixtures(db,T):
    if db(db.auth_group.id > 0).count() == 0:
        db.auth_group.insert(
            role='Estudiante',
            description='3'
        )
        db.auth_group.insert(
            role='Profesor',
            description='2'
        )
        db.auth_group.insert(
            role='Coordinador',
            description='4'
        )
        db.auth_group.insert(
            role='Empresa',
            description='3'
        )
        db.auth_group.insert(
            role='Tutor Industrial',
            description='3'
        )
        db.auth_group.insert(
            role='CoordinadorCCT',
            description='3'
        )
        db.auth_group.insert(
            role='AdministrativoCCT',
            description='3'
        )
        db.auth_group.insert(
            role='Administrativo',
            description='3'
        )
        db.auth_group.insert(
            role='Invitado',
            description='3'
        )
        db.commit()



    if db(db.auth_user.id > 0).count() == 0:
        db.auth_user.insert(
            id=1,
            first_name='Ecorp',
            last_name='',
            email='ecorp-admin@ecorp.com',
            username=None,
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id='ecorp-admin@ecorp.com'
        )
        db.auth_user.insert(
            id=2,
            first_name='Francisco Javier',
            last_name='Sucre González',
            email='fsucre@integra.la',
            username=None,
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id=''
        )
        db.auth_user.insert(
            id=3,
            first_name='Enrique',
            last_name='Muguerza',
            email='emuguerza@gmail.com',
            username=None,
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id=''
        )
        db.auth_user.insert(
            id=4,
            first_name='Roberto Andres',
            last_name='Manzanilla',
            email='queso976@gmail.com',
            username=None,
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id=''
        )
        db.auth_user.insert(
            id=5,
            first_name='Hector Alejandro',
            last_name='Goncalves Pita',
            email='',
            username='10-10292',
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id=''
        )
        db.auth_user.insert(
            id=6,
            first_name='Daniel Arturo',
            last_name='Marin Tirado',
            email='',
            username='10-10419',
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id=''
        )
        db.auth_user.insert(
            id=7,
            first_name='Francisco Javier',
            last_name='Sucre Gonzalez',
            email='',
            username='10-10717',
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id=''
        )
        db.auth_user.insert(
            id=8,
            first_name='Mathieu',
            last_name='Da Valery',
            email='',
            username='10-10193',
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id=''
        )
        db.auth_user.insert(
            id=9,
            first_name='Andres Rafael',
            last_name='Hernandez Monterola',
            email='',
            username='10-10353',
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id=''
        )
        db.auth_user.insert(
            id=10,
            first_name= 'Alfredo',
            last_name='Delgado',
            email='',
            username='10-10195',
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id=''
        )
        db.auth_user.insert(
            id=11,
            first_name='Gabriel',
            last_name='Austin',
            email='',
            username='09-10066',
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id=''
        )
        db.commit()

    if db(db.auth_user.id > 0).count() == 0:
        db.auth_user.insert(
            auth_User=1,
            first_name='Ecorp',
            email='ecorp-admin@ecorp.com',
            pregunta_secreta='¿Cual es la solucion?',
            respuesta_secreta='¡Ecorp!',
            pais='1',
            estado='1',
            telefono='04128063009',
            direccion='Sartenejas'
        )
        db.auth_user.insert(
            auth_User=2,
            first_name='Francisco Javier',
            email='fsucre@integra.la',
            pregunta_secreta='¿Mejor Equipo Del Futbol?',
            respuesta_secreta='Real Madrid',
            pais='1',
            estado='1',
            telefono='04128063009',
            direccion='Calle P1'
        )
        db.commit()

    if db(db.auth_user.id > 0).count() == 0:
        db.auth_user.insert(
            id=3,
            auth_User=3,
            username='emuguerza',
            first_name='Enrique',
            last_name='Muguerza',
            email='emuguerza@gmail.com',
            clave=db.auth_user.password.validate('Ecorp.2016')[0],
            tipo_documento='1',
            numero_documento='11234112',
            telefono='04122347576',
            direccion='Caracas',
            sexo='M',
            activo='True'
        )
        db.auth_user.insert(
            id=4,
            auth_User=4,
            username='10-10102',
            first_name='Roberto Andres',
            last_name='Manzanilla',
            email='queso976@gmail.com',
            clave=db.auth_user.password.validate('Ecorp.2016')[0],
            tipo_documento='1',
            numero_documento='20101324',
            telefono='04129767576',
            direccion='Prados Del Este',
            sexo='M',
            activo='True'
        )
        db.auth_user.insert(
            id=5,
            auth_User=5,
            username='10-10292',
            first_name='Hector Alejandro',
            last_name='Goncalves Pita',
            email='KKNKKMTGJYXLCURWCFAC',
            clave=db.auth_user.password.validate('Ecorp.2016')[0],
            tipo_documento='1',
            numero_documento='20101324',
            telefono='04243130932',
            direccion='Prados Del Este',
            sexo='M',
            activo='True'
        )
        db.auth_user.insert(
            id=6,
            auth_User=6,
            username='10-10419',
            first_name='Daniel Arturo',
            last_name='Marin Tirado',
            email='NULL',
            clave=db.auth_user.password.validate('Ecorp.2016')[0],
            tipo_documento='1',
            numero_documento='21464359',
            telefono='0414-4742003',
            direccion='merche',
            sexo='M',
            activo='True'
        )
        db.auth_user.insert(
            id=7,
            auth_User=7,
            username='10-10717',
            first_name='Francisco Javier',
            last_name='Sucre Gonzalez',
            email='10-10717@usb.ve',
            clave=db.auth_user.password.validate('Ecorp.2016')[0],
            tipo_documento='1',
            numero_documento='19564959',
            telefono='02127653852',
            direccion='La Floresta',
            sexo='M',
            activo='True'
        )
        db.auth_user.insert(
            id=8,
            auth_User=8,
            username='10-10193',
            first_name='Mathieu',
            last_name='Da Valery',
            email='mvalery@gmail.com',
            clave=db.auth_user.password.validate('Ecorp.2016')[0],
            tipo_documento='1',
            numero_documento='20101324',
            telefono='04129767576',
            direccion='Prados Del Este',
            sexo='M',
            activo='True'
        )
        db.auth_user.insert(
            id=9,
            auth_User=9,
            username='10-10353',
            first_name='Andres Rafael',
            last_name='Hernandez Monterola',
            email='queso976@gmail.com',
            clave=db.auth_user.password.validate('Ecorp.2016')[0],
            tipo_documento='1',
            numero_documento='20101324',
            telefono='04129767576',
            direccion='Prados Del Este',
            sexo='M',
            activo='True'
        )
        db.auth_user.insert(
            id=10,
            auth_User=10,
            username='10-10195',
            first_name='Alfredo',
            last_name='Delgado',
            email='adelgado@gmail.com',
            clave=db.auth_user.password.validate('Ecorp.2016')[0],
            tipo_documento='1',
            numero_documento='20101324',
            telefono='04129767576',
            direccion='Prados Del Este',
            sexo='M',
            activo='True'
        )
        db.auth_user.insert(
            id=11,
            auth_User=11,
            username='09-10066',
            first_name='Gabriel',
            last_name='Austin',
            email='gmailaustin@gmail.com',
            clave=db.auth_user.password.validate('Ecorp.2016')[0],
            tipo_documento='1',
            numero_documento='20101324',
            telefono='04129767576',
            direccion='Prados Del Este',
            sexo='M',
            activo='True'
        )
        db.commit()



    if db(db.auth_membership.id > 0).count() == 0:
        db.auth_membership.insert(
            user_id='1',
            group_id='4'
        )
        db.auth_membership.insert(
            user_id='2',
            group_id='5'
        )
        db.auth_membership.insert(
            user_id='3',
            group_id='1'
        )
        db.auth_membership.insert(
            user_id='4',
            group_id='1'
        )
        db.auth_membership.insert(
            user_id='5',
            group_id='2'
        )
        db.auth_membership.insert(
            user_id='6',
            group_id='6'
        )
        db.auth_membership.insert(
            user_id='7',
            group_id='1'
        )
        db.auth_membership.insert(
            user_id='8',
            group_id='3'
        )
        db.auth_membership.insert(
            user_id='9',
            group_id='6'
        )
        db.auth_membership.insert(
            user_id='10',
            group_id='2'
        )
        db.auth_membership.insert(
            user_id='11',
            group_id='8'
        )
        db.commit()
