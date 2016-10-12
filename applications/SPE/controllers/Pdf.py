# -*- coding: utf-8 -*-

import cStringIO
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, PageBreak, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, purple, yellow, black, blue, white


def stylesheet():
    styles = {
        'default': ParagraphStyle(
            'default',
            fontName='Times-Roman',
            fontSize=10,
            leading=10,
            leftIndent=0,
            rightIndent=0,
            firstLineIndent=0,
            alignment=TA_JUSTIFY,
            spaceBefore=0,
            spaceAfter=0,
            bulletFontName='Times-Roman',
            bulletFontSize=10,
            bulletIndent=0,
            textColor=black,
            backColor=None,
            wordWrap=None,
            borderWidth=0,
            borderPadding=0,
            borderColor=None,
            borderRadius=None,
            allowWidows=1,
            allowOrphans=0,
            textTransform=None,  # 'uppercase' | 'lowercase' | None
            endDots=None,
            splitLongWords=1,
        ),
    }
    styles['bluetitle'] = ParagraphStyle(
        'bluetitle',
        parent=styles['default'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=10,
        alignment=TA_LEFT,
        textColor=HexColor(0x325d88),
    )
    styles['firma'] = ParagraphStyle(
        'firma',
        parent=styles['default'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=10,
        alignment=TA_CENTER,
        textColor=black,
    )

    styles['blacktitle'] = ParagraphStyle(
        'blacktitle',
        parent=styles['default'],
        fontName='Times-Roman',
        fontSize=9,
        leading=10,
        alignment=TA_LEFT,
        textColor=black,
    )
    styles['space'] = ParagraphStyle(
        'space',
        parent=styles['default'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=10,
        alignment=TA_LEFT,
        textColor=white,
    )
    styles['default2'] = ParagraphStyle(
        'default2',
        parent=styles['default'],
        fontName='Times-Roman',
        fontSize=8,
        leading=8,
        textColor=black,
        alignment=TA_JUSTIFY,
    )

    return styles


def generarPdfConstanciaCulminacion():
    # Datos del estudiante

    userid = session.currentUser.id
    currentUser = db.UsuarioUSB(db.UsuarioUSB.id == userid)
    rol = db(
        (db.auth_membership.user_id == userid) & (db.auth_membership.group_id == db.auth_group.id)).select().first()
    usuario = {
        "apellido": currentUser.apellido,
        "nombre": currentUser.nombre,
        "rol": rol.auth_group.role,
    }

    estudiante = db(((db.UsuarioUSB.id == userid) & (db.Estudiante.usuario == db.UsuarioUSB.id))).select().first()
    carrera = db.Carrera(id=estudiante.Estudiante.carrera)
    sede = db(db.Sede.id == db.Estudiante.sede).select().first()
    pasantia = db(db.Pasantia.estudiante == estudiante.Estudiante).select().first()
    tutor_academico = pasantia.tutor_academico
    tutor_industrial = pasantia.tutor_industrial

    styles = stylesheet()

    story = [Paragraph("ESTUDIANTE", styles['bluetitle']), Paragraph("/n", styles['space'])]

    # no separar en parrafos poner tod pegado
    tbl_estudiante = [
        [Paragraph("Nombre y Apellido:" + str(usuario['nombre']) + str(usuario['apellido']), styles["default"]),
         Paragraph("Carnet:" + str(estudiante.Estudiante.carnet), styles["default"]),
         Paragraph("Cedula:" + str(estudiante.UsuarioUSB.numero_documento), styles["default"])
         ],
        [Paragraph("Carrera: " + str(carrera.nombre), styles["default"]),
         Paragraph("Telefono:" + str(estudiante.UsuarioUSB.telefono), styles["default"]),
         Paragraph("Email:" + str(estudiante.UsuarioUSB.correo), styles["default"])
         ],
        [Paragraph("Periodo de Pasantia:" + str(pasantia.periodo.mes_inicio) + "-"
                   + str(pasantia.periodo.mes_final), styles["default"]),
         ],

    ]
    tbl_estu = Table(tbl_estudiante)
    tbl_estu.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
    story.append(tbl_estu)
    story.append(Paragraph("/n", styles['space']))
    story.append(Paragraph("TUTOR ACADEMICO", styles['bluetitle']))
    story.append(Paragraph("/n", styles['space']))

    tbl_tutor_academico = [
        [Paragraph("Nombre y Apellido:" + str(tutor_academico.usuario.nombre) +
                   str(tutor_academico.usuario.apellido), styles["default"]),
         Paragraph("Categoria:" + str(tutor_academico.categoria.nombre), styles["default"]),
         Paragraph("Dedicacion:" + str(tutor_academico.dedicacion.nombre), styles["default"])
         ],
        [Paragraph("Departamento: " + str(tutor_academico.departamento.nombre), styles["default"]),
         Paragraph("Telefono:" + str(tutor_academico.usuario.telefono), styles["default"]),
         Paragraph("Email:" + str(tutor_academico.usuario.correo), styles["default"])
         ],
    ]

    tbl_tut_ac = Table(tbl_tutor_academico)
    tbl_tut_ac.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
    story.append(tbl_tut_ac)
    story.append(Paragraph("/n", styles['space']))
    story.append(Paragraph("TUTOR INDUSTRIAL", styles['bluetitle']))
    story.append(Paragraph("/n", styles['space']))

    tbl_tutor_industrial = [
        [Paragraph("Empresa:" + str(tutor_industrial.Empresa.usuario.nombre) + str(usuario['apellido']),
                   styles["default"]),
         Paragraph("Telefono:" + str(tutor_industrial.Empresa.usuario.telefono), styles["default"]),
         Paragraph("Email:" + str(tutor_industrial.Empresa.usuario.correo), styles["default"])
         ],
        [Paragraph("Pais: " + str(tutor_industrial.Empresa.usuario.pais), styles["default"]),
         Paragraph("Estado:" + str(tutor_industrial.Empresa.usuario.estado), styles["default"]),
         Paragraph("Direccion:" + str(tutor_industrial.Empresa.usuario.direccion), styles["default"])
         ],
        [Paragraph("Nombres y Apellidos: " + str(tutor_industrial.usuario.nombre), styles["default"]),
         Paragraph("Profesion:" + str(tutor_industrial.profesion), styles["default"]),
         Paragraph("Cedula/Pasaporte:" + str(tutor_industrial.numero_documento), styles["default"])
         ],
        [Paragraph("Cargo: " + str(tutor_industrial.cargo), styles["default"]),
         Paragraph("Departamento:" + str(tutor_industrial.departamento), styles["default"]),
         Paragraph("Contacto Recursos Humanos" + str(tutor_industrial.Empresa.contacto_RRHH), styles["default"])
         ],
        [Paragraph("Pagina web: " + str(tutor_industrial.Empresa.direccion_web), styles["default"]),
         Paragraph("Breve Descripción de la empresa:" + str(tutor_industrial.Empresa.descripcion), styles["default"])
         ],

    ]

    tbl_tut_ind = Table(tbl_tutor_industrial)
    tbl_tut_ind.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
    story.append(tbl_tut_ind)
    story.append(Paragraph("/n", styles['space']))
    story.append(Paragraph("PASANTIA", styles['bluetitle']))
    story.append(Paragraph("/n", styles['space']))

    tbl_pasantia = [
        [Paragraph("Titulo:" + str(pasantia.titulo), styles["default"]),
         Paragraph("Area del proyecto:" + str(pasantia.area_proyecto.nombre), styles["default"])
         ],
    ]

    tbl_pas = Table(tbl_pasantia)
    tbl_pas.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
    story.append(tbl_pas)
    story.append(Paragraph("/n", styles['space']))
    # ACEPTACION DE LA TUTORIA

    story.append(Paragraph("""ACEPTACIÓN DE TUTORÍA: Al firmar este documento, aceptamos la tutoría de esta pasantía, durante el periodo
    señalado, y el cumplimiento de nuestras responsabilidades especificadas como Tutor Académico y Tutor Industrial
    respectivamente, establecidas por la Universidad Simón Bolívar 1 para su Programa de cursos de cooperación.
    CONFIDENCIALIDAD: Tanto el informe final, la presentación y defensa correspondientes a una pasantía de la
    Universidad Simón Bolívar tienen carácter público 1 , por lo que no podrán contener información clasificada como
    confidencial por parte de la Entidad de Trabajo en la cual se haya realizado la pasantía. En el caso de que se considere que
    alguna información debe ser confidencial, ésta debe indicarse en forma expresa en el Plan de Trabajo y requiere la
    suscripción de un acuerdo de confidencialidad entre la Entidad de Trabajo y la Universidad Simón Bolívar antes de dar inicio
    a la pasantía 2,3 . Ningún estudiante está autorizado a firmar unilateralmente acuerdos de confidencialidad
    con entidad alguna, de manera voluntaria u bajo coacción de algún tipo, sin la previa autorización de la Universidad
    Simón Bolívar 2 .
    PROPIEDAD INTELECTUAL: Todo lo concerniente a la propiedad intelectual y los derechos de orden moral y patrimonial
    que se deriven de la presente pasantía, así como la comercialización y explotación de los resultados provenientes de ella,
    serán tratados en la reglamentación interna que al efecto dicte el Consejo Directivo sobre derechos de autor y patente
    industrial 2,3 .""", styles['default2']))

    # REFERENCIAS

    story.append(Paragraph("/n", styles['space']))
    story.append(Paragraph("""Referencias:""", styles['blacktitle']))
    story.append(Paragraph("1.Reglamento C.4 Cursos de Cooperación. Universidad Simón Bolívar", styles['default2']))
    story.append(Paragraph("2.Norma C.20 Pregrado. Proyectos de Grado. Universidad Simón Bolívar", styles['default2']))
    story.append(
        Paragraph("3.Resolución G.21 Creación Intelectual, Regalías. Universidad Simón Bolívar", styles['default2']))

    # FIRMAS

    story.append(Paragraph("/n", styles['space']))
    tbl_firmas = [
        [Paragraph("Firma del Tutor Industrial Sello de la Empresa", styles["firma"]),
         Paragraph("Firma del Tutor Académico Sello del Departamento Académico:" + str(estudiante.Estudiante.carnet),
                   styles["firma"]),
         Paragraph(
             "Firma del Coordinador Sello de la Coordinación de Carrera" + str(estudiante.UsuarioUSB.numero_documento),
             styles["firma"])
         ],
    ]
    tbl_firm = Table(tbl_firmas)
    story.append(tbl_firm)

    buffer = cStringIO.StringIO()
    doc = SimpleDocTemplate(buffer)
    doc.build(story)
    pdf = buffer.getvalue()
    buffer.close()

    filename = "Plan de Trabajo"
    header = {'Content-Disposition': 'attachment; filename=' + filename}
    response.headers.update(header)

    return pdf
