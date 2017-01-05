# -*- coding: utf-8 -*-

# Proceso de registro en el cual un tutor solicita un registro a una Empresa
from shlex import shlex
from applications.SPE.modules.Planes_Trabajo import Plan_Trabajo

Plan_Trabajo=Plan_Trabajo()

@auth.requires(auth.is_logged_in()
               and Plan_Trabajo.esActorDePlan(db,auth.user.id,request.args[0]))
def verDetallePasantia():
    pasantiaId=request.args[0]
    # Buscamos los datos necesarios
    pasantia = db((db.Pasantia.id == pasantiaId)).select().first()
    planTrabajo = pasantia.Plan_Trabajo.select().first()
    # Definimos que no se pueden editar los datos
    for field in db.Pasantia:
        field.writable=False
    # Llenamos Los Campos con los datos encontrados
    db.Pasantia.titulo.default=pasantia.titulo
    db.Pasantia.estudiante.default = pasantia.estudiante
    db.Pasantia.tutor_academico.default = pasantia.tutor_academico
    db.Pasantia.tutor_industrial.default = pasantia.tutor_industrial
    db.Pasantia.periodo.default = pasantia.periodo
    db.Pasantia.area_proyecto.default = pasantia.area_proyecto
    db.Pasantia.resumen_proyecto.default = pasantia.resumen_proyecto
    db.Pasantia.materia.default = pasantia.materia
    db.Pasantia.objetivo.default = pasantia.objetivo
    db.Pasantia.confidencialidad.default = pasantia.confidencialidad
    db.Pasantia.status.default = pasantia.status
    db.Pasantia.etapa.default = pasantia.etapa
    db.Pasantia.fecha_creacion.default = pasantia.fecha_creacion
    db.Pasantia.fecha_inicio.default = pasantia.fecha_inicio
    db.Pasantia.fecha_fin.default = pasantia.fecha_fin
    db.Pasantia.fecha_tope_jurado.default = pasantia.fecha_tope_jurado
    db.Pasantia.fecha_defensa.default = pasantia.fecha_defensa
    # Definimos que no se pueden editar los datos
    for field in db.Plan_Trabajo:
        field.writable=False
    # Si existe el plan de trabajo repetimos el proceso con el plan de trabajo
    if (planTrabajo):
        db.Plan_Trabajo.aprobacion_tutor_academico.default = planTrabajo.aprobacion_tutor_academico
        db.Plan_Trabajo.aprobacion_tutor_industrial.default = planTrabajo.aprobacion_tutor_industrial
        db.Plan_Trabajo.aprobacion_coordinacion.default = planTrabajo.aprobacion_coordinacion
        db.Plan_Trabajo.fecha_creacion.default = planTrabajo.fecha_creacion
        db.Plan_Trabajo.fecha_envio.default = planTrabajo.fecha_envio
        db.Plan_Trabajo.estado.default = planTrabajo.estado
    # Creamos Los forms con lso que mostraremos los datos
    formPasantia = SQLFORM.factory(db.Pasantia, db.Plan_Trabajo, fields=None, showid=False)
    formPlanTrabajo = SQLFORM.factory(db.Pasantia, db.Plan_Trabajo, fields=None, showid=False)
    response.view = 'Pasantia/Detalle_Pasantia.html'
    return locals()

@auth.requires(auth.is_logged_in()
               and Plan_Trabajo.esActorDePlan(db,auth.user.id,request.args[0])
               and not Plan_Trabajo.comprobarPlanAprobado(db,request.args[0]))
def crudPasantia():
    pasantia = db(db.Pasantia.id == request.args[0]).select().first()
    # Quitamos los campo que no se deben modificar
    db.Pasantia.etapa.writable = False
    db.Pasantia.status.writable = False
    db.Pasantia.fecha_creacion.writable = False
    db.Pasantia.fecha_inicio.writable = False
    db.Pasantia.fecha_fin.writable = False
    db.Pasantia.fecha_tope_jurado.writable = False
    db.Pasantia.fecha_defensa.writable = False
    db.Pasantia.estudiante.writable = False
    # Quitamos los campo que no se deben leer
    db.Pasantia.etapa.readable = False
    db.Pasantia.status.readable = False
    db.Pasantia.fecha_creacion.readable = False
    db.Pasantia.fecha_inicio.readable = False
    db.Pasantia.fecha_fin.readable = False
    db.Pasantia.fecha_tope_jurado.readable = False
    db.Pasantia.fecha_defensa.readable = False
    db.Pasantia.estudiante.readable = False
    # Solo el estudiante puede cambiar al resto de los actores
    if not auth.has_membership(role='Estudiante'):
        db.Pasantia.tutor_industrial.writable = False
        db.Pasantia.tutor_academico.writable = False
        db.Pasantia.tutor_industrial.readable = False
        db.Pasantia.tutor_academico.readable = False
    # Creo el formulario
    form = SQLFORM(db.Pasantia, pasantia,showid=False)
    if form.process().accepted:
        response.flash = 'form accepted'
        # Reprobamos el plan de trabajo para que deba ser revisado por todos los actores de nuevo
        Plan_Trabajo.reprobar(id=request.args[0])
        redirect(URL(c='Pasantia',f='verDetallePasantia', args=[request.args[0]],vars=dict(pasantiaId=request.args[0])))
    elif form.errors:
        response.flash = 'form has errors'
    # Definimos la vista que vamos a renderizar
    response.view='Pasantia/crudPasantia.html'
    return locals()

