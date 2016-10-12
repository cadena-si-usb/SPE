# -*- coding: utf-8 -*-

import cStringIO
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, purple, yellow, black, blue


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
            alignment=TA_LEFT,
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
        textColor=blue,
    )
    styles['blacktitle'] = ParagraphStyle(
        'blacktitle',
        parent=styles['default'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=10,
        alignment=TA_LEFT,
        textColor=black,
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

    story = [
        Paragraph("ESTUDIANTE", styles['bluetitle']),
    ]

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
    story.append(tbl_estu)
    Spacer(1, 0.25 * inch),
    story.append(Paragraph("TUTOR ACADEMICO", styles['bluetitle']))

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
    story.append(tbl_tut_ac)
    Spacer(1, 0.25 * inch),
    story.append(Paragraph("TUTOR INDUSTRIAL", styles['bluetitle']))

    tbl_tutor_industrial = [
        [Paragraph("Empresa:" + str(tutor_industrial.Empresa.usuario.nombre) + str(usuario['apellido']), styles["default"]),
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
    story.append(tbl_tut_ind)
    Spacer(1, 0.25 * inch),
    story.append(Paragraph("PASANTIA", styles['bluetitle']))

    tbl_pasantia = [
        [Paragraph("Titulo:" + str(pasantia.titulo), styles["default"]),
         Paragraph("Area del proyecto:" + str(pasantia.area_proyecto.nombre), styles["default"])
         ],
    ]

    tbl_pas = Table(tbl_pasantia)
    story.append(tbl_pas)

    buffer = cStringIO.StringIO()
    doc = SimpleDocTemplate(buffer)
    doc.build(story)
    pdf = buffer.getvalue()
    buffer.close()

    filename = "Plan de Trabajo"
    header = {'Content-Disposition': 'attachment; filename=' + filename}
    response.headers.update(header)

    return pdf


