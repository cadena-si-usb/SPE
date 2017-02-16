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
        fontSize=9,
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
            ('INNERGRID', (0, 0), (-1, -1), 1, gray),
            ('LINEABOVE', (0, 0), (-1, -1), 1, black),
            ('LINEBEFORE', (0, 0), (-1, -1), 1, black),
            ('LINEAFTER', (0, 0), (-1, -1), 1, black),
            ('LINEBELOW', (0, 0), (-1, -1), 1, black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

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
            ('LINEABOVE', (0, 0), (-1, -1), 1, black),
            ('LINEBEFORE', (0, 0), (-1, -1), 1, black),
            ('LINEAFTER', (0, 0), (-1, -1), 1, black),
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


    return styles


def generarPdfInscripcionExtemporanea():

    coordinacion = 'Ingenieria Geofisica'
    estudiante = 'Christian Jose Merino Gonzalez'
    carnet = '12-10946'
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
    tbl_cabeza = [
        [logo,
         Paragraph("<b>PERMISO PARA PASANTIA</b>", styles["default3"]),
         Paragraph("", styles["default4"]),
         ],
    ]

    tbl_cab = Table(tbl_cabeza, colWidths=[2.5 * inch])
    story.append(tbl_cab)
    story.append(Paragraph("<b>Inscripcion Extemporanea</b>", styles["default3"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>COORDINACION DE: </b>" + coordinacion, styles["blacktitle"]))
    story.append(Spacer(1, 6))
    tbl_estudiante = [
        [Paragraph("<b>Nombre del Estudiante: </b>" + estudiante, styles["blacktitle"]),
         Paragraph("<b>Carnet: </b>" + carnet, styles["blacktitle"]),
         ],
    ]
    tbl_est = Table(tbl_estudiante, colWidths=[h * inch for h in [4.5, 3]])
    story.append(tbl_est)

    story.append(Spacer(1, 24))

    tbl_prueba = Table(
        [[Paragraph("<b>PASANTIA</b>"
                    , styles["default3"]),
          ],
         ],
        style=styles['table_default6'],

    )

    story.append(tbl_prueba)

    if pasantia == 'corta':
        tbl_prueba = Table(
            [[Spacer(1, 5),
              ],
             [Paragraph("<b>CORTA(EP1420)<u>_X_</u>INTERMEDIA(EP2420)<u>__</u>LARGA(EP3420)<u>__</u></b>"
                        , styles["default3"]),
              ],
             [Spacer(1, 5),
              ],
             ],
            style=styles['table_default7'],

        )
    elif pasantia == 'intermedia':
        tbl_prueba = Table(
            [[Spacer(1, 5),
              ],
             [Paragraph("<b>CORTA(EP1420)<u>__</u>INTERMEDIA(EP2420)<u>_X_</u>LARGA(EP3420)<u>__</u></b>"
                        , styles["default3"]),
              ],
             [Spacer(1, 5),
              ],
             ],
            style=styles['table_default7'],

        )
    else:
        tbl_prueba = Table(
            [[Spacer(1, 5),
              ],
             [Paragraph("<b>CORTA(EP1420)<u>__</u>INTERMEDIA(EP2420)<u>__</u>LARGA(EP3420)<u>_X_</u></b>"
                        , styles["default3"]),
              ],
             [Spacer(1, 5),
              ],
             ],
            style=styles['table_default7'],

        )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Periodo: </b>" + periodo, styles["default3"]),
          ],
         [Spacer(1, 5),
          ],
         ],
        style=styles['table_default7'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>TUTOR ACADEMICO</b>", styles["blacktitle"]),
          Paragraph("Nombre:", styles["blacktitle"]),
          Paragraph("Firma:<u>___________________</u>", styles["blacktitle"]),
          ]
         ],
        colWidths=[h * inch for h in [2, 3, 2.5]],
        rowHeights=0.75 * inch,
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Justificacion:</b>", styles["default4"]),
          ],
         [Paragraph(justificacion, styles["default"]),
         ],
         ],
        rowHeights=[h * inch for h in [0.5, 2]],
        style=styles['table_default8'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Observaciones CCT:</b>", styles["default4"]),
          Paragraph("Vo Bo. Firma y sello de Coordinación de Carrera Fecha:", styles["default4"]),
          Paragraph("Firma del Coordinador de CCT Fecha:", styles["default4"]),
          ],
         ],
        colWidths=[h * inch for h in [3, 2.20, 2.30]],
        rowHeights=2.25 * inch,
        style=styles['table_default5'],

    )

    story.append(tbl_prueba)

    story.append(Spacer(1, 12))
    story.append(Paragraph("<b><i>Puerta de Comunidad a Comunidad</i></b>", styles["bluetitle2"]))
    story.append(Paragraph("<b>Codigo Seguridad:</b>" + codigo, styles["default"]))
    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Sartenejas, Baruta, Edif. Comunicaciones Telf: (0212) 906.3157 al 64 Apartado postal 89000, Zip Code 1080-A. www.usb.ve</b>", styles["bluetitle"]))



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