@auth.requires(auth.is_logged_in()
               and Plan_Trabajo.esActorDePlan(db,auth.user.id,request.args[0])
               and not Plan_Trabajo.comprobarPlanAprobado(db,request.args[0]))
def verPlanDeTrabajo():
    pasantiaId=request.args[0]
    # Obtenemos el objeto de pasantia
    pasantia = db((db.Pasantia.id == pasantiaId)).select().first()
    # Obtenemos el plan de trabajo
    planTrabajo = pasantia.Plan_Trabajo.select().first()
    # Obtenemos las fases del plan de trabajo
    fases=planTrabajo.Fase.select(orderby=db.Fase.numero)
    # Verificamos si el plan ya fue aprobado, si no es asi entonces puede ser editado por el tutor industrial
    editable=(planTrabajo.aprobacion_coordinacion=='Aprobado'
              and planTrabajo.aprobacion_tutor_academico=='Aprobado'
              and planTrabajo.aprobacion_tutor_industrial=='Aprobado')

    if auth.user.id==pasantia.estudiante:
        response.view = 'Pasantia/Detalle_Plan_De_Trabajo_estudiante.html'
    elif auth.user.id==pasantia.tutor_academico:
        response.view = 'Pasantia/Detalle_Plan_De_Trabajo_tutor.html'
    else:
        response.view = 'Pasantia/Detalle_Plan_De_Trabajo_coordinador.html'

    return locals()

@auth.requires(auth.is_logged_in()
               and Plan_Trabajo.esActorDePlan(db,auth.user.id,request.args[0])
               and not Plan_Trabajo.comprobarPlanAprobado(db,request.args[0]))
def crudFase():
    db.Fase.plan_trabajo.readable=False
    db.Fase.plan_trabajo.writable = False
    if len(request.args)==1:
        db.Fase.plan_trabajo.default=request.args[0]
        record = None
    else:
        record = db.Fase(request.args[1])

    pasantia = db(db.Pasantia.id == request.args[0]).select().first()
    db.Actividad.fase.writable = False
    form = SQLFORM(db.Fase, record,showid=False)
    if form.process().accepted:
        response.flash = 'form accepted'
        # Reprobamos el plan de trabajo para que deba ser revisado por todos los actores de nuevo
        Plan_Trabajo.reprobar(id=request.args[0])
        redirect(URL(c='Pasantia',f='verPlanDeTrabajo', args=[request.args[0]],vars=dict(planId=request.args[0])))
    elif form.errors:
        response.flash = 'form has errors'
    # Definimos la vista que vamos a renderizar
    response.view='Pasantia/crudFase.html'
    return locals()

@auth.requires(auth.is_logged_in()
               and Plan_Trabajo.esActorDePlan(db,auth.user.id,request.args[0])
               and not Plan_Trabajo.comprobarPlanAprobado(db,request.args[0]))
def eliminarFase():
    # Creamos el formulario
    form = FORM.confirm('¿Esta Seguro Que Desea Eliminar Esta Fase?', {'Retornar': URL('verPlanDeTrabajo',args=[request.vars.planId],vars=dict(planId=request.vars.planId))})
    # Buscamos informacion de la pasantia
    fase = db.Fase(id=request.args[1])
    # Buscamos informacion de la pasantia
    pasantia = db(db.Pasantia.id==fase.plan_trabajo).select().first()
    if form.accepted:
        # Eliminamos la pasantia
        fase.delete_record()
        # Reprobamos el plan de trabajo para que deba ser revisado por todos los actores de nuevo
        Plan_Trabajo.reprobar(id=request.args[0])
        # Retornamos a la vista de plan de trabajo
        redirect(URL(c='Pasantia',f='verPlanDeTrabajo',args=[request.args[0]]))
    # Definimos la vista que vamos a renderizar
    response.view = 'Pasantia/eliminarFase.html'
    return locals()

@auth.requires(auth.is_logged_in()
               and Plan_Trabajo.esActorDePlan(db,auth.user.id,request.args[0])
               and not Plan_Trabajo.comprobarPlanAprobado(db,request.args[0]))
