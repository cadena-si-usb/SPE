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
            username='ecorp-admin@ecorp.com',
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id='ecorp-admin@ecorp.com',
            tipo_documento='1',
            numero_documento='12341223',
            telefono='02129871121',
            direccion='Portal de algun lado, calle 234',
            sexo='M',
            activo=True,
            pregunta_secreta='Pregunta??',
            respuesta_secreta='Respuesta!!',
            pais='1',
            estado='1',
        )
        db.auth_user.insert(
            id=2,
            first_name='Francisco Javier',
            last_name='Sucre González',
            email='fsucre@integra.la',
            username='fsucre@integra.la',
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id='',
            tipo_documento='1',
            numero_documento='12341223',
            telefono='02129871121',
            direccion='Portal de algun lado, calle 234',
            sexo='M',
            activo=True,
            pregunta_secreta='Pregunta??',
            respuesta_secreta='Respuesta!!',
            pais='1',
            estado='1',
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
            registration_id='',
            tipo_documento='1',
            numero_documento='12341223',
            telefono='02129871121',
            direccion='Portal de algun lado, calle 234',
            sexo='M',
            activo=True,
            pregunta_secreta='Pregunta??',
            respuesta_secreta='Respuesta!!',
            pais='1',
            estado='1',
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
            registration_id='',
            tipo_documento='1',
            numero_documento='12341223',
            telefono='02129871121',
            direccion='Portal de algun lado, calle 234',
            sexo='M',
            activo=True,
            pregunta_secreta='Pregunta??',
            respuesta_secreta='Respuesta!!',
            pais='1',
            estado='1',
        )
        db.auth_user.insert(
            id=5,
            first_name='Hector Alejandro',
            last_name='Goncalves Pita',
            email='hpita@gmail.com',
            username='10-10292',
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id='',
            tipo_documento='1',
            numero_documento='12341223',
            telefono='02129871121',
            direccion='Portal de algun lado, calle 234',
            sexo='M',
            activo=True,
            pregunta_secreta='Pregunta??',
            respuesta_secreta='Respuesta!!',
            pais='1',
            estado='1',
        )
        db.auth_user.insert(
            id=6,
            first_name='Daniel Arturo',
            last_name='Marin Tirado',
            email='dmarin@gmail.com',
            username='10-10419',
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id='',
            tipo_documento='1',
            numero_documento='12341223',
            telefono='02129871121',
            direccion='Portal de algun lado, calle 234',
            sexo='M',
            activo=True,
            pregunta_secreta='Pregunta??',
            respuesta_secreta='Respuesta!!',
            pais='1',
            estado='1',
        )
        db.auth_user.insert(
            id=7,
            first_name='Francisco Javier',
            last_name='Sucre Gonzalez',
            email='frank91frank@gmail.com',
            username='10-10717',
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id='',
            tipo_documento='1',
            numero_documento='12341223',
            telefono='02129871121',
            direccion='Portal de algun lado, calle 234',
            sexo='M',
            activo=True,
            pregunta_secreta='Pregunta??',
            respuesta_secreta='Respuesta!!',
            pais='1',
            estado='1',
        )
        db.auth_user.insert(
            id=8,
            first_name='Mathieu',
            last_name='Da Valery',
            email='mvalery@gmail.com',
            username='10-10193',
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id='',
            tipo_documento='1',
            numero_documento='12341223',
            telefono='02129871121',
            direccion='Portal de algun lado, calle 234',
            sexo='M',
            activo=True,
            pregunta_secreta='Pregunta??',
            respuesta_secreta='Respuesta!!',
            pais='1',
            estado='1',
        )
        db.auth_user.insert(
            id=9,
            first_name='Andres Rafael',
            last_name='Hernandez Monterola',
            email='ahernandez@gmail.com',
            username='10-10353',
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id='',
            tipo_documento='1',
            numero_documento='12341223',
            telefono='02129871121',
            direccion='Portal de algun lado, calle 234',
            sexo='M',
            activo=True,
            pregunta_secreta='Pregunta??',
            respuesta_secreta='Respuesta!!',
            pais='1',
            estado='1',
        )
        db.auth_user.insert(
            id=10,
            first_name= 'Alfredo',
            last_name='Delgado',
            email='adelgado@gmail.com',
            username='10-10195',
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id='',
            tipo_documento='1',
            numero_documento='12341223',
            telefono='02129871121',
            direccion='Portal de algun lado, calle 234',
            sexo='M',
            activo=True,
            pregunta_secreta='Pregunta??',
            respuesta_secreta='Respuesta!!',
            pais='1',
            estado='1',
        )
        db.auth_user.insert(
            id=11,
            first_name='Gabriel',
            last_name='Austin',
            email='gaustin@gmail.com',
            username='09-10066',
            password=db.auth_user.password.validate('Ecorp.2016')[0],
            registration_key='',
            reset_password_key='',
            registration_id='',
            tipo_documento='1',
            numero_documento='12341223',
            telefono='02129871121',
            direccion='Portal de algun lado, calle 234',
            sexo='Masculino',
            activo=True,
            pregunta_secreta='Pregunta??',
            respuesta_secreta='Respuesta!!',
            pais='1',
            estado='1',
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
