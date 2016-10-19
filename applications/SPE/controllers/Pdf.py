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


def es_semana(actividad, semana):
    if int(actividad.semana_fin) == int(semana) or int(actividad.semana_inicio) == int(semana) or (
                (semana < int(actividad.semana_fin)) and (semana > int(actividad.semana_inicio))):
        return str("")
    else:
        return str(" ")


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
        fontSize=9,
        leading=10,
        alignment=TA_LEFT,
        textColor=HexColor(0x325d88),
    )
    styles['firma'] = ParagraphStyle(
        'firma',
        parent=styles['default'],
        fontName='Times-Roman',
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
        leading=10,
        textColor=black,
        alignment=TA_JUSTIFY,
    )
    styles['default3'] = ParagraphStyle(
        'default3',
        parent=styles['default'],
        fontName='Times-Roman',
        fontSize=10,
        leading=12,
        textColor=black,
        alignment=TA_CENTER,
    )

    return styles


def generarPdfPlanTrabajo():
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
    plan_trabajo = db(db.Plan_Trabajo.pasantia == pasantia.id).select().first()
    fases = db(db.Fase.plan_trabajo == pasantia.id).select(orderby=db.Fase.numero)
    tutor_academico = pasantia.tutor_academico
    tutor_industrial = pasantia.tutor_industrial

    styles = stylesheet()

    story = []
    logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/images/logo2.png')
    logo = Image(logo_path, width=120, height=80)

    # ENCABEZADO
    tbl_cabeza = [
        [logo,
         Paragraph("<b>PLAN DE TRABAJO PASANTÍA</b>", styles["default3"]),
         Paragraph("Pagina 1 de 3", styles["default3"]),
         ],
    ]

    tbl_cab = Table(tbl_cabeza, colWidths=[2.5 * inch])
    story.append(tbl_cab)
    story.append(Paragraph("ESTUDIANTE", styles['bluetitle']))

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

    tbl_tutor_industrial = [
        [Paragraph("<b>Empresa:</b>" + " " +
                   str(tutor_industrial.Empresa.usuario.nombre) + " " +
                   "<b>Telefono:</b>" + " " + str(tutor_industrial.Empresa.usuario.telefono) + " " +
                   "<b>Email:</b>" + " " + str(tutor_industrial.Empresa.usuario.correo) + " " +
                   "<b>Pais:</b>" + " " + str(tutor_industrial.Empresa.usuario.pais.nombre), styles["default"]),
         ],
        [Paragraph("<b>Estado:</b>" + " " + str(tutor_industrial.Empresa.usuario.estado.nombre) + " " +
                   "<b>Direccion:</b>" + " " + str(tutor_industrial.Empresa.usuario.direccion) + " " +
                   "<b>Nombres y Apellidos:</b>" + " " + str(tutor_industrial.usuario.nombre) + " " +
                   str(tutor_industrial.apellido), styles["default"]),
         ],
        [
            Paragraph("<b>Profesion:</b>" + " " + str(tutor_industrial.profesion) + " " +
                      "<b>Cedula/Pasaporte:</b>" + " " + str(tutor_industrial.numero_documento) + " " +
                      "<b>Cargo:</b>" + " " + str(tutor_industrial.cargo), styles["default"])
        ],
        [Paragraph("<b>Departamento:</b>" + " " + str(tutor_industrial.departamento), styles["default"])
         ],
        [Paragraph("<b>Contacto Recursos Humanos:</b>" + " " +
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

    tbl_pasantia = [
        [Paragraph("<b>Titulo:</b>" + " " + str(pasantia.titulo), styles["default"])
         ],
        [Paragraph("<b>Area del proyecto:</b>" + str(pasantia.area_proyecto.nombre), styles["default"])
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

    qr_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/images/qr.png')
    qr = Image(qr_path, width=70, height=70)
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
    story.append(tbl_cab)
    story.append(Paragraph("/n", styles['space']))
    story.append(Paragraph("PASANTIA", styles['bluetitle']))


    # DETALLES PASANTIA

    tbl_pasantia2 = [
        [Paragraph("<b>Titulo:</b>" + " " + str(pasantia.titulo), styles["default"])
         ],
        [Paragraph("<b>Area del proyecto:</b>" + str(pasantia.area_proyecto.nombre), styles["default"])
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
    for fase in fases:
        story.append(Paragraph("/n", styles['space']))
        tbl_objetivo_titulo = [
            [Paragraph(str(contador) + " " + "<b>Objetivo especifico:</b>" + " " +
                       str(fase.objetivo_especifico), styles["default"])
             ]
        ]
        tbl_objetivo1 = [
            [Paragraph("<b>Actividades</b>", styles["default"]),
             Paragraph("<b>Semana Inicio</b>", styles["default"]),
             Paragraph("<b>Semana Final</b>", styles["default"]),
             ],

        ]
        tbl_obj_tit = Table(tbl_objetivo_titulo, colWidths=[6.0 * inch])
        tbl_obj_tit.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
        story.append(tbl_obj_tit)

        tbl_obj1 = Table(tbl_objetivo1, colWidths=[2.0 * inch])
        tbl_obj1.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                                      ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)]))
        story.append(tbl_obj1)

        for actividad in fase.Actividad.select(orderby=db.Actividad.numero):
            tbl_objetivo = [
                [Paragraph(str(actividad.descripcion), styles["default"]),
                 Paragraph(str(actividad.semana_inicio), styles["default"]),
                 Paragraph(str(actividad.semana_fin), styles["default"]),
                 ],
            ]

            tbl_obj = Table(tbl_objetivo, colWidths=[2.0 * inch])
            tbl_obj.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                                         ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)]))
            story.append(tbl_obj)

        contador += 1

    # Hasta aqui

    # CRONOGRAMA DE ACTIVIDADES

    story.append(Paragraph("/n", styles['space']))
    story.append(Paragraph("CRONOGRAMA DE ACTIVIDADES", styles['bluetitle']))

    tbl_titulo_semanas = [
        [Paragraph("<b>SEMANAS DEL PERIODO DE PASANTIAS:</b>", styles["default"])
         ]
    ]

    tbl_tot_sem = Table(tbl_titulo_semanas, colWidths=[6.0 * inch])
    tbl_tot_sem.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
    story.append(tbl_tot_sem)

    tbl_cronograma1 = [
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
    ]
    tbl_cro1 = Table(tbl_cronograma1, colWidths=[0.285714286 * inch])
    tbl_cro1.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                                  ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)]))
    story.append(tbl_cro1)
    for fase in fases:
        for actividad in fase.Actividad.select():
            tbl_cronograma2 = [
                [Paragraph(str(fase.numero) + "." + str(actividad.numero), styles["default"]),
                 Paragraph(str(es_semana(actividad, 1)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 2)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 3)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 4)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 5)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 6)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 7)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 8)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 9)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 10)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 11)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 12)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 13)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 14)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 15)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 16)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 17)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 18)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 19)), styles["default"]),
                 Paragraph(str(es_semana(actividad, 20)), styles["default"]),
                 ],
            ]
            tbl_cro2 = Table(tbl_cronograma2, colWidths=[0.285 * inch])
            tbl_cro2.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                                          ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)]))
            story.append(tbl_cro2)

    # FIRMAS2

    story.append(Paragraph("/n", styles['space']))
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
