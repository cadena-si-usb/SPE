# -*- coding: utf-8 -*-
from Pasantias import Pasantia

import Encoder

Pasantia = Pasantia()

def listar():
    session.rows = []

    return dict(rows=session.rows)

def agregar():
    fields = ['nombre','empresa','tutor_industrial','tutor_academico','plan_trabajo','id_estudiante','materia']

    form = Pasantia.form(fields)

    if form.process().accepted:
        session.flash = T('El material fue agregado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()

def count():
    obj = Encoder.to_dict(request.vars)
    count = Pasantia.count(obj)

    return count

def get():
    obj = Encoder.to_dict(request.vars)

    rows = Pasantia.JMaterias(obj)

    rows = rows.as_json()

    return rows

# Verifica que se accedan a los recursos asignados al actor correspondiente 
def chequear_permisologia():
    try:
        userid = str(auth.user['username'])
        estudiante = db.Estudiante(db.Estudiante.carnet == userid)
        pasantia = db.Pasantia(db.Pasantia.estudiante == estudiante['id'])
    except Exception as e:
        return False

    return True


@auth.requires(chequear_permisologia())
def ver():
    pasantia = db.Pasantia(request.args(0)) or redirect(URL('agregar'))
    etapa = db.Etapa(pasantia.etapa)

    if etapa.nombre == 'Inscripcion':
        plan_trabajo = db(db.Plan_Trabajo.pasantia == pasantia.id).select().first()

    response.view = 'mis_pasantias/' + etapa.nombre.lower() + '.html'
    
    return locals()

# Agregar que no puede editar una pasantia que no ha sido inscrita por el
#@auth.requires(chequear_permisologia())
def editar():
    # Obtenemos la pasantia previamente agregada en inscripcion
    #area_proyecto = db.area_proyecto

    fields = [
        'titulo',
#        'area_proyecto',
        'resumen_proyecto',
        'objetivo',
        'confidencialidad'
    ]
    pasantia = db.Pasantia(request.args(0))

    # Cargamos el estudiante que ya esta enlazado a esta pasantia
    # db.Pasantia.estudiante.default = pasantia.estudiante['id']
    # db.Pasantia.estudiante.writable = False

    form = SQLFORM(db.Pasantia,record=pasantia,fields=fields,submit_button='Actualizar',showid=False)

    if form.process().accepted:
        session.flash = T('Pasantia actualizada exitosamente!')
        redirect(URL('editar'))
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()
    
# Nueva ruta    
#@auth.requires(chequear_permisologia())
def planes_trabajo():
    # Obtenemos la pasantia previamente agregada en inscripcion
    pasantia = db.Pasantia(request.args(0))

    return locals()

#@auth.requires(chequear_permisologia())
def preinscribir():
    idMateria = request.args(0)
    currentUser = session.currentUser
    estudiante = db(db.Estudiante.usuario == currentUser.id).select().first()
    etapa = db(db.Etapa.nombre == 'Preinscripcion').select().first()
    periodo = db(db.Periodo).select().first()

    if not estudiante:
        return "ERROR, debes ser estudiante"

    curriculo = db((db.Curriculo.estudiante == estudiante.id) and (db.Curriculo.activo == True)).select().first()

    if not curriculo:
        return "ERROR, debes tener el curriculo lleno"

    tienePasantia = db((db.Pasantia.estudiante == estudiante.id) and (db.Pasantia.materia == idMateria)).select().first()

    if tienePasantia:
        return "ERROR, no puedes tener dos pasantias"

    pasantia = db.Pasantia.insert(estudiante=estudiante.id,materia=idMateria,etapa=etapa.id,periodo=periodo.id)
    preinscripcion = db.Preinscripcion.insert(pasantia=pasantia.id)
    
    redirect(URL('ver', args=(pasantia)))
    