def generarPdfEvaluacionExtemporanea():

    coordinacion = 'Ingenieria Mecanica'
    estudiante = 'Erick Jose Vianello Schloeter'
    carnet = '10-10763'
    periodo = 'Julio-Agosto 2016'
    justificacion = ''' '''
    codigo = 'b25512fe28'
    pasantia = 'intermedia'

    width, height = letter

    styles = stylesheet()

    story = []
    logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/images/logo2.png')
    logo = Image(logo_path, width=180, height=120)

    # ENCABEZADO
    tbl_cabeza = [
        [logo,
         Paragraph("<b>PERMISO PARA PASANTIA</b>", styles["default3"]),
         Paragraph("", styles["default4"]),
         ],
    ]

    tbl_cab = Table(tbl_cabeza, colWidths=[2.5 * inch])
    story.append(tbl_cab)
    story.append(Paragraph("<b>Evaluacion Extemporanea</b>", styles["default3"]))
    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>COORDINACION DE: </b>" + coordinacion, styles["blacktitle"]))
    story.append(Spacer(1, 6))
    tbl_estudiante = [
        [Paragraph("<b>Nombre del Estudiante: </b>" + estudiante, styles["blacktitle"]),
         Paragraph("<b>Carnet: </b>" + carnet, styles["blacktitle"]),
         ],
    ]
    tbl_est = Table(tbl_estudiante, colWidths=[h * inch for h in [4.5, 3]])
    story.append(tbl_est)
    story.append(Spacer(1, 6))
    tbl_prueba = [
        [Paragraph("<b>Fecha Propuesta: </b>", styles["default3"]),
         ],
    ]
    tbl_pru = Table(tbl_prueba, colWidths=[h * inch for h in [4.5, 3]])
    story.append(tbl_pru)
    story.append(Spacer(1, 6))

    tbl_prueba = Table(
        [[Paragraph("<b>PASANTIA</b>"
                    , styles["default3"]),
          ],
         ],
        style=styles['table_default6'],

    )

    story.append(tbl_prueba)

    if pasantia == 'corta':
        tbl_prueba = Table(
            [[Spacer(1, 5),
              ],
             [Paragraph("<b>CORTA(EP1420)<u>_X_</u>INTERMEDIA(EP2420)<u>__</u>LARGA(EP3420)<u>__</u></b>"
                        , styles["default3"]),
              ],
             [Spacer(1, 5),
              ],
             ],
            style=styles['table_default7'],

        )
    elif pasantia == 'intermedia':
        tbl_prueba = Table(
            [[Spacer(1, 5),
              ],
             [Paragraph("<b>CORTA(EP1420)<u>__</u>INTERMEDIA(EP2420)<u>_X_</u>LARGA(EP3420)<u>__</u></b>"
                        , styles["default3"]),
              ],
             [Spacer(1, 5),
              ],
             ],
            style=styles['table_default7'],

        )
    else:
        tbl_prueba = Table(
            [[Spacer(1, 5),
              ],
             [Paragraph("<b>CORTA(EP1420)<u>__</u>INTERMEDIA(EP2420)<u>__</u>LARGA(EP3420)<u>_X_</u></b>"
                        , styles["default3"]),
              ],
             [Spacer(1, 5),
              ],
             ],
            style=styles['table_default7'],

        )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Periodo: </b>" + periodo, styles["default3"]),
          ],
         [Spacer(1, 5),
          ],
         ],
        style=styles['table_default7'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>TUTOR ACADEMICO</b>", styles["blacktitle"]),
          Paragraph("Nombre:", styles["blacktitle"]),
          Paragraph("Firma:<u>___________________</u>", styles["blacktitle"]),
          ]
         ],
        colWidths=[h * inch for h in [2, 3, 2.5]],
        rowHeights=0.75 * inch,
        style=styles['table_default4'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Justificacion:</b>", styles["default4"]),
          ],
         [Paragraph(justificacion, styles["default"]),
         ],
         ],
        rowHeights=[h * inch for h in [0.5, 2]],
        style=styles['table_default8'],

    )

    story.append(tbl_prueba)

    tbl_prueba = Table(
        [[Paragraph("<b>Observaciones CCT:</b>", styles["default4"]),
          Paragraph("Vo Bo. Firma y sello de Coordinación de Carrera Fecha:", styles["default4"]),
          Paragraph("Firma del Coordinador de CCT Fecha:", styles["default4"]),
          ],
         ],
        colWidths=[h * inch for h in [3, 2.20, 2.30]],
        rowHeights=2.25 * inch,
        style=styles['table_default5'],

    )

    story.append(tbl_prueba)

    story.append(Spacer(1, 12))
    story.append(Paragraph("<b><i>Puerta de Comunidad a Comunidad</i></b>", styles["bluetitle2"]))
    story.append(Paragraph("<b>Codigo Seguridad:</b>" + codigo, styles["default"]))
    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Sartenejas, Baruta, Edif. Comunicaciones Telf: (0212) 906.3157 al 64 Apartado postal 89000, Zip Code 1080-A. www.usb.ve</b>", styles["bluetitle"]))



    buffer = cStringIO.StringIO()
    doc = SimpleDocTemplate(buffer,pagesize=letter,
                        rightMargin=30,leftMargin=30,
                        topMargin=0,bottomMargin=30)
    doc.build(story)
    pdf = buffer.getvalue()
    buffer.close()

    filename = "Evaluacion Extemporanea"
    header = {'Content-Disposition': 'attachment; filename=' + filename}
    response.headers.update(header)

    return pdf