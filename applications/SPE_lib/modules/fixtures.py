# -*- coding: utf-8 -*-
def load_fixtures(db,T):
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
        db.commit()

    if db(db.Dedicacion.id > 0).count() == 0:
        db.Dedicacion.insert(
            nombre='Exclusiva'
        )
        db.commit()

    if db(db.Division.id > 0).count() == 0:
        db.Division.insert(
            nombre='Ciencias Informaticas'
        )
        db.commit()

    if db(db.Area_Proyecto.id > 0).count() == 0:
        db.Area_Proyecto.insert(
            nombre='Informatica Forense',
            descripcion=''
        )
        db.Area_Proyecto.insert(
            nombre='Sistema De Informacion',
            descripcion=''
        )
        db.commit()


    if db(db.Sede.id > 0).count() == 0:
        db.Sede.insert(
            nombre='Sartenejas'
        )
        db.Sede.insert(
            nombre='Litoral'
        )
        db.commit()

    if db(db.Pais.id > 0).count() == 0:
        db.Pais.insert(
            nombre='Venezuela'
        )
        db.Pais.insert(
            nombre='U.S.A.'
        )
        db.commit()

    if db(db.Estado.id > 0).count() == 0:
        db.Estado.insert(
            nombre='Distrito Capital',
            Pais=1
        )
        db.Estado.insert(
            nombre='Aragua',
            Pais=1
        )
        db.commit()

    if db(db.Etapa.id > 0).count() == 0:
        db.Etapa.insert(
            nombre='Preinscripcion',
            procedimientos='En las primeras cuatro semanas (semana 1 a semana 4) de cada trimestre académico se llevará a cabo el Proceso de Preinscripción de la Pasantía . Los estudiantes que desean optar a una pasantía deben preinscribirse al trimestre anterior al período de la pasantía a cursar. La preinscripción tendrá carácter obligatorio y el estudiante deberá consignar ante la CCTDS, o ante la CCCE según sea el caso, específicamente al personal de Atención al Estudiante, los siguientes recaudos:',
            descripcion='/#'
        )
        db.Etapa.insert(
            nombre='Colocacion',
            procedimientos='Después del proceso de Preinscripción, la sección de Relaciones con la Industria debe iniciar su proceso de búsqueda de pasantías mediante la comunicación con las empresas y la oferta de pasantes para el próximo período.',
            descripcion='/#'
        )
        db.Etapa.insert(
            nombre='Inscripcion',
            procedimientos='Durante la semana doce (12) del trimestre anterior a la pasantía y hasta la semana cero (0) del trimestre en el que se cursará la pasantía, se llevará a cabo el Proceso de Inscripción de la misma. Para ello, el estudiante debe descargar de la página web de la CCTDS (www.cctds.dex.usb.ve) los siguientes formularios (de carácter obligatorio)',
            descripcion='/#'
        )
        db.Etapa.insert(
            nombre='Ejecucion',
            procedimientos='Por contretar',
            descripcion='/#'
        )
        db.commit()

    if db(db.Materia.id > 0).count() == 0:
        db.Materia.insert(
            codigo='EP3420',
            sede='1',
            tipo='Larga',
            descripcion='Lograr que el estudiante se integre a las actividades de la empresa o institución y actúe dentro de la misma como un recurso capaz de intervenir en el desarrollo completo de trabajos, tareas o proyectos a nivel profesional, utilizando para ello los conocimientos y la formación de que dispone.',
            duracion='20'
        )
        db.Materia.insert(
            codigo='EP1420',
            sede='1',
            tipo='Corta',
            descripcion='En las primeras cuatro semanas (semana 1 a semana 4) de cada trimestre académico se llevará a cabo el Proceso de Preinscripción de la Pasantía . Los estudiantes que desean optar a una pasantía deben preinscribirse al trimestre anterior al período de la pasantía a cursar. La preinscripción tendrá carácter obligatorio y el estudiante deberá consignar ante la CCTDS, o ante la CCCE según sea el caso, específicamente al personal de Atención al Estudiante, los siguientes recaudos:',
            duracion='6'
        )
        db.commit()

    if db(db.Departamento.id > 0).count() == 0:
        db.Departamento.insert(
            nombre='Ciencias De La Informacion',
            id_division='1',
            email_dep='ci@usb.ve',
            sede='1',
        )
        db.commit()

    if db(db.Periodo.id > 0).count() == 0:
        db.Periodo.insert(
            mes_inicio='Abril',
            mes_final='Septiembre'
        )
        db.Periodo.insert(
            mes_inicio='Abril',
            mes_final='Septiembre'
        )
        db.Periodo.insert(
            mes_inicio='Octubre',
            mes_final='Enero'
        )
        db.commit()

    if db(db.Area_Laboral.id > 0).count() == 0:
        db.Area_Laboral.insert(
            nombre='Tecnologia',
            descripcion='tecnológica'
        )
        db.Area_Laboral.insert(
            nombre='Informatica',
            descripcion='Consultoria, desarrollo de software,etc'
        )
        db.Area_Laboral.insert(
            nombre='Legal',
            descripcion='Asesoria legal, resolucion de casos'
        )
        db.Area_Laboral.insert(
            nombre='Electricidad',
            descripcion='Instalaciones electricas'
        )
        db.Area_Laboral.insert(
            nombre='Arquitectura',
            descripcion='Diseño de planos'
        )
        db.commit()

    if db(db.Universidad.id > 0).count() == 0:
        db.Universidad.insert(
            nombre='Universidad Simón Bolívar',
            id_pais=1
        )
        db.Universidad.insert(
            nombre='Universidad Católica Andrés Bello',
            id_pais=1
        )
        db.Universidad.insert(
            nombre='Universidad Metropolitana',
            id_pais=1
        )
        db.Universidad.insert(
            nombre='Universidad De Florida',
            id_pais=2
        )
        db.commit()

    if db(db.Categoria.id > 0).count() == 0:
        db.Categoria.insert(
            nombre='Asociado'
        )
        db.Categoria.insert(
            nombre='Titular'
        )
        db.Categoria.insert(
            nombre='Agregado'
        )
        db.Categoria.insert(
            nombre='Asistente'
        )
        db.commit()

    if db(db.Coordinacion.id > 0).count() == 0:
        db.Coordinacion.insert(
            nombre='Computacion',
            usbid='1000',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Mecanica',
            usbid='1001',
            sede=1
        )
        db.Coordinacion.insert(
            nombre='Coordinación de Cooperación Tecnica',
            usbid='1002',
            sede=1
        )
        db.commit()

    if db(db.Carrera.id > 0).count() == 0:
        db.Carrera.insert(
            nombre='Ingenieria de la Computacion',
            codigo='0800',
            duracion='Larga',
            coordinacion=1
        )
        db.Carrera.insert(
            nombre='Ingenieria de Mecanica',
            codigo='0200',
            duracion='Larga',
            coordinacion=1
        )
        db.commit()

    if db(db.Tipo_Documento.id > 0).count() == 0:
        db.Tipo_Documento.insert(
            nombre='Cedula'
        )
        db.Tipo_Documento.insert(
            nombre='Pasaporte'
        )
        db.Tipo_Documento.insert(
            nombre='RIF'
        )
        db.commit()

    if db(db.Acceso_Etapa.id > 0).count() == 0:
        db.Acceso_Etapa.insert(
            rol='3',
            etapa='3'
        )
        db.Acceso_Etapa.insert(
            rol='6',
            etapa='2'
        )
        db.Acceso_Etapa.insert(
            rol='6',
            etapa='4'
        )
        db.Acceso_Etapa.insert(
            rol='6',
            etapa='3'
        )
        db.Acceso_Etapa.insert(
            rol='6',
            etapa='1'
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
            first_name='Roberto',
            last_name='Romero',
            email='',
            username='10-10642',
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

    if db(db.UsuarioExterno.id > 0).count() == 0:
        db.UsuarioExterno.insert(
            auth_User=1,
            nombre='Ecorp',
            correo='ecorp-admin@ecorp.com',
            pregunta_secreta='¿Cual es la solucion?',
            respuesta_secreta='¡Ecorp!',
            pais='1',
            estado='1',
            telefono='04128063009',
            direccion='Sartenejas'
        )
        db.UsuarioExterno.insert(
            auth_User=2,
            nombre='Francisco Javier',
            correo='fsucre@integra.la',
            pregunta_secreta='¿Mejor Equipo Del Futbol?',
            respuesta_secreta='Real Madrid',
            pais='1',
            estado='1',
            telefono='04128063009',
            direccion='Calle P1'
        )
        db.commit()

    if db(db.UsuarioUSB.id > 0).count() == 0:
        db.UsuarioUSB.insert(
            id=3,
            auth_User=3,
            usbid='emuguerza',
            nombre='Enrique',
            apellido='Muguerza',
            correo='emuguerza@gmail.com',
            clave=db.auth_user.password.validate('Ecorp.2016')[0],
            tipo_documento='1',
            numero_documento='11234112',
            telefono='04122347576',
            direcUsuario='Caracas',
            sexo='M',
            activo='True'
        )
        db.UsuarioUSB.insert(
            id=4,
            auth_User=4,
            usbid='10-10102',
            nombre='Roberto Andres',
            apellido='Manzanilla',
            correo='queso976@gmail.com',
            clave=db.auth_user.password.validate('Ecorp.2016')[0],
            tipo_documento='1',
            numero_documento='20101324',
            telefono='04129767576',
            direcUsuario='Prados Del Este',
            sexo='M',
            activo='True'
        )
        db.UsuarioUSB.insert(
            id=5,
            auth_User=5,
            usbid='10-10292',
            nombre='Hector Alejandro',
            apellido='Goncalves Pita',
            correo='KKNKKMTGJYXLCURWCFAC',
            clave=db.auth_user.password.validate('Ecorp.2016')[0],
            tipo_documento='1',
            numero_documento='20101324',
            telefono='04243130932',
            direcUsuario='Prados Del Este',
            sexo='M',
            activo='True'
        )
        db.UsuarioUSB.insert(
            id=6,
            auth_User=6,
            usbid='10-10419',
            nombre='Daniel Arturo',
            apellido='Marin Tirado',
            correo='NULL',
            clave=db.auth_user.password.validate('Ecorp.2016')[0],
            tipo_documento='1',
            numero_documento='21464359',
            telefono='0414-4742003',
            direcUsuario='merche',
            sexo='M',
            activo='True'
        )
        db.UsuarioUSB.insert(
            id=7,
            auth_User=7,
            usbid='10-10717',
            nombre='Francisco Javier',
            apellido='Sucre Gonzalez',
            correo='10-10717@usb.ve',
            clave=db.auth_user.password.validate('Ecorp.2016')[0],
            tipo_documento='1',
            numero_documento='19564959',
            telefono='02127653852',
            direcUsuario='La Floresta',
            sexo='M',
            activo='True'
        )
        db.UsuarioUSB.insert(
            id=8,
            auth_User=8,
            usbid='10-10193',
            nombre='Mathieu',
            apellido='Da Valery',
            correo='mvalery@gmail.com',
            clave=db.auth_user.password.validate('Ecorp.2016')[0],
            tipo_documento='1',
            numero_documento='20101324',
            telefono='04129767576',
            direcUsuario='Prados Del Este',
            sexo='M',
            activo='True'
        )
        db.UsuarioUSB.insert(
            id=9,
            auth_User=9,
            usbid='10-10353',
            nombre='Andres Rafael',
            apellido='Hernandez Monterola',
            correo='queso976@gmail.com',
            clave=db.auth_user.password.validate('Ecorp.2016')[0],
            tipo_documento='1',
            numero_documento='20101324',
            telefono='04129767576',
            direcUsuario='Prados Del Este',
            sexo='M',
            activo='True'
        )
        db.UsuarioUSB.insert(
            id=10,
            auth_User=10,
            usbid='10-10642',
            nombre='Roberto',
            apellido='Romero',
            correo='robert@gmail.com',
            clave=db.auth_user.password.validate('Ecorp.2016')[0],
            tipo_documento='1',
            numero_documento='20101324',
            telefono='04129767576',
            direcUsuario='Prados Del Este',
            sexo='M',
            activo='True'
        )
        db.UsuarioUSB.insert(
            id=11,
            auth_User=11,
            usbid='09-10066',
            nombre='Gabriel',
            apellido='Austin',
            correo='gmailaustin@gmail.com',
            clave=db.auth_user.password.validate('Ecorp.2016')[0],
            tipo_documento='1',
            numero_documento='20101324',
            telefono='04129767576',
            direcUsuario='Prados Del Este',
            sexo='M',
            activo='True'
        )
        db.commit()

    if db(db.Estudiante.id > 0).count() == 0:
        db.Estudiante.insert(
            id='4',
            usuario='4',
            carnet='10-10102',
            carrera='1',
            sede='1',
            activo='True'
        )
        db.Estudiante.insert(
            id='7',
            usuario='7',
            carnet='10-10717',
            carrera='1',
            sede='1',
            activo='True'
        )
        db.commit()

    if db(db.Profesor.id > 0).count() == 0:
        db.Profesor.insert(
            id='3',
            usuario='3',
            categoria='1',
            dedicacion='1',
            departamento='1',
            sede='1',
            activo='True'
        )
        db.Profesor.insert(
            id='5',
            usuario='5',
            categoria='1',
            dedicacion='1',
            departamento='1',
            sede='1',
            activo='True'
        )
        db.Profesor.insert(
            id='10',
            usuario='10',
            categoria='1',
            dedicacion='1',
            departamento='1',
            sede='1',
            activo='True'
        )
        db.commit()

    if db(db.Administrativo.id > 0).count() == 0:
        db.Administrativo.insert(
            id='11',
            usuario='11',
            carnet='09-10066',
            coordinacion='3',
            correo_Alternativo='gmailaustin@gmail.com'
        )
        db.commit()

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

    if db(db.Tutor_Industrial.id > 0).count() == 0:
        db.Tutor_Industrial.insert(
            id='2',
            usuario='2',
            apellido='Sucre González',
            Empresa='1',
            profesion='Consultor De Software',
            tipo_documento='1',
            numero_documento='19564959',
            cargo='Administrador De Base De Datos',
            departamento='Tecnologia De La Informacion',
            universidad='1',
            comfirmado_Por_Empresa='1'
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

        db.commit()

    if db(db.Accion_Usuario.id > 0).count() == 0:
        db.Accion_Usuario.insert(
            nombre='Acciones',
            destino='/SPE/acciones_usuario/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            nombre='Mis Pasantias',
            destino='/SPE/mis_pasantias/listar',
            contexto='coordinacion',
            rol='1'
        )
        db.Accion_Usuario.insert(
            nombre='Pasantias',
            destino='/SPE/pasantias/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            nombre='Pasantias',
            destino='/SPE/pasantias/listar',
            contexto=None,
            rol='3'
        )
        db.Accion_Usuario.insert(
            nombre='Editar Perfil',
            destino='/SPE/mi_perfil/configuracion',
            contexto='configuracion',
            rol='1'
        )
        db.Accion_Usuario.insert(
            nombre='Editar Curriculo',
            destino='/SPE/mi_perfil/editar_curriculo',
            contexto='configuracion',
            rol='1'
        )
        db.Accion_Usuario.insert(
            nombre='Usuarios',
            destino='/SPE/usuarios/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            nombre='Estudiantes',
            destino='/SPE/estudiantes/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            nombre='Sedes',
            destino='/SPE/sedes/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            nombre='Carreras',
            destino='/SPE/carreras/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            nombre='Coordinaciones',
            destino='/SPE/coordinaciones/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            nombre='Preinscripciones',
            destino='/SPE/preinscripciones/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            nombre='Colocaciones',
            destino='/SPE/colocaciones/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            nombre='Inscripciones',
            destino='/SPE/inscripciones/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            nombre='Planes De Trabajo',
            destino='/SPE/planes_trabajo/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            nombre='Mis Pasantias',
            destino='/SPE/Coordinador/consultarPasantias',
            contexto='coordinacion',
            rol='3'
        )
        db.commit()

    if db(db.Coordinador.id > 0).count() == 0:
        db.Coordinador.insert(
            id='6',
            usuario='6',
            carnet='10-10330',
            coordinacion='3',
            correo_Alternativo='danielarturomt@gmail.com'
        )
        db.Coordinador.insert(
            id='8',
            usuario='8',
            carnet='10-10193',
            coordinacion = '1',
            correo_Alternativo='coord@copt.com'
        )
        db.Coordinador.insert(
            id='9',
            usuario='9',
            carnet='10-10292',
            coordinacion = '2',
            correo_Alternativo='asd@asd.com'
        )
        db.commit()

    if db(db.Curriculo.id > 0).count() == 0:
        db.Curriculo.insert(
            estudiante='4',
            electivas='Diseño De Piezas',
            cursos = 'Matlab II',
            aficiones='Fifa 2016',
            idiomas='Español, Ingles',
            activo=True
        )
        db.Curriculo.insert(
            estudiante='7',
            electivas='Sistemas De Informacion II, Sistemas De Informacion III,Base De Datos II,Modelos Lineales II',
            cursos = 'Codeacademy',
            aficiones='Musica',
            idiomas='Español, Ingles,Portugues',
            activo=True
        )
        db.commit()
