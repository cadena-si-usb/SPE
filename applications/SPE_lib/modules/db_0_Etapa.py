# -*- coding: utf-8 -*-
from gluon import *
def Etapa_Table(db,T):
    db.define_table('Etapa',
        Field('first_name','string'),
        Field('procedimientos','string'),
        Field('descripcion','string'),
        format='%(first_name)s')

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