def crudActividad():
    # Buscamos informacion de la pasantia
    record = None
    # Si no existe definimos que pertenecera a la fase que estamos trabajando
    if len(request.args)==2:
        db.Actividad.fase.default=request.args[1]
        record = None
    else:
        record = db.Actividad(request.args[2])
    pasantia=db(db.Pasantia.id==request.args[0]).select().first()
    duracion=pasantia.materia.duracion

    rango=range(1,duracion+1,1)

    db.Actividad.semana_inicio.requires=IS_IN_SET(rango,zero=None)
    db.Actividad.semana_fin.requires = IS_IN_SET(rango,zero=None)

    # Marcamos la referencia a la fase como no legible o escribible ya que no le proporcionan informacion util al
    # usuario
    db.Actividad.fase.writable = False
    db.Actividad.fase.readable = False
    # Buscamos informacion de la pasantia
    pasantia = db(db.Pasantia.id == request.args[0]).select().first()
    # Buscamos informacion de la pasantia
    fase = db.Fase(id=request.args[1])
    # Creamos el formulario
    form = SQLFORM(db.Actividad, record,showid=False)
    if form.process().accepted:
        response.flash = 'form accepted'
        # Reprobamos el plan de trabajo para que deba ser revisado por todos los actores de nuevo
        Plan_Trabajo.reprobar(id=request.args[0])
        redirect(URL(c='Pasantia',f='verPlanDeTrabajo',args=[request.args[0]]))
    elif form.errors:
        response.flash = 'form has errors'
    # Definimos la vista que vamos a renderizar
    response.view = 'Pasantia/crudActividad.html'
    return locals()

@auth.requires(auth.is_logged_in()
               and Plan_Trabajo.esActorDePlan(db,auth.user.id,request.args[0])
               and not Plan_Trabajo.comprobarPlanAprobado(db,request.args[0]))
def eliminarActividad():
    form = FORM.confirm('¿Esta Seguro Que Desea Eliminar Esta Actividad?', {'Retornar': URL('verPlanDeTrabajo',args=[request.vars.planId])})
    fase = db.Fase(id=request.args[1])
    actividad = db.Actividad(id=request.args[2])
    pasantia = db(db.Pasantia.id == fase.plan_trabajo).select().first()
    if form.accepted:
        actividad.delete_record()
        # Reprobamos el plan de trabajo para que deba ser revisado por todos los actores de nuevo
        Plan_Trabajo.reprobar(id=request.args[0])
        redirect(URL(c='Pasantia',f='verPlanDeTrabajo',args=[request.args[0]]))
    # Definimos la vista que vamos a renderizar
    response.view = 'Pasantia/eliminarActividad.html'
    return locals()

@auth.requires(auth.is_logged_in()
               and Plan_Trabajo.esActorDePlan(db,auth.user.id,request.args[0])
               and not Plan_Trabajo.comprobarPlanAprobado(db,request.args[0]))
def AprobarPlanTrabajoTutorAcademico():
    plan_trabajo = db.Plan_Trabajo(id=request.args[0])
    plan_trabajo.update_record(aprobacion_tutor_academico="Aprobado")
    redirect(URL(c='Pasantia',f='verPlanDeTrabajo', args=[request.args[0]]))
    return locals()

@auth.requires(auth.is_logged_in()
               and Plan_Trabajo.esActorDePlan(db,auth.user.id,request.args[0])
               and not Plan_Trabajo.comprobarPlanAprobado(db,request.args[0]))
def AprobarPlanTrabajoCoordinador():
    plan_trabajo = db.Plan_Trabajo(id=request.args[0])
    plan_trabajo.update_record(aprobacion_coordinacion="Aprobado")
    redirect(URL(c='Pasantia',f='verPlanDeTrabajo', args=[request.args[0]]))
    return locals()

@auth.requires(auth.is_logged_in()
               and Plan_Trabajo.esActorDePlan(db,auth.user.id,request.args[0])
               and not Plan_Trabajo.comprobarPlanAprobado(db,request.args[0]))
def enviarPlanTrabajo():
    plan_trabajo = db.Plan_Trabajo(id=request.args[0])
    plan_trabajo.update_record(estado="Enviado",fecha_envio=request.now)
    redirect(URL(c='Pasantia',f='verPlanDeTrabajo', args=[request.args[0]]))
    return locals()

@auth.requires(auth.is_logged_in() and auth.has_membership(role='Coordinador'))
def consultarPasantias():
    userId=auth.user.id
    coordinador=db.Coordinador(id=userId)
    coordinacion=db.Coordinacion(id=coordinador.coordinacion)
    carrera=db.Carrera(coordinacion=coordinacion.id)
    email = auth.user.email
    pasantias=db((db.Estudiante.id==db.Pasantia.estudiante) & (db.Estudiante.carrera==carrera.id))

    prueba=pasantias.select().first()

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

    response.view = 'Coordinador/Consultar_Pasantias.html'
    return locals()