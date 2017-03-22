# -*- coding: utf-8 -*-

import cStringIO
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, PageBreak, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, purple, yellow, black, blue, white, red, gray, green
from reportlab.platypus.flowables import Image
from reportlab.lib.pagesizes import letter

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
        fontSize=10,
        leading=10,
        alignment=TA_LEFT,
        textColor=HexColor(0x325d88),
    )
    styles['bluetitle2'] = ParagraphStyle(
        'bluetitle2',
        parent=styles['default'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=10,
        alignment=TA_RIGHT,
        textColor=HexColor(0x325d88),
    )
    styles['firma'] = ParagraphStyle(
        'firma',
        parent=styles['default'],
        fontName='Times-Roman',
        fontSize=10,
        leading=10,
        alignment=TA_CENTER,
        textColor=black,
    )

    styles['blacktitle'] = ParagraphStyle(
        'blacktitle',
        parent=styles['default'],
        fontName='Times-Roman',
        fontSize=12,
        leading=10,
        alignment=TA_LEFT,
        textColor=black,
    )
    styles['blacktitle2'] = ParagraphStyle(
        'blacktitle2',
        parent=styles['default'],
        fontName='Times-Roman',
        fontSize=12,
        leading=10,
        alignment=TA_CENTER,
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
        alignment=TA_CENTER,
    )
    styles['default2-2'] = ParagraphStyle(
        'default2',
        parent=styles['default'],
        fontName='Times-Roman',
        fontSize=8,
        leading=10,
        textColor=black,
        alignment=TA_LEFT,
    )
    styles['default3'] = ParagraphStyle(
        'default3',
        parent=styles['default'],
        fontName='Times-Roman',
        fontSize=12,
        leading=12,
        textColor=black,
        alignment=TA_CENTER,
    )
    styles['default4'] = ParagraphStyle(
        'default4',
        parent=styles['default'],
        fontName='Times-Roman',
        fontSize=12,
        leading=16,
        textColor=black,
        alignment=TA_LEFT,
    )
    styles['default5'] = ParagraphStyle(
        'default5',
        parent=styles['default'],
        fontName='Times-Roman',
        fontSize=12,
        leading=16,
        textColor=black,
        alignment=TA_RIGHT,
    )
    styles['table_default2'] = TableStyle(
        [
            ('BOX', (0, 0), (-1, -1), 2, black),

        ]
    )
    styles['table_default3'] = TableStyle(
        [
            ('INNERGRID', (0, 0), (-1, -1), 1, gray),
            ('LINEABOVE', (0, 0), (-1, -1), 1, black),
            ('LINEBEFORE', (0, 0), (-1, -1), 1, black),
            ('LINEAFTER', (0, 0), (-1, -1), 1, black),
            ('LINEBELOW', (0, 0), (-1, -1), 0.5, gray),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),

        ]
    )
    styles['table_default4'] = TableStyle(
        [
            ('INNERGRID', (0, 0), (-1, -1), 0.5, gray),
            ('LINEABOVE', (0, 0), (-1, -1), 0.5, gray),
            ('LINEBEFORE', (0, 0), (-1, -1), 0.5, gray),
            ('LINEAFTER', (0, 0), (-1, -1), 0.5, gray),
            ('LINEBELOW', (0, 0), (-1, -1), 0.5, gray),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

        ]
    )
    styles['table_firma'] = TableStyle(
        [
            ('INNERGRID', (0, 0), (-1, -1), 0.5, gray),
            ('LINEABOVE', (0, 0), (-1, -1), 0.5, gray),
            ('LINEBEFORE', (0, 0), (-1, -1), 0.5, gray),
            ('LINEAFTER', (0, 0), (-1, -1), 0.5, gray),
            ('LINEBELOW', (0, 0), (-1, -1), 0.5, gray),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),

        ]
    )
    styles['table_default5'] = TableStyle(
        [
            ('INNERGRID', (0, 0), (-1, -1), 0.75, gray),
            ('LINEABOVE', (0, 0), (-1, -1), 0.75, gray),
            ('LINEBEFORE', (0, 0), (0, 0), 1.25, black),
            ('LINEAFTER', (-1, 0), (-1, 0), 1.25, black),
            ('LINEBELOW', (0, 0), (-1, -1), 1.25, black),
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),
            ('VALIGN', (0, 0), (0, 0), 'TOP'),

        ]
    )
    styles['table_default6'] = TableStyle(
        [
            ('LINEABOVE', (0, 0), (-1, -1), 0.5, gray),
            ('LINEBEFORE', (0, 0), (-1, -1), 0.5, gray),
            ('LINEAFTER', (0, 0), (-1, -1), 0.5, gray),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),

        ]
    )
    styles['table_default7'] = TableStyle(
        [
            ('LINEBEFORE', (0, 0), (-1, -1), 1, black),
            ('LINEAFTER', (0, 0), (-1, -1), 1, black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

        ]
    )
    styles['table_default8'] = TableStyle(
        [
            ('LINEBEFORE', (0, 0), (-1, -1), 1, black),
            ('LINEAFTER', (0, 0), (-1, -1), 1, black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, -1), (0, -1), 'TOP'),

        ]
    )

    styles['table_encabezado'] = TableStyle(
        [

            ('ALIGN', (-1, 0), (-1, -1), 'RIGHT'),
            ('VALIGN', (-1, 0), (-1, -1), 'MIDDLE'),

        ]
    )


    return styles


