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
        db.auth_group.insert(
            role='Administrativo',
            description='3'
        )
        db.auth_group.insert(
            role='Invitado',
            description='3'
        )
        db.commit()

    if db(db.Dedicacion.id > 0).count() == 0:
        db.Dedicacion.insert(
            first_name='Exclusiva'
        )
        db.commit()

    if db(db.Division.id > 0).count() == 0:
        db.Division.insert(
            first_name='Ciencias Informaticas'
        )
        db.commit()

    if db(db.Area_Proyecto.id > 0).count() == 0:
        db.Area_Proyecto.insert(
            first_name='Informatica Forense',
            descripcion=''
        )
        db.Area_Proyecto.insert(
            first_name='Sistema De Informacion',
            descripcion=''
        )
        db.commit()


    if db(db.Sede.id > 0).count() == 0:
        db.Sede.insert(
            first_name='Sartenejas'
        )
        db.Sede.insert(
            first_name='Litoral'
        )
        db.commit()

    if db(db.Pais.id > 0).count() == 0:
        db.Pais.insert(
            first_name='Venezuela'
        )
        db.Pais.insert(
            first_name='U.S.A.'
        )
        db.commit()

    if db(db.Estado.id > 0).count() == 0:
        db.Estado.insert(
            first_name='Distrito Capital',
            Pais=1
        )
        db.Estado.insert(
            first_name='Aragua',
            Pais=1
        )
        db.commit()

    if db(db.Etapa.id > 0).count() == 0:
        db.Etapa.insert(
            first_name='Preinscripcion',
            procedimientos='En las primeras cuatro semanas (semana 1 a semana 4) de cada trimestre académico se llevará a cabo el Proceso de Preinscripción de la Pasantía . Los estudiantes que desean optar a una pasantía deben preinscribirse al trimestre anterior al período de la pasantía a cursar. La preinscripción tendrá carácter obligatorio y el estudiante deberá consignar ante la CCTDS, o ante la CCCE según sea el caso, específicamente al personal de Atención al Estudiante, los siguientes recaudos:',
            descripcion='/#'
        )
        db.Etapa.insert(
            first_name='Colocacion',
            procedimientos='Después del proceso de Preinscripción, la sección de Relaciones con la Industria debe iniciar su proceso de búsqueda de pasantías mediante la comunicación con las empresas y la oferta de pasantes para el próximo período.',
            descripcion='/#'
        )
        db.Etapa.insert(
            first_name='Inscripcion',
            procedimientos='Durante la semana doce (12) del trimestre anterior a la pasantía y hasta la semana cero (0) del trimestre en el que se cursará la pasantía, se llevará a cabo el Proceso de Inscripción de la misma. Para ello, el estudiante debe descargar de la página web de la CCTDS (www.cctds.dex.usb.ve) los siguientes formularios (de carácter obligatorio)',
            descripcion='/#'
        )
        db.Etapa.insert(
            first_name='Ejecucion',
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
            first_name='Ciencias De La Informacion',
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

    # if db(db.P.id > 0).count() == 0:
    #     db.Permisos.insert(
    #         Tipo='Inscripcion Extemporanea'
    #     )
    #     db.Permisos.insert(
    #         Tipo='Inscripcion Extemporanea'
    #     )
    #     db.Permisos.insert(
    #     )
    #     db.commit()


    if db(db.Area_Laboral.id > 0).count() == 0:
        db.Area_Laboral.insert(
            first_name='Tecnologia',
            descripcion='tecnológica'
        )
        db.Area_Laboral.insert(
            first_name='Informatica',
            descripcion='Consultoria, desarrollo de software,etc'
        )
        db.Area_Laboral.insert(
            first_name='Legal',
            descripcion='Asesoria legal, resolucion de casos'
        )
        db.Area_Laboral.insert(
            first_name='Electricidad',
            descripcion='Instalaciones electricas'
        )
        db.Area_Laboral.insert(
            first_name='Arquitectura',
            descripcion='Diseño de planos'
        )
        db.commit()

    if db(db.Universidad.id > 0).count() == 0:
        db.Universidad.insert(
            first_name='Universidad Simón Bolívar',
            id_pais=1
        )
        db.Universidad.insert(
            first_name='Universidad Católica Andrés Bello',
            id_pais=1
        )
        db.Universidad.insert(
            first_name='Universidad Metropolitana',
            id_pais=1
        )
        db.Universidad.insert(
            first_name='Universidad De Florida',
            id_pais=2
        )
        db.commit()

    if db(db.Categoria.id > 0).count() == 0:
        db.Categoria.insert(
            first_name='Asociado'
        )
        db.Categoria.insert(
            first_name='Titular'
        )
        db.Categoria.insert(
            first_name='Agregado'
        )
        db.Categoria.insert(
            first_name='Asistente'
        )
        db.commit()

    if db(db.Coordinacion.id > 0).count() == 0:
        db.Coordinacion.insert(
            first_name='Computacion',
            username='1000',
            sede=1
        )
        db.Coordinacion.insert(
            first_name='Mecanica',
            username='1001',
            sede=1
        )
        db.Coordinacion.insert(
            first_name='Coordinación de Cooperación Tecnica',
            username='1002',
            sede=1
        )
        db.commit()

    if db(db.Carrera.id > 0).count() == 0:
        db.Carrera.insert(
            first_name='Ingenieria de la Computacion',
            codigo='0800',
            duracion='Larga',
            coordinacion=1
        )
        db.Carrera.insert(
            first_name='Ingenieria de Mecanica',
            codigo='0200',
            duracion='Larga',
            coordinacion=1
        )
        db.commit()

    if db(db.Tipo_Documento.id > 0).count() == 0:
        db.Tipo_Documento.insert(
            first_name='Cedula'
        )
        db.Tipo_Documento.insert(
            first_name='Pasaporte'
        )
        db.Tipo_Documento.insert(
            first_name='RIF'
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
            id='9',
            usuario='9',
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
            last_name='Sucre González',
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
        db.auth_membership.insert(
            user_id='10',
            group_id='2'
        )
        db.auth_membership.insert(
            user_id='11',
            group_id='8'
        )
        db.commit()

    if db(db.Accion_Usuario.id > 0).count() == 0:
        db.Accion_Usuario.insert(
            first_name='Acciones',
            destino='/SPE/acciones_usuario/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Mis Pasantias',
            destino='/SPE/mis_pasantias/listar',
            contexto='coordinacion',
            rol='1'
        )
        db.Accion_Usuario.insert(
            first_name='Mis Permisos',
            destino='/SPE/mis_permisos/listar',
            contexto='coordinacion',
            rol='1'
        )
        db.Accion_Usuario.insert(
            first_name='Pasantias',
            destino='/SPE/pasantias/listar',
            contexto='pasantias',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Pasantias',
            destino='/SPE/pasantias/listar',
            contexto=None,
            rol='3'
        )
        db.Accion_Usuario.insert(
            first_name='Editar Perfil',
            destino='/SPE/mi_perfil/configuracion',
            contexto='configuracion',
            rol='1'
        )
        db.Accion_Usuario.insert(
            first_name='Editar Curriculo',
            destino='/SPE/mi_perfil/editar_curriculo',
            contexto='configuracion',
            rol='1'
        )
        db.Accion_Usuario.insert(
            first_name='Usuarios',
            destino='/SPE/usuarios/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Usuarios',
            destino='/SPE/usuarios/listar',
            contexto='',
            rol='1'
        )
        db.Accion_Usuario.insert(
            first_name='Estudiantes',
            destino='/SPE/estudiantes/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Sedes',
            destino='/SPE/sedes/listar',
            contexto='catalogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Carreras',
            destino='/SPE/carreras/listar',
            contexto='catalogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='coordinaciones',
            destino='/SPE/coordinaciones/listar',
            contexto='catalogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Preinscripciones',
            destino='/SPE/preinscripciones/listar',
            contexto='pasantias',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Colocaciones',
            destino='/SPE/colocaciones/listar',
            contexto='pasantias',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Inscripciones',
            destino='/SPE/inscripciones/listar',
            contexto='pasantias',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Planes De Trabajo',
            destino='/SPE/planes_trabajo/listar',
            contexto='pasantias',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Mis Pasantias',
            destino='/SPE/Coordinador/consultarPasantias',
            contexto='coordinacion',
            rol='3'
        )
        db.Accion_Usuario.insert(
            first_name='Materias',
            destino='/SPE/materias/listar',
            contexto='',
            rol='1'
        )
        db.Accion_Usuario.insert(
            first_name='Materias',
            destino='/SPE/materias/listar',
            contexto='catalogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Permisos',
            destino='/SPE/permisos/listar',
            contexto='pasantias',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Permisos',
            destino='/SPE/permisos/agregar',
            contexto='pasantias',
            rol='1'
        )
        db.Accion_Usuario.insert(
            first_name='Permisos',
            destino='/SPE/permisos/listar',
            contexto='pasantias',
            rol='1'
        )
        db.Accion_Usuario.insert(
            first_name='Retiros',
            destino='/SPE/retiros/listar',
            contexto='pasantias',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Roles',
            destino='/SPE/roles/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Asignar Roles',
            destino='/SPE/membresias/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Areas Laborales',
            destino='/SPE/areas_laborales/listar',
            contexto='catalogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Configurar Accesos',
            destino='/SPE/accesos_etapa/listar',
            contexto='pasantias',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Areas De Proyecto',
            destino='/SPE/areas_proyecto/listar',
            contexto='catalogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Curriculos',
            destino='/SPE/curriculos/listar',
            contexto='pasantias',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Etapas',
            destino='/SPE/etapas/listar',
            contexto='catalogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Tipos De Documentos',
            destino='/SPE/tipos_documento/listar',
            contexto='catalogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Categorias',
            destino='/SPE/categorias/listar',
            contexto='catalogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Coordinadores',
            destino='/SPE/coordinadores/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Dedicaciones',
            destino='/SPE/dedicaciones/listar',
            contexto='catalogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Departamentos',
            destino='/SPE/departamentos/listar',
            contexto='catalogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Divisiones',
            destino='/SPE/divisiones/listar',
            contexto='catalogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Ejecuciones',
            destino='/SPE/ejecuciones/listar',
            contexto='pasantias',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Empresas',
            destino='/SPE/empresas/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Estados',
            destino='/SPE/estados/listar',
            contexto='catalogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Materias Periodo',
            destino='/SPE/materias_periodo/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Paises',
            destino='/SPE/paises/listar',
            contexto='catalogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Periodos',
            destino='/SPE/periodos/listar',
            contexto='catalogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Profesores',
            destino='/SPE/profesores/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Tutores Industriales',
            destino='/SPE/tutores_industriales/listar',
            contexto='coordinacion',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Universidades',
            destino='/SPE/universidades/listar',
            contexto='catalogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            first_name='Personal Administrativo',
            destino='/SPE/administrativos/listar',
            contexto='coordinacion',
            rol='6'
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
