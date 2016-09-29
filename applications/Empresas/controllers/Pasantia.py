# -*- coding: utf-8 -*-

# Proceso de registro en el cual un tutor solicita un registro a una Empresa
from shlex import shlex

@auth.requires_login()
def verDetallePasantia():
    pasantiaId=request.vars.pasantiaId
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

@auth.requires_login()
def verPlanDeTrabajo():
    pasantiaId=request.vars.pasantiaId
    if pasantiaId is None:
        pasantiaId=request.vars.planId
    # Obtenemos el objeto de pasantia
    pasantia = db((db.Pasantia.id == pasantiaId)).select().first()
    # Obtenemos el plan de trabajo
    planTrabajo = pasantia.Plan_Trabajo.select().first()
    # Obtenemos las fases del plan de trabajo
    fases=planTrabajo.Fase.select()
    # Verificamos si el plan ya fue aprobado, si no es asi entonces puede ser editado por el tutor industrial
    editable=(planTrabajo.aprobacion_coordinacion=='Aprobado'
              and planTrabajo.aprobacion_tutor_academico=='Aprobado'
              and planTrabajo.aprobacion_tutor_industrial=='Aprobado')
    response.view = 'Pasantia/Detalle_Plan_De_Trabajo.html'
    return locals()

@auth.requires_login()
def verPerfil():
    usuarioExterno = db(db.UsuarioExterno, (auth.user.id == db.UsuarioExterno.auth_User)).select().first()
    tutor = db(db.Tutor_Industrial, (db.Tutor_Industrial.usuario == db.UsuarioExterno.id)).select().first()

    db.UsuarioExterno.correo.default = usuarioExterno.correo
    db.UsuarioExterno.clave.default = usuarioExterno.clave
    db.UsuarioExterno.pregunta_secreta.default = usuarioExterno.pregunta_secreta
    db.UsuarioExterno.respuesta_secreta.default = usuarioExterno.respuesta_secreta
    db.UsuarioExterno.nombre.default = usuarioExterno.nombre
    db.UsuarioExterno.pais.default = usuarioExterno.pais
    db.UsuarioExterno.estado.default = usuarioExterno.estado

    db.Tutor_Industrial.apellido.default = tutor.apellido
    db.Tutor_Industrial.Empresa.default = tutor.Empresa
    db.Tutor_Industrial.profesion.default = tutor.profesion
    db.Tutor_Industrial.tipo_documento.default = tutor.tipo_documento
    db.Tutor_Industrial.numero_documento.default = tutor.numero_documento
    db.Tutor_Industrial.cargo.default = tutor.cargo
    db.Tutor_Industrial.departamento.default = tutor.departamento
    db.Tutor_Industrial.universidad.default = tutor.universidad
    db.UsuarioExterno.direccion.default = usuarioExterno.direccion
    db.UsuarioExterno.telefono.default = usuarioExterno.telefono

    for field in db.UsuarioExterno:
        field.writable=False
    for field in db.Tutor_Industrial:
        field.writable=False

    fields = [
        'correo',
        'nombre',
        'apellido',
        'tipo_documento',
        'numero_documento',
        'clave',
        'Empresa',
        'pregunta_secreta',
        'respuesta_secreta',
        'profesion',
        'cargo',
        'departamento',
        'pais',
        'estado',
        'universidad',
        'direccion',
        'telefono'
    ]
    form = SQLFORM.factory(db.UsuarioExterno, db.Tutor_Industrial, fields=fields, submit_button='Actualizar', showid=False)

    response.view = 'Pasantia/perfil_Tutor_Industrial.html'
    return locals()

@auth.requires_login()
def crudFase():
    db.Fase.plan_trabajo.readable=False
    db.Fase.plan_trabajo.writable = False
    record = db.Fase(request.vars.faseId)
    if record is None:
        db.Fase.plan_trabajo.default=request.vars.planId
    pasantia = db(db.Pasantia.id == request.vars.planId).select().first()
    db.Actividad.fase.writable = False
    form = SQLFORM(db.Fase, record,showid=False)
    if form.process().accepted:
        response.flash = 'form accepted'
        # Reprobamos el plan de trabajo para que deba ser revisado por todos los actores de nuevo
        reprobar()
        redirect(URL(c='Pasantia',f='verPlanDeTrabajo', vars=dict(planId=request.vars.planId)))
    elif form.errors:
        response.flash = 'form has errors'
    # Definimos la vista que vamos a renderizar
    response.view='Pasantia/crudFase.html'
    return locals()