def generarPdfInscripcionExtemporanea():

    carrera = 'Ingenieria Geofisica'
    estudiante = 'Christian Jose Merino Gonzalez'
    carnet = '12-10946'
    cedula = '20.156.258'
    tutor = 'Leonid Tineo'
    telefono = '0416-1234567'
    periodo = 'Julio-Agosto 2016'
    justificacion = '''Debido que, conseguí la pasantía en el período vacacional y me encontraba en el Estado
                        Anzoategui, necesito, obligatoriamente inscribir las pasantías durante la inscripción
                        extemporánea.'''
    codigo = 'b25512fe28'
    pasantia = 'corta'

    width, height = letter

    styles = stylesheet()

    story = []
    logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/images/logo2.png')
    logo = Image(logo_path, width=180, height=120)

    # ENCABEZADO

    tbl_tempo = Table(
        [[Paragraph("Fecha de la Solicitud", styles["default5"]),
          ],
         [Paragraph("<b>PLANILLA DE INSCRIPCIÓN EXTEMPORANEA</b>", styles["default3"]),
          ],
         ],
        rowHeights=[h * inch for h in [0.25, 1]],
        colWidths= 4.5 * inch,
        style=styles['table_encabezado'],

    )

    tbl_prueba = Table(
        [[logo,
          tbl_tempo,
          ]
         ],
        colWidths=[h * inch for h in [2.5, 5]],
        style=styles['table_encabezado'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Datos del Estudiante</b>"
                    , styles["default3"]),
          ],
         ],
        style=styles['table_default6'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Número de Carnet: </b>", styles["default"]),
          Paragraph(carnet, styles["default"]),
          Paragraph("<b>Número de Cédula de Identidad: </b>", styles["default"]),
          Paragraph(cedula, styles["default"]),
          ]
         ],
        colWidths=[h * inch for h in [1.75, 2, 1.75, 2]],
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Nombre del Estudiante: </b>", styles["default"]),
          Paragraph(estudiante, styles["default"]),
          ]
         ],
        colWidths=[h * inch for h in [1.75, 5.75]],
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Carrera: </b>", styles["default"]),
          Paragraph(carrera, styles["default"]),
          ]
         ],
        colWidths=[h * inch for h in [1.75, 5.75]],
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Trimestre: </b>", styles["default"]),
          Paragraph(periodo, styles["default"]),
          Paragraph("<b>Teléfono de contacto: </b>", styles["default"]),
          Paragraph(telefono, styles["default"]),
          ]
         ],
        colWidths=[h * inch for h in [1.75, 2, 1.75, 2]],
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Nombre del Tutor Academico: </b>", styles["default"]),
          Paragraph(tutor, styles["default"]),
          ]
         ],
        colWidths=[h * inch for h in [1.75, 5.75]],
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Datos de la pasantia</b>"
                    , styles["default3"]),
          ],
         ],
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    story.append(Spacer(1, 12))

    tbl_prueba = Table(
        [[Paragraph("<b>Código de asignatura</b>", styles["default2"]),
          Paragraph("<b>Nombre de la asignatura</b>", styles["default2"]),
          Paragraph("<b>Acción que solicita</b>", styles["default2"]),
          Paragraph("<b>Permiso que solicita</b>", styles["default2"]),
          Paragraph("<b>Autorizado </b>(Coordinacion)", styles["default2"]),
          Paragraph("<b>Solicitud de cupo </b>(Sección, firma y sello Dpto)", styles["default2"]),
          Paragraph("<b>Dejar sin efecto el tramite</b>", styles["default2"]),
          ]
         ],
        colWidths=[h * inch for h in [0.75, 1.5, 0.75, 1.25, 1, 1.5, 0.75]],
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    if pasantia == 'corta':

        tbl_prueba = Table(
            [[Paragraph("EP1420", styles["blacktitle"]),
              Paragraph("Pasantia Corta", styles["blacktitle"]),
              Paragraph("<u>__</u>Incluir <u>__</u>Modificar", styles["default2-2"]),
              [[Paragraph("<u>__</u>Requisito/correquisito", styles["default2-2"]),
               ],
              [Paragraph("<u>__</u>Extraplan", styles["default2-2"]),
               ],
              [Paragraph("<u>__</u>Cambio de Seccion", styles["default2-2"]),
               ]],
              Paragraph("<u>__</u>SI   <u>__</u>NO", styles["blacktitle"]),
              Paragraph(" ", styles["default2"]),
              Paragraph("<u>__</u>", styles["default2"]),
              ]
             ],
            colWidths=[h * inch for h in [0.75, 1.5, 0.75, 1.25, 1, 1.5, 0.75]],
            rowHeights=0.5 * inch,
            style=styles['table_default4'],

        )

    elif pasantia == 'intermedia':

        tbl_prueba = Table(
            [[Paragraph("EP2420", styles["blacktitle"]),
              Paragraph("Pasantia Intermedia", styles["blacktitle"]),
              Paragraph("<u>__</u>Incluir <u>__</u>Modificar", styles["default2-2"]),
              [[Paragraph("<u>__</u>Requisito/correquisito", styles["default2-2"]),
                ],
               [Paragraph("<u>__</u>Extraplan", styles["default2-2"]),
                ],
               [Paragraph("<u>__</u>Cambio de Seccion", styles["default2-2"]),
                ]],
              Paragraph("<u>__</u>SI   <u>__</u>NO", styles["blacktitle"]),
              Paragraph(" ", styles["default2"]),
              Paragraph("<u>__</u>", styles["default2"]),
              ]
             ],
            colWidths=[h * inch for h in [0.75, 1.5, 0.75, 1.25, 1, 1.5, 0.75]],
            rowHeights=0.5 * inch,
            style=styles['table_default4'],

        )

    else:

        tbl_prueba = Table(
            [[Paragraph("EP3420", styles["blacktitle"]),
              Paragraph("Pasantia Larga", styles["blacktitle"]),
              Paragraph("<u>__</u>Incluir <u>__</u>Modificar", styles["default2-2"]),
              [[Paragraph("<u>__</u>Requisito/correquisito", styles["default2-2"]),
                ],
               [Paragraph("<u>__</u>Extraplan", styles["default2-2"]),
                ],
               [Paragraph("<u>__</u>Cambio de Seccion", styles["default2-2"]),
                ]],
              Paragraph("<u>__</u>SI   <u>__</u>NO", styles["blacktitle"]),
              Paragraph(" ", styles["default2"]),
              Paragraph("<u>__</u>", styles["default2"]),
              ]
             ],
            colWidths=[h * inch for h in [0.75, 1.5, 0.75, 1.25, 1, 1.5, 0.75]],
            rowHeights=0.5 * inch,
            style=styles['table_default4'],

        )

    story.append(tbl_prueba)

    story.append(Spacer(1, 24))

    tbl_prueba = Table(
        [[Paragraph("", styles["default2"]),
          Paragraph("<b>Observaciones </b>(Coordinación)", styles["blacktitle2"]),
          Paragraph("<b>Dejar sin efecto el tramite</b>", styles["default2"]),
          ]
         ],
        colWidths=[h * inch for h in [1.5, 5.25, 0.75]],
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<u>__</u>SI <u>__</u>NO", styles["blacktitle2"]),
          Paragraph("", styles["blacktitle"]),
          Paragraph("<u>__</u>", styles["default2"]),
          ]
         ],
        colWidths=[h * inch for h in [1.5, 5.25, 0.75]],
        rowHeights=2 * inch,
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    story.append(Spacer(1, 42))

    tbl_prueba = Table(
        [[Paragraph("FIRMA DEL ESTUDIANTE", styles["firma"]),
          Paragraph("FIRMA DEL TUTOR ACADEMICO", styles["firma"]),
          Paragraph("COORDINACIÓN (Firma, sello y fecha)", styles["firma"]),
          ]
         ],
        colWidths=[h * inch for h in [2.5, 2.5, 2.5]],
        rowHeights=1 * inch,
        style=styles['table_firma'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph('''NOTA: Presentar ante la Coordinación tres copias de la planilla debidamente completadas y sin enmiendas (una copia para la Coordinación, una copia para el
expediente en DACE, una copia para el estudiante) junto con la copia del comprobante de inscripción y el arancel correspondiente.
La solicitud está sujeta a su aprobación por parte de la Coordinación docente. Verificar el resultado de la solicitud a través del comprobante de inscripción.
Deberá utilizarse únicamente bolígrafo cuando la planilla no sea llenada en el formato .DOC o .PDF''', styles["default2"]),

          ]
         ],
        colWidths=7.5 * inch,
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    buffer = cStringIO.StringIO()
    doc = SimpleDocTemplate(buffer,pagesize=letter,
                        rightMargin=30,leftMargin=30,
                        topMargin=0,bottomMargin=30)
    doc.build(story)
    pdf = buffer.getvalue()
    buffer.close()

    filename = "Inscripcion Extemporanea"
    header = {'Content-Disposition': 'attachment; filename=' + filename}
    response.headers.update(header)

    return pdf


