# -*- coding: utf-8 -*-
from Empresas import Empresa

import Encoder
from applications.SPE_lib.modules.grids import simple_spe_grid
Empresa = Empresa()
from applications.SPE_lib.modules.grids import simple_spe_grid
def sqlform_grid():
    fields = [db.Empresa.usuario,
              db.Empresa.area_laboral,
              db.Empresa.contacto_RRHH]
    if not request.args:
        return simple_spe_grid(db.Empresa,fields=fields)
    elif request.args[-2]=='new':
        return agregar(request)
    elif request.args[-3]=='edit':
        return modificar(request)
    elif request.args[-3]=='view':
        return ver(request)
    else:
        return simple_spe_grid(db.Empresa,fields=fields)

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows)

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar(request):
    fields = [db.auth_user.email, db.auth_user.password]
    fields += [
        db.auth_user.pregunta_secreta,
        db.auth_user.respuesta_secreta,
        db.auth_user.first_name,
        db.auth_user.pais,
        db.auth_user.estado,
        db.Empresa.area_laboral,
        db.auth_user.direccion,
        db.Empresa.direccion_web,
        db.Empresa.descripcion,
        db.auth_user.telefono,
        db.Empresa.contacto_RRHH
    ]

    form = SQLFORM.factory(
        *fields,
        submit_button='Crear',
        showid=False,
        separator=': ',
        buttons=['submit'],
        col3={'email': T('Identificación de acceso unica asignada a la Empresa'),
              'password': T('Contraseña para acceder al sistema'),
              'comfirm_Password': T('Repita su contraseña'),
              'pregunta_secreta': T('Si necesita obtener de nuevo su contraseña se le hara esta pregunta'),
              'respuesta_secreta': T('Respuesta a su pregunta secreta'),
              'first_name': T('Nombre comercial de la Empresa'),
              'pais': T('Pais en el que se encuentra la Empresa'),
              'estado': T('Estado del pais en el que se encuentra'),
              'area_laboral': T('Area Laboral de la Empresa'),
              'direccion': T('Direccion de las instalaciones de la Empresa'),
              'direccion_web': T('Pagina Web de la Empresa'),
              'descripcion': T('Descripcion breve de la Empresa, su vision y sus funciones'),
              'telefono': T('Numero telefonico de contacto de la Empresa'),
              'contacto_RRHH': T('Correo de contacto del departamento de recursos humanos de la Empresa')}
    )

    # Caso 1: El form se lleno de manera correcta asi que registramos la Empresa y procedemos a la pagina de exito
    if form.process().accepted:

        # Insertamos en la tabla User de Web2py, para el correoin
        result = db.auth_user.insert(
            username=request.vars.email,
            first_name=request.vars.first_name,
            password=db.auth_user.password.validate(request.vars.password)[0],
            email=request.vars.email,
            pregunta_secreta=request.vars.pregunta_secreta,
            respuesta_secreta=request.vars.respuesta_secreta,
            pais=request.vars.pais,
            estado=request.vars.estado,
            telefono=request.vars.telefono,
            direccion=request.vars.direccion,
        )
        group_id = auth.id_group(role='Empresa')
        auth.add_membership(group_id, result)

        usuarioExternoSet = db(db.auth_user.email == request.vars.email).select()
        usuarioExterno = usuarioExternoSet[0]

        # Registramos la Empresa
        db.Empresa.insert(
            id=result,
            usuario=usuarioExterno.id,
            area_laboral=request.vars.area_laboral,
            direccion_web=request.vars.direccion_web,
            descripcion=request.vars.descripcion,
            contacto_RRHH=request.vars.contacto_RRHH
        )
        # Actualizo los datos exclusivos de estudiante
        session.flash = T('Perfil actualizado exitosamente!')
        redirect(URL('sqlform_grid'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return form

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def count():
    obj = Encoder.to_dict(request.vars)
    count = Empresa.count(obj)

    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db((db.Empresa.usuario == db.auth_user.id) &
              (db.Empresa.area_laboral == db.Area_Laboral.id) & (db.auth_user.pais == db.Pais.id)).select()

    return rows.as_json()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar(request):
    # Buscamos la informacion de tutor
    empresa = db.Empresa(usuario=request.args[-1])
    # Buscamos la informacion general del usuario
    auth_user = db.auth_user(id=empresa.usuario)
    # Agregamos los campos en el orden deseado, comenzamos con el correoin y el password
    # Agregamos los campos en el orden deseado, comenzamos con el correoin y el password
    fields = [db.auth_user.email]
    # Agregamos el resto de los campos
    fields += [
        db.auth_user.pregunta_secreta,
        db.auth_user.respuesta_secreta,
        db.auth_user.first_name,
        db.auth_user.pais,
        db.auth_user.estado,
        db.Empresa.area_laboral,
        db.auth_user.direccion,
        db.Empresa.direccion_web,
        db.Empresa.descripcion,
        db.auth_user.telefono,
        db.Empresa.contacto_RRHH
    ]

    db.auth_user.email.requires=[]
    db.auth_user.email.default = auth_user.email
    db.auth_user.pregunta_secreta.default = auth_user.pregunta_secreta
    db.auth_user.respuesta_secreta.default = auth_user.respuesta_secreta
    db.auth_user.first_name.default = auth_user.first_name
    db.auth_user.pais.default = auth_user.pais
    db.auth_user.estado.default = auth_user.estado
    db.Empresa.area_laboral.default = empresa.area_laboral
    db.auth_user.direccion.default = auth_user.direccion
    db.Empresa.direccion_web.default = empresa.direccion_web
    db.Empresa.descripcion.default = empresa.descripcion
    db.auth_user.telefono.default = auth_user.telefono
    db.Empresa.contacto_RRHH.default = empresa.contacto_RRHH

    # Generamos el SQLFORM utilizando los campos
    form = SQLFORM.factory(
        *fields,
        submit_button='Submit',
        separator=': ',
        buttons=['submit'],
        col3={'email': T('Identificación de acceso unica asignada a la Empresa'),
              'comfirm_Password': T('Repita su contraseña'),
              'pregunta_secreta': T('Si necesita obtener de nuevo su contraseña se le hara esta pregunta'),
              'respuesta_secreta': T('Respuesta a su pregunta secreta'),
              'first_name': T('Nombre comercial de la Empresa'),
              'pais': T('Pais en el que se encuentra la Empresa'),
              'estado': T('Estado del pais en el que se encuentra'),
              'area_laboral': T('Area Laboral de la Empresa'),
              'direccion': T('Direccion de las instalaciones de la Empresa'),
              'direccion_web': T('Pagina Web de la Empresa'),
              'descripcion': T('Descripcion breve de la Empresa, su vision y sus funciones'),
              'telefono': T('Numero telefonico de contacto de la Empresa'),
              'contacto_RRHH': T('Correo de contacto del departamento de recursos humanos de la Empresa')}
    )
    # Caso 1: El form se lleno de manera correcta asi que registramos al tutor y procedemos a la pagina de exito
    if form.process().accepted:

        auth_user = db.auth_user(id=auth_user.id).update_record(**db.auth_user._filter_fields(form.vars))
        id = empresa.update_record(**db.Empresa._filter_fields(form.vars))
        redirect(URL('sqlform_grid'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return form

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def ver(request):
    # Buscamos la informacion de tutor
    empresa = db.Empresa(usuario=request.args[-1])
    # Buscamos la informacion general del usuario
    auth_user = db.auth_user(id=empresa.usuario)
    # Agregamos los campos en el orden deseado, comenzamos con el correoin y el password
    # Agregamos los campos en el orden deseado, comenzamos con el correoin y el password
    fields = ['email']
    # Agregamos el resto de los campos
    fields += [
        'pregunta_secreta',
        'respuesta_secreta',
        'first_name',
        'pais',
        'estado',
        'area_laboral',
        'direccion',
        'direccion_web',
        'descripcion',
        'telefono',
        'contacto_RRHH'
    ]

    for field in fields:
        if field in db.auth_user.fields:
            db.auth_user[field].default = auth_user[field]
        elif field in db.Empresa.fields:
            db.Empresa[field].default = empresa[field]

    # Generamos el SQLFORM utilizando los campos
    form = SQLFORM.factory(db.auth_user,db.Empresa,
                           fields=fields,
                           readonly=True,
                           submit_button='Submit',
                           separator=': ',
                           buttons=['submit']
                           )
    # Caso 1: El form se lleno de manera correcta asi que registramos al tutor y procedemos a la pagina de exito
    return form