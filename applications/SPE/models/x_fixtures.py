# -*- coding: utf-8 -*-

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
        sede='Sartenejas',
        tipo='Larga',
        descripcion='Lograr que el estudiante se integre a las actividades de la empresa o institución y actúe dentro de la misma como un recurso capaz de intervenir en el desarrollo completo de trabajos, tareas o proyectos a nivel profesional, utilizando para ello los conocimientos y la formación de que dispone.',
        duracion='20'
    )
    db.Materia.insert(
        codigo='EP1420',
        sede='Sartenejas',
        tipo='Corta',
        descripcion='En las primeras cuatro semanas (semana 1 a semana 4) de cada trimestre académico se llevará a cabo el Proceso de Preinscripción de la Pasantía . Los estudiantes que desean optar a una pasantía deben preinscribirse al trimestre anterior al período de la pasantía a cursar. La preinscripción tendrá carácter obligatorio y el estudiante deberá consignar ante la CCTDS, o ante la CCCE según sea el caso, específicamente al personal de Atención al Estudiante, los siguientes recaudos:',
        duracion='6'
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

if db(db.Rol.id > 0).count() == 0:
    db.Rol.insert(
        nombre='Estudiante'
    )
    db.Rol.insert(
        nombre='Coordinador_CCT'
    )
    db.Rol.insert(
        nombre='Coordinador'
    )
    db.Rol.insert(
        nombre='Invitado'
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
        rol='2',
        etapa='2'
    )
    db.Acceso_Etapa.insert(
        rol='2',
        etapa='4'
    )
    db.Acceso_Etapa.insert(
        rol='2',
        etapa='3'
    )
    db.Acceso_Etapa.insert(
        rol='2',
        etapa='1'
    )
    db.commit()

if db(db.Acceso_Etapa.id > 0).count() == 0:
    db.Acceso_Etapa.insert(
        nombre='Acciones',
        destino='/SPE/acciones_usuario/listar',
        contexto='coordinacion',
        rol='2'
    )
    db.Acceso_Etapa.insert(
        nombre='Mis Pasantias',
        destino='/SPE/mis_pasantias/listar',
        contexto='coordinacion',
        rol='1'
    )
    db.Acceso_Etapa.insert(
        nombre='Pasantias',
        destino='/SPE/pasantias/listar',
        contexto='coordinacion',
        rol='2'
    )
    db.Acceso_Etapa.insert(
        nombre='Pasantias',
        destino='/SPE/pasantias/listar',
        contexto=None,
        rol='3'
    )
    db.Acceso_Etapa.insert(
        nombre='Editar Perfil',
        destino='/SPE/mi_perfil/configuracion',
        contexto='configuracion',
        rol='1'
    )
    db.Acceso_Etapa.insert(
        nombre='Editar Curriculo',
        destino='/SPE/mi_perfil/editar_curriculo',
        contexto='configuracion',
        rol='1'
    )

    db.commit()