@auth.requires_login()
def eliminarFase():
    # Creamos el formulario
    form = FORM.confirm('¿Esta Seguro Que Desea Eliminar Esta Fase?', {'Retornar': URL('verPlanDeTrabajo',vars=dict(planId=request.vars.planId))})
    # Buscamos informacion de la pasantia
    fase = db.Fase(id=request.vars.faseId)
    # Buscamos informacion de la pasantia
    pasantia = db(db.Pasantia.id==fase.plan_trabajo).select().first()
    if form.accepted:
        # Eliminamos la pasantia
        fase.delete_record()
        # Reprobamos el plan de trabajo para que deba ser revisado por todos los actores de nuevo
        reprobar()
        # Retornamos a la vista de plan de trabajo
        redirect(URL(c='Pasantia',f='verPlanDeTrabajo',vars=dict(planId=request.vars.planId)))
    # Definimos la vista que vamos a renderizar
    response.view = 'Pasantia/eliminarFase.html'
    return locals()

@auth.requires_login()
def crudActividad():
    # Buscamos informacion de la pasantia
    record = db.Actividad(request.vars.actId)
    # Si no existe definimos que pertenecera a la fase que estamos trabajando
    if record is None:
        db.Actividad.fase.default=request.vars.faseId
    # Marcamos la referencia a la fase como no legible o escribible ya que no le proporcionan informacion util al
    # usuario
    db.Actividad.fase.writable = False
    db.Actividad.fase.readable = False
    # Buscamos informacion de la pasantia
    pasantia = db(db.Pasantia.id == request.vars.planId).select().first()
    # Buscamos informacion de la pasantia
    fase = db.Fase(id=request.vars.faseId)
    # Creamos el formulario
    form = SQLFORM(db.Actividad, record,showid=False)
    if form.process().accepted:
        response.flash = 'form accepted'
        # Reprobamos el plan de trabajo para que deba ser revisado por todos los actores de nuevo
        reprobar()
        redirect(URL(c='Pasantia',f='verPlanDeTrabajo', vars=dict(planId=request.vars.planId)))
    elif form.errors:
        response.flash = 'form has errors'
    # Definimos la vista que vamos a renderizar
    response.view = 'Pasantia/crudActividad.html'
    return locals()

@auth.requires_login()
def eliminarActividad():
    form = FORM.confirm('¿Esta Seguro Que Desea Eliminar Esta Actividad?', {'Retornar': URL('verPlanDeTrabajo',vars=dict(planId=request.vars.planId))})
    fase = db.Fase(id=request.vars.faseId)
    actividad = db.Actividad(id=request.vars.actId)
    pasantia = db(db.Pasantia.id == fase.plan_trabajo).select().first()
    if form.accepted:
        actividad.delete_record()
        # Reprobamos el plan de trabajo para que deba ser revisado por todos los actores de nuevo
        reprobar()
        redirect(URL(c='Pasantia',f='verPlanDeTrabajo',vars=dict(planId=request.vars.planId)))
    # Definimos la vista que vamos a renderizar
    response.view = 'Pasantia/eliminarActividad.html'
    return locals()

@auth.requires_login()
def AprobarPlanTrabajo():
    form = FORM.confirm('¿Esta Seguro Aprobar Este Plan De Trabajo?',
                        {'Back': URL(c='Pasantia',f='verPlanDeTrabajo', vars=dict(planId=request.vars.planId))})
    if form.accepted:
        fase = db.Fase(id=request.vars.faseId)
        fase.delete_record()
        reprobar()
        redirect(URL(c='Pasantia',f='verPlanDeTrabajo', vars=dict(planId=request.vars.planId)))
    return locals()

@auth.requires_login()
def reprobar():
    plan_trabajo = db.Plan_Trabajo(id=request.vars.planId)
    # Verificamos si hay que revertir aprobaciones para evitar ir a la base de datos innecesariamente
    if ((plan_trabajo.aprobacion_tutor_academico!="En Espera"
        or plan_trabajo.aprobacion_tutor_industrial!="En Espera"
        or plan_trabajo.aprobacion_coordinacion!="En Espera")
        and plan_trabajo.estado!="Enviado"):
        # Cambiamos el estado
        plan_trabajo.update_record(
            aprobacion_tutor_academico="En Espera",
            aprobacion_tutor_industrial="En Espera",
            aprobacion_coordinacion="En Espera",
            estado="Sin Enviar")

# Funcion que retorna True si el plan fue enviado y aprobado,False de lo contrario
@auth.requires_login()
def comprobarPlanAprobado(planId):
    plan_trabajo = db.Plan_Trabajo(id=planId)
    # Verificamos si hay que revertir aprobaciones para evitar ir a la base de datos innecesariamente
    if (plan_trabajo.aprobacion_tutor_academico=="Aprobado"
        and plan_trabajo.aprobacion_tutor_industrial=="Aprobado"
        and plan_trabajo.aprobacion_coordinacion=="Aprobado"
        and plan_trabajo.estado=="Enviado"):
        return True
    else:
        return False