def generarPdfRetiro():

    carrera = 'Ingenieria Geofisica'
    estudiante = 'Christian Jose Merino Gonzalez'
    carnet = '12-10946'
    cedula = '20.156.258'
    tutor = 'Leonid Tineo'
    telefono = '0416-1234567'
    periodo = 'Julio-Agosto 2016'
    justificacion = '''Debido que, conseguí la pasantía en el período vacacional y me encontraba en el Estado
                        Anzoategui, necesito, obligatoriamente inscribir las pasantías durante la inscripción
                        extemporánea.'''
    codigo = 'b25512fe28'
    pasantia = 'corta'

    width, height = letter

    styles = stylesheet()

    story = []
    logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/images/logo2.png')
    logo = Image(logo_path, width=180, height=120)

    # ENCABEZADO

    tbl_tempo = Table(
        [[Paragraph("Fecha de la Solicitud", styles["default5"]),
          ],
         [Paragraph("<b>PLANILLA DE INSCRIPCIÓN EXTEMPORANEA</b>", styles["default3"]),
          ],
         ],
        rowHeights=[h * inch for h in [0.25, 1]],
        colWidths= 4.5 * inch,
        style=styles['table_encabezado'],

    )

    tbl_prueba = Table(
        [[logo,
          tbl_tempo,
          ]
         ],
        colWidths=[h * inch for h in [2.5, 5]],
        style=styles['table_encabezado'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Datos del Estudiante</b>"
                    , styles["default3"]),
          ],
         ],
        style=styles['table_default6'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Número de Carnet: </b>", styles["default"]),
          Paragraph(carnet, styles["default"]),
          Paragraph("<b>Número de Cédula de Identidad: </b>", styles["default"]),
          Paragraph(cedula, styles["default"]),
          ]
         ],
        colWidths=[h * inch for h in [1.75, 2, 1.75, 2]],
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Nombre del Estudiante: </b>", styles["default"]),
          Paragraph(estudiante, styles["default"]),
          ]
         ],
        colWidths=[h * inch for h in [1.75, 5.75]],
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Carrera: </b>", styles["default"]),
          Paragraph(carrera, styles["default"]),
          ]
         ],
        colWidths=[h * inch for h in [1.75, 5.75]],
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Trimestre: </b>", styles["default"]),
          Paragraph(periodo, styles["default"]),
          Paragraph("<b>Teléfono de contacto: </b>", styles["default"]),
          Paragraph(telefono, styles["default"]),
          ]
         ],
        colWidths=[h * inch for h in [1.75, 2, 1.75, 2]],
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Nombre del Tutor Academico: </b>", styles["default"]),
          Paragraph(tutor, styles["default"]),
          ]
         ],
        colWidths=[h * inch for h in [1.75, 5.75]],
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Datos de la pasantia</b>"
                    , styles["default3"]),
          ],
         ],
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    story.append(Spacer(1, 12))

    tbl_prueba = Table(
        [[Paragraph("<b>Código de asignatura</b>", styles["default2"]),
          Paragraph("<b>Nombre de la asignatura</b>", styles["default2"]),
          Paragraph("<b>Autorizado </b>(Coordinacion)", styles["default2"]),
          Paragraph("<b>Solicitud de cupo </b>(Sección, firma y sello Dpto)", styles["default2"]),
          Paragraph("<b>Dejar sin efecto el tramite</b>", styles["default2"]),
          ]
         ],
        colWidths=[h * inch for h in [1.5, 2.5, 1.25, 1.5, 0.75]],
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    if pasantia == 'corta':

        tbl_prueba = Table(
            [[Paragraph("EP1420", styles["blacktitle2"]),
              Paragraph("Pasantia Corta", styles["blacktitle2"]),
              Paragraph("<u>__</u>SI   <u>__</u>NO", styles["blacktitle2"]),
              Paragraph(" ", styles["default2"]),
              Paragraph("<u>__</u>", styles["default2"]),
              ]
             ],
            colWidths=[h * inch for h in [1.5, 2.5, 1.25, 1.5, 0.75]],
            rowHeights=0.5 * inch,
            style=styles['table_default4'],

        )


    elif pasantia == 'intermedia':

        tbl_prueba = Table(
            [[Paragraph("EP3420", styles["blacktitle2"]),
              Paragraph("Pasantia Larga", styles["blacktitle2"]),
              Paragraph("<u>__</u>SI   <u>__</u>NO", styles["blacktitle2"]),
              Paragraph(" ", styles["default2"]),
              Paragraph("<u>__</u>", styles["default2"]),
              ]
             ],
            colWidths=[h * inch for h in [1.5, 2.5, 1.25, 1.5, 0.75]],
            rowHeights=0.5 * inch,
            style=styles['table_default4'],

        )

    else:

        tbl_prueba = Table(
            [[Paragraph("EP3420", styles["blacktitle2"]),
              Paragraph("Pasantia Larga", styles["blacktitle2"]),
              Paragraph("<u>__</u>SI   <u>__</u>NO", styles["blacktitle2"]),
              Paragraph(" ", styles["default2"]),
              Paragraph("<u>__</u>", styles["default2"]),
              ]
             ],
            colWidths=[h * inch for h in [1.5, 2.5, 1.25, 1.5, 0.75]],
            rowHeights=0.5 * inch,
            style=styles['table_default4'],

        )

    story.append(tbl_prueba)

    story.append(Spacer(1, 24))

    tbl_prueba = Table(
        [[Paragraph("", styles["default2"]),
          Paragraph("<b>Observaciones </b>(Coordinación)", styles["blacktitle2"]),
          Paragraph("<b>Dejar sin efecto el tramite</b>", styles["default2"]),
          ]
         ],
        colWidths=[h * inch for h in [1.5, 5.25, 0.75]],
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<u>__</u>SI <u>__</u>NO", styles["blacktitle2"]),
          Paragraph("", styles["blacktitle"]),
          Paragraph("<u>__</u>", styles["default2"]),
          ]
         ],
        colWidths=[h * inch for h in [1.5, 5.25, 0.75]],
        rowHeights=2 * inch,
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    story.append(Spacer(1, 42))

    tbl_prueba = Table(
        [[Paragraph("FIRMA DEL ESTUDIANTE", styles["firma"]),
          Paragraph("FIRMA DEL TUTOR ACADEMICO", styles["firma"]),
          Paragraph("COORDINACIÓN (Firma, sello y fecha)", styles["firma"]),
          ]
         ],
        colWidths=[h * inch for h in [2.5, 2.5, 2.5]],
        rowHeights=1 * inch,
        style=styles['table_firma'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph('''NOTA: Presentar ante la Coordinación tres copias de la planilla debidamente completadas y sin enmiendas (una copia para la Coordinación, una copia para el
expediente en DACE, una copia para el estudiante) junto con la copia del comprobante de inscripción y el arancel correspondiente.
La solicitud está sujeta a su aprobación por parte de la Coordinación docente. Verificar el resultado de la solicitud a través del comprobante de inscripción.
Deberá utilizarse únicamente bolígrafo cuando la planilla no sea llenada en el formato .DOC o .PDF''', styles["default2"]),

          ]
         ],
        colWidths=7.5 * inch,
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    buffer = cStringIO.StringIO()
    doc = SimpleDocTemplate(buffer,pagesize=letter,
                        rightMargin=30,leftMargin=30,
                        topMargin=0,bottomMargin=30)
    doc.build(story)
    pdf = buffer.getvalue()
    buffer.close()

    filename = "Retiro"
    header = {'Content-Disposition': 'attachment; filename=' + filename}
    response.headers.update(header)

    return pdf
