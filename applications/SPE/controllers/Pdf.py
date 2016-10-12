# -*- coding: utf-8 -*-

import cStringIO
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, PageBreak, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, purple, yellow, black, blue, white
from reportlab.platypus.flowables import Image
import os.path


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
        fontSize=10,
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
        fontSize=10,
        leading=12,
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


    story = []

    # ENCABEZADO
    tbl_cabeza = [
        [Paragraph("<b>PLAN DE TRABAJO PASANTÍA</b>", styles["default"])
         ],
    ]

    tbl_cab = Table(tbl_cabeza, colWidths=[6.0 * inch])
    story.append(tbl_cab)
    story.append(Paragraph("/n", styles['space']))


    story.append(Paragraph("ESTUDIANTE", styles['bluetitle']))
    story.append(Paragraph("/n", styles['space']))

    # no separar en parrafos poner tod pegado
    tbl_estudiante = [
        [Paragraph("<b>Nombre y Apellido:</b>" + "  " +
                   str(usuario['nombre']) + " " + str(usuario['apellido']) + "   " +
                   "<b>Carnet:</b>" + " " + str(estudiante.Estudiante.carnet) + "   " +
                   "<b>Cedula:</b>" + " " + str(estudiante.UsuarioUSB.numero_documento), styles["default"])
         ],
        [Paragraph("<b>Carrera:</b>" + " " +
                   str(carrera.nombre) + " " +
                   "<b>Telefono:</b>" + " " + str(estudiante.UsuarioUSB.telefono) + " " +
                   "<b>Email:</b>" + " " + str(estudiante.UsuarioUSB.correo), styles["default"])
         ],
        [Paragraph("<b>Periodo de Pasantia:</b>" + " " +
                   str(pasantia.periodo.mes_inicio) + "-" +
                   str(pasantia.periodo.mes_final), styles["default"]),
         ],

    ]
    tbl_estu = Table(tbl_estudiante, colWidths=[6.0 * inch])
    tbl_estu.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
    story.append(tbl_estu)
    story.append(Paragraph("/n", styles['space']))
    story.append(Paragraph("TUTOR ACADEMICO", styles['bluetitle']))
    story.append(Paragraph("/n", styles['space']))

    tbl_tutor_academico = [
        [Paragraph("<b>Nombre y Apellido:</b>" + " " +
                   str(tutor_academico.usuario.nombre) + " " +
                   str(tutor_academico.usuario.apellido) + " " +
                   "<b>Categoria:</b>" + " " + str(tutor_academico.categoria.nombre) + " " +
                   "<b>Dedicacion:</b>" + " " + str(tutor_academico.dedicacion.nombre), styles["default"])
         ],
        [Paragraph("<b>Departamento:</b>" + " " +
                   str(tutor_academico.departamento.nombre) + " " +
                   "<b>Telefono:</b>" + " " + str(tutor_academico.usuario.telefono) + " " +
                   "<b>Email:</b>" + " " + str(tutor_academico.usuario.correo), styles["default"])
         ],
    ]

    tbl_tut_ac = Table(tbl_tutor_academico, colWidths=[6.0 * inch])
    tbl_tut_ac.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
    story.append(tbl_tut_ac)
    story.append(Paragraph("/n", styles['space']))
    story.append(Paragraph("TUTOR INDUSTRIAL", styles['bluetitle']))
    story.append(Paragraph("/n", styles['space']))

    tbl_tutor_industrial = [
        [Paragraph("<b>Empresa:</b>" + " " +
                   str(tutor_industrial.Empresa.usuario.nombre) + " " +
                   "<b>Telefono:</b>" + " " + str(tutor_industrial.Empresa.usuario.telefono) + " " +
                   "<b>Email:</b>" + " " + str(tutor_industrial.Empresa.usuario.correo) + " " +
                   "<b>Pais:</b>" + " " + str(tutor_industrial.Empresa.usuario.pais), styles["default"]),
         ],
        [Paragraph("<b>Estado:</b>" + " " + str(tutor_industrial.Empresa.usuario.estado) + " " +
                   "<b>Direccion:</b>" + " " + str(tutor_industrial.Empresa.usuario.direccion) + " " +
                   "<b>Nombres y Apellidos:</b>" + " " + str(tutor_industrial.usuario.nombre), styles["default"]),
         ],
        [
            Paragraph("<b>Profesion:</b>" + " " + str(tutor_industrial.profesion) + " " +
                      "<b>Cedula/Pasaporte:</b>" + " " + str(tutor_industrial.numero_documento) + " " +
                      "<b>Cargo:</b>" + " " + str(tutor_industrial.cargo), styles["default"])
        ],
        [Paragraph("<b>Departamento:</b>" + " " + str(tutor_industrial.departamento) + " " +
                   "<b>Contacto Recursos Humanos</b>" + " " +
                   str(tutor_industrial.Empresa.contacto_RRHH), styles["default"])
         ],
        [Paragraph("<b>Pagina web:</b>" + " " + str(tutor_industrial.Empresa.direccion_web) + " " +
                   "<b>Breve Descripción de la empresa:</b>" + " " +
                   str(tutor_industrial.Empresa.descripcion), styles["default"])
         ],

    ]

    tbl_tut_ind = Table(tbl_tutor_industrial, colWidths=[6.0 * inch])
    tbl_tut_ind.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
    story.append(tbl_tut_ind)
    story.append(Paragraph("/n", styles['space']))
    story.append(Paragraph("PASANTIA", styles['bluetitle']))
    story.append(Paragraph("/n", styles['space']))

    tbl_pasantia = [
        [Paragraph("<b>Titulo:</b>" + " " + str(pasantia.titulo) + " " +
                   "Area del proyecto:" + str(pasantia.area_proyecto.nombre), styles["default"])
         ],
    ]

    tbl_pas = Table(tbl_pasantia, colWidths=[6.0 * inch])
    tbl_pas.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
    story.append(tbl_pas)
    story.append(Paragraph("/n", styles['space']))
    # ACEPTACION DE LA TUTORIA

    story.append(Paragraph("""<b>ACEPTACIÓN DE TUTORÍA:</b> Al firmar este documento, aceptamos la tutoría de esta pasantía, durante el periodo
    señalado, y el cumplimiento de nuestras responsabilidades especificadas como Tutor Académico y Tutor Industrial
    respectivamente, establecidas por la Universidad Simón Bolívar 1 para su Programa de cursos de cooperación.
    <b>CONFIDENCIALIDAD:</b> Tanto el informe final, la presentación y defensa correspondientes a una pasantía de la
    Universidad Simón Bolívar tienen carácter público 1 , por lo que no podrán contener información clasificada como
    confidencial por parte de la Entidad de Trabajo en la cual se haya realizado la pasantía. En el caso de que se considere que
    alguna información debe ser confidencial, ésta debe indicarse en forma expresa en el Plan de Trabajo y requiere la
    suscripción de un acuerdo de confidencialidad entre la Entidad de Trabajo y la Universidad Simón Bolívar antes de dar inicio
    a la pasantía 2,3 . Ningún estudiante está autorizado a firmar unilateralmente acuerdos de confidencialidad
    con entidad alguna, de manera voluntaria u bajo coacción de algún tipo, sin la previa autorización de la Universidad
    Simón Bolívar 2.
    <b>PROPIEDAD INTELECTUAL:</b> Todo lo concerniente a la propiedad intelectual y los derechos de orden moral y patrimonial
    que se deriven de la presente pasantía, así como la comercialización y explotación de los resultados provenientes de ella,
    serán tratados en la reglamentación interna que al efecto dicte el Consejo Directivo sobre derechos de autor y patente
    industrial 2,3 .""", styles['default2']))

    # REFERENCIAS

    story.append(Paragraph("/n", styles['space']))
    story.append(Paragraph("<b>Referencias:</b>", styles['blacktitle']))
    story.append(Paragraph("1.Reglamento C.4 Cursos de Cooperación. Universidad Simón Bolívar", styles['default2']))
    story.append(Paragraph("2.Norma C.20 Pregrado. Proyectos de Grado. Universidad Simón Bolívar", styles['default2']))
    story.append(
        Paragraph("3.Resolución G.21 Creación Intelectual, Regalías. Universidad Simón Bolívar", styles['default2']))

    # FIRMAS

    qr = str(os.path.isfile("/static/images/qr.png"))
    story.append(Paragraph("/n", styles['space']))
    tbl_firmas = [
        [Paragraph("Firma del Tutor Industrial Sello de la Empresa", styles["firma"]),
         Paragraph("Firma del Tutor Académico Sello del Departamento Académico",
                   styles["firma"]),
         Paragraph(
             "Firma del Coordinador Sello de la Coordinación de Carrera",
             styles["firma"]),
         qr
         ]
    ]
    tbl_firm = Table(tbl_firmas)
    story.append(tbl_firm)
    story.append(PageBreak())
    story.append(Paragraph("/n", styles['space']))
    story.append(Paragraph("PASANTIA", styles['bluetitle']))
    story.append(Paragraph("/n", styles['space']))


    # DETALLES PSANTIA

    tbl_pasantia2 = [
        [Paragraph("<b>Titulo:</b>" + " " + str(pasantia.titulo) + " " +
                   "Area del proyecto:" + str(pasantia.area_proyecto.nombre), styles["default"])
         ],
    ]
    tbl_pasantia3 = [
        [Paragraph("<b>Resumen del proyecto:</b>" + " " + str(pasantia.resumen_proyecto), styles["default"])
         ],
    ]
    tbl_pasantia4 = [
        [Paragraph("<b>Objetivo General:</b>" + " " + str(pasantia.objetivo), styles["default"])
         ],
    ]
    tbl_pasantia5 = [
        [Paragraph("<b>Detalles de Confidencialidad:</b>" + " " + str(pasantia.confidencialidad), styles["default"])
         ],
    ]

    tbl_pas2 = Table(tbl_pasantia2, colWidths=[6.0 * inch])
    tbl_pas3 = Table(tbl_pasantia3, colWidths=[6.0 * inch])
    tbl_pas4 = Table(tbl_pasantia4, colWidths=[6.0 * inch])
    tbl_pas5 = Table(tbl_pasantia5, colWidths=[6.0 * inch])
    tbl_pas2.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
    tbl_pas3.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
    tbl_pas4.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
    tbl_pas5.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
    story.append(tbl_pas2)
    story.append(tbl_pas3)
    story.append(tbl_pas4)
    story.append(tbl_pas5)


    # OBEJTIVOS ESPECIFICOS
    # Hacer un FOR para todos los objetivo especificos y listo

    # Desde aqui va el FOR
    contador = 1
    story.append(Paragraph("/n", styles['space']))
    tbl_objetivo_titulo = [
        [Paragraph(str(contador) +" " + "<b>Objetivo especifico:</b>" + " " +
                   "str(pasantia.objetivoespeciico[i].titulo)",styles["default"])
         ]
    ]
    tbl_objetivo=[
        [Paragraph("<b>Actividades</b>", styles["default"]),
         Paragraph("<b>Semana Inicio</b>", styles["default"]),
         Paragraph("<b>Semana Final</b>", styles["default"]),
         ],
        [
         # Hacer un FOR para las actividades del objetivo especifico desde aqui
         Paragraph("str(pasantia.objetivoespecifico[i].actividad[j].id)" + " " +
                   "str(pasantia.objetivoespecifico[i].actividad[j].nombre)", styles["default"]),
         Paragraph("str(pasantia.objetivoespecifico[i].actividad[j].inicio", styles["default"]),
         Paragraph("str(pasantia.objetivoespecifico[i].actividad[j].final", styles["default"]),
         # Hasta aqui
         ],
    ]
    tbl_obj_tit =Table(tbl_objetivo_titulo, colWidths=[6.0 * inch])
    tbl_obj_tit.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
    story.append(tbl_obj_tit)

    tbl_obj = Table(tbl_objetivo, colWidths=[2.0 * inch])
    tbl_obj.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                                 ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black)]))
    story.append(tbl_obj)

    # Hasta aqui

    # CRONOGRAMA DE ACTIVIDADES

    story.append(Paragraph("/n", styles['space']))
    story.append(Paragraph("CRONOGRAMA DE ACTIVIDADES", styles['bluetitle']))
    story.append(Paragraph("/n", styles['space']))

    tbl_titulo_semanas = [
        [Paragraph("<b>SEMANAS DEL PERIODO DE PASANTIAS:</b>",styles["default"])
         ]
    ]

    tbl_tot_sem =Table(tbl_titulo_semanas , colWidths=[6.3 * inch])
    tbl_tot_sem.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
    story.append(tbl_tot_sem)

    tbl_cronograma=[
        [Paragraph("Act", styles["default"]),
         Paragraph("1", styles["default"]),
         Paragraph("2", styles["default"]),
         Paragraph("3", styles["default"]),
         Paragraph("4", styles["default"]),
         Paragraph("5", styles["default"]),
         Paragraph("6", styles["default"]),
         Paragraph("7", styles["default"]),
         Paragraph("8", styles["default"]),
         Paragraph("9", styles["default"]),
         Paragraph("10", styles["default"]),
         Paragraph("11", styles["default"]),
         Paragraph("12", styles["default"]),
         Paragraph("13", styles["default"]),
         Paragraph("14", styles["default"]),
         Paragraph("15", styles["default"]),
         Paragraph("16", styles["default"]),
         Paragraph("17", styles["default"]),
         Paragraph("18", styles["default"]),
         Paragraph("19", styles["default"]),
         Paragraph("20", styles["default"]),
         ],
        # hacer un FOR para las actividades del proyecto
        # en ID va el id de la actividad
        # en IF va la condicion de si la ctividad comienza o termina en esa semana coloca un *
        [Paragraph("ID", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         Paragraph("IF", styles["default"]),
         ],
        # hasta aqui

    ]
    tbl_cro =Table(tbl_cronograma, colWidths=[0.3 * inch])
    tbl_cro.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                                ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black)]))
    story.append(tbl_cro)

    # FIRMAS2

    story.append(Paragraph("/n", styles['space']))
    tbl_firmas2 = [
        [Paragraph("V.B del Tutor Académico", styles["firma"]),
         Paragraph("V.B. del Coordinador de Carrera" + str(estudiante.Estudiante.carnet),
                   styles["firma"])
         ],
    ]
    tbl_firm2 = Table(tbl_firmas2)
    story.append(tbl_firm2)

    buffer = cStringIO.StringIO()
    doc = SimpleDocTemplate(buffer)
    doc.build(story)
    pdf = buffer.getvalue()
    buffer.close()

    filename = "Plan de Trabajo"
    header = {'Content-Disposition': 'attachment; filename=' + filename}
    response.headers.update(header)

    return pdf
