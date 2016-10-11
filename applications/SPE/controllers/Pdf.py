# -*- coding: utf-8 -*-

import cStringIO

from reportlab.pdfgen import canvas
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch



def generarPdfConstanciaCulminacion():
    """
    To display the generated PDF in your browser go to:
     http://.../<app>/<controller>/generate

    To download it as hello.pdf, for example, instead, use:
     http://.../<app>/<controller>/generate/hello.pdf
    """

    styles = getSampleStyleSheet()
    story = [
        Paragraph("Hello World", styles['Heading1']),
        Paragraph("The quick brown fox", styles['Normal']),
        Spacer(1, 0.25*inch),
        Paragraph("jumps over the lazy dog.", styles['Normal'])]
    buffer = cStringIO.StringIO()
    doc = SimpleDocTemplate(buffer)
    doc.build(story)
    pdf = buffer.getvalue()
    buffer.close()

    filename = request.args(0)
    if filename:
        header = {'Content-Disposition': 'attachment; filename=' + filename}
    else:
        header = {'Content-Type': 'application/pdf'}
    response.headers.update(header)
    return pdf


