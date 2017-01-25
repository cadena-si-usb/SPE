# -*- coding: utf-8 -*-
from Pasantias import Pasantia

import Encoder

Pasantia = Pasantia()

# Hacer para el caso en el que el actor sea tutor academico
def listar():
    session.rows = []

    return dict(rows=session.rows)

def agregar():
    fields = ['first_name','empresa','tutor_industrial','tutor_academico','plan_trabajo','id_estudiante','materia']

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
        userid = auth.user.id
        estudiante = db.Estudiante(usuario= userid)
        pasantia = db.Pasantia(estudiante=estudiante.id)
    except Exception as e:
        return False

    return True


#@auth.requires(chequear_permisologia())
def ver():
    pasantia = db.Pasantia(request.args(0)) or redirect(URL('agregar'))
    etapa = db.Etapa(pasantia.etapa)

    if etapa.first_name == 'Inscripcion':
        inscripcion=db.Inscripcion(pasantia= pasantia.id)
        plan_trabajo = db.Plan_Trabajo(pasantia=pasantia.id)
    elif etapa.first_name == 'Colocacion':
        colocacion=db.Colocacion(pasantia=pasantia.id)
    elif etapa.first_name == 'Preinscripcion':
        preinscripcion = db.Preinscripcion(pasantia=pasantia.id)
    elif etapa.first_name == 'Ejecucion':
        ejecucion = db.Ejecucion(pasantia=pasantia.id)

    response.view = 'mis_pasantias/' + etapa.first_name.lower() + '.html'
    
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
    user = auth.user
    estudiante = db.Estudiante(usuario=user.id)
    etapa = db.Etapa(first_name= 'Preinscripcion')
    periodo = db(db.Periodo).select().first()

    if not estudiante:
        return "ERROR, debes ser estudiante"
    curriculo = db.Curriculo(estudiante= estudiante.id,activo= True)

    if not curriculo:
        return "ERROR, debes tener el curriculo lleno"
    tienePasantia = db.Pasantia(estudiante=estudiante.id,materia=idMateria)
    if tienePasantia:
        return "ERROR, no puedes tener dos pasantias"

    pasantia = db.Pasantia.insert(estudiante=estudiante.id,materia=idMateria,etapa=etapa.id,periodo=periodo.id)
    preinscripcion = db.Preinscripcion.insert(pasantia=pasantia.id)
    
    redirect(URL('ver', args=(pasantia)))
    
@auth.requires(auth.is_logged_in() and auth.has_membership(role='Profesor'))
def consultar_pasantias_profesor():
    response.view = 'mis_pasantias/consultar_pasantias_profesor.html'
    return locals()

@auth.requires(auth.is_logged_in() and auth.has_membership(role='Profesor'))
def pasantias_grid_profesor():
    userId=auth.user.id
    profesor = db.Profesor(usuario=userId)
    email = auth.user.email
    pasantias=db((profesor.id==db.Pasantia.tutor_academico))

    #Define the fields to show on grid. Note: (you need to specify id field in fields section in 1.99.2
    # this is not required in later versions)
    fields = (db.Pasantia.titulo, db.Pasantia.estudiante,db.Pasantia.etapa, db.Pasantia.status)

    #Define headers as tuples/dictionaries
    headers = {
            ''
            'Pasantia.titulo': 'Titulo',
            'Pasantia.estudiante':'Estudiante',
            'Pasantia.etapa':'Etapa',
            'Pasantia.status': 'Status' }

    #Let's specify a default sort order on date_of_birth column in grid
    default_sort_order=[db.Pasantia.titulo]
    links = [lambda row: A('Detalle', _href=URL(c='Pasantia',f='verDetallePasantia',args=[row.id]))]

    #Creating the grid object
    form = SQLFORM.grid(query=pasantias, fields=fields, headers=headers, orderby=default_sort_order,
                create=False, deletable=False, editable=False, maxtextlength=64, paginate=25,details=False,
                links=links,csv=False,user_signature=False)

    return form

@auth.requires(auth.is_logged_in() and auth.has_membership(role='Coordinador'))
def consultar_pasantias_coordinador():
    userId=auth.user.id
    coordinador=db.Coordinador(id=userId)
    coordinacion=db.Coordinacion(id=coordinador.coordinacion)
    response.view = 'mis_pasantias/consultar_pasantias_coordinador.html'
    return locals()

@auth.requires(auth.is_logged_in() and auth.has_membership(role='Coordinador'))
def pasantias_grid_coordinador():
    userId = auth.user.id
    coordinador = db.Coordinador(id=userId)
    coordinacion = db.Coordinacion(id=coordinador.coordinacion)
    carrera = db.Carrera(coordinacion=coordinacion.id)
    email = auth.user.email
    pasantias = db((db.Estudiante.id == db.Pasantia.estudiante) & (db.Estudiante.carrera == carrera.id))

    # Define the fields to show on grid. Note: (you need to specify id field in fields section in 1.99.2
    # this is not required in later versions)
    fields = (db.Pasantia.titulo, db.Pasantia.estudiante, db.Pasantia.etapa, db.Pasantia.status)

    # Define headers as tuples/dictionaries
    headers = {
        ''
        'Pasantia.titulo': 'Titulo',
        'Pasantia.estudiante': 'Estudiante',
        'Pasantia.etapa': 'Etapa',
        'Pasantia.status': 'Status'
    }

    # Let's specify a default sort order on date_of_birth column in grid
    default_sort_order = [db.Pasantia.titulo]
    links = [lambda row: A('Detalle', _href=URL(c='Pasantia', f='verDetallePasantia', args=[row.id]))]

    # Creating the grid object
    form = SQLFORM.grid(query=pasantias, fields=fields, headers=headers, orderby=default_sort_order,
                        create=False, deletable=False, editable=False, maxtextlength=64, paginate=25, details=False,
                        links=links, csv=False, user_signature=False)
    return form

@auth.requires(auth.is_logged_in() and auth.has_membership(role='Estudiante'))
def consultar_pasantias_estudiante():
    pasantia_abierta = not db(db.Pasantia.status!='Culminada').isempty()
    response.view = 'mis_pasantias/consultar_pasantias_estudiante.html'
    return locals()

@auth.requires(auth.is_logged_in() and auth.has_membership(role='Estudiante'))
def pasantias_grid_estudiante():
    userId = auth.user.id
    email = auth.user.email
    pasantias = db((db.Estudiante.id == db.Pasantia.estudiante) & (db.Estudiante.usuario == userId))
    # Define the fields to show on grid. Note: (you need to specify id field in fields section in 1.99.2
    # this is not required in later versions)
    fields = (db.Pasantia.titulo, db.Pasantia.estudiante, db.Pasantia.etapa, db.Pasantia.status)

    # Define headers as tuples/dictionaries
    headers = {
        ''
        'Pasantia.titulo': 'Titulo',
        'Pasantia.estudiante': 'Estudiante',
        'Pasantia.etapa': 'Etapa',
        'Pasantia.status': 'Status'
    }

    # Let's specify a default sort order on date_of_birth column in grid
    default_sort_order = [db.Pasantia.titulo]
    links = [lambda row: A('Detalle', _href=URL(c='mis_pasantias', f='ver', args=[row.id]))]

    # Creating the grid object
    form = SQLFORM.grid(query=pasantias, fields=fields, headers=headers, orderby=default_sort_order,
                        create=False, deletable=False, editable=False, maxtextlength=64, paginate=25, details=False,
                        links=links, csv=False, user_signature=False)
    return form