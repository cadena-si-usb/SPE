# -*- coding: utf-8 -*-
from Empresas import Empresa

import Encoder

Empresa = Empresa()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows)

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar():
    fields = [db.UsuarioExterno.correo, db.auth_user.password]
    fields += [
        db.UsuarioExterno.pregunta_secreta,
        db.UsuarioExterno.respuesta_secreta,
        db.UsuarioExterno.nombre,
        db.UsuarioExterno.pais,
        db.UsuarioExterno.estado,
        db.Empresa.area_laboral,
        db.UsuarioExterno.direccion,
        db.Empresa.direccion_web,
        db.Empresa.descripcion,
        db.UsuarioExterno.telefono,
        db.Empresa.contacto_RRHH
    ]

    form = SQLFORM.factory(
        *fields,
        submit_button='Crear',
        showid=False,
        separator=': ',
        buttons=['submit'],
        col3={'correo': T('Identificación de acceso unica asignada a la Empresa'),
              'password': T('Contraseña para acceder al sistema'),
              'comfirm_Password': T('Repita su contraseña'),
              'pregunta_secreta': T('Si necesita obtener de nuevo su contraseña se le hara esta pregunta'),
              'respuesta_secreta': T('Respuesta a su pregunta secreta'),
              'nombre': T('Nombre comercial de la Empresa'),
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
            first_name=request.vars.nombre,
            password=db.auth_user.password.validate(request.vars.password)[0],
            email=request.vars.correo,
        )
        group_id = auth.id_group(role='Empresa')
        auth.add_membership(group_id, result)

        # Registramos el usuario externo
        db.UsuarioExterno.insert(
            id=result,
            auth_User=result,
            correo=request.vars.correo,
            pregunta_secreta=request.vars.pregunta_secreta,
            respuesta_secreta=request.vars.respuesta_secreta,
            nombre=request.vars.nombre,
            pais=request.vars.pais,
            estado=request.vars.estado,
            telefono=request.vars.telefono,
            direccion=request.vars.direccion,
        )

        usuarioExternoSet = db(db.UsuarioExterno.correo == request.vars.correo).select()
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
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def count():
    obj = Encoder.to_dict(request.vars)
    count = Empresa.count(obj)

    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = db((db.Empresa.usuario == db.UsuarioExterno.id) & (db.auth_user.id == db.UsuarioExterno.auth_User) &
              (db.Empresa.area_laboral == db.Area_Laboral.id) & (db.UsuarioExterno.pais == db.Pais.id)).select()

    return rows.as_json()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar():
    empresa = db(db.Empresa.id == request.args[0]).select()[0]
    usuarioExterno = db(db.UsuarioExterno.id == empresa.usuario).select()[0]
    # Agregamos los campos en el orden deseado, comenzamos con el correoin y el password
    # Agregamos los campos en el orden deseado, comenzamos con el correoin y el password
    fields = [db.UsuarioExterno.correo]
    # Agregamos el resto de los campos
    fields += [
        db.UsuarioExterno.pregunta_secreta,
        db.UsuarioExterno.respuesta_secreta,
        db.UsuarioExterno.nombre,
        db.UsuarioExterno.pais,
        db.UsuarioExterno.estado,
        db.Empresa.area_laboral,
        db.UsuarioExterno.direccion,
        db.Empresa.direccion_web,
        db.Empresa.descripcion,
        db.UsuarioExterno.telefono,
        db.Empresa.contacto_RRHH
    ]

    db.UsuarioExterno.correo.requires=[]
    db.UsuarioExterno.correo.default = usuarioExterno.correo
    db.UsuarioExterno.pregunta_secreta.default = usuarioExterno.pregunta_secreta
    db.UsuarioExterno.respuesta_secreta.default = usuarioExterno.respuesta_secreta
    db.UsuarioExterno.nombre.default = usuarioExterno.nombre
    db.UsuarioExterno.pais.default = usuarioExterno.pais
    db.UsuarioExterno.estado.default = usuarioExterno.estado
    db.Empresa.area_laboral.default = empresa.area_laboral
    db.UsuarioExterno.direccion.default = usuarioExterno.direccion
    db.Empresa.direccion_web.default = empresa.direccion_web
    db.Empresa.descripcion.default = empresa.descripcion
    db.UsuarioExterno.telefono.default = usuarioExterno.telefono
    db.Empresa.contacto_RRHH.default = empresa.contacto_RRHH

    db.UsuarioExterno.pregunta_secreta.writable = True
    db.UsuarioExterno.respuesta_secreta.writable = True
    db.UsuarioExterno.nombre.writable = True
    db.UsuarioExterno.pais.writable = True
    db.UsuarioExterno.estado.writable = True
    db.Empresa.area_laboral.writable = True
    db.UsuarioExterno.direccion.writable = True
    db.Empresa.direccion_web.writable = True
    db.Empresa.descripcion.writable = True
    db.UsuarioExterno.telefono.writable = True
    db.Empresa.contacto_RRHH.writable = True

    # Generamos el SQLFORM utilizando los campos
    form = SQLFORM.factory(
        *fields,
        submit_button='Submit',
        separator=': ',
        buttons=['submit'],
        col3={'correo': T('Identificación de acceso unica asignada a la Empresa'),
              'comfirm_Password': T('Repita su contraseña'),
              'pregunta_secreta': T('Si necesita obtener de nuevo su contraseña se le hara esta pregunta'),
              'respuesta_secreta': T('Respuesta a su pregunta secreta'),
              'nombre': T('Nombre comercial de la Empresa'),
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

        # Registramos el usuario externo
        usuarioExterno.update_record(
            pregunta_secreta=request.vars.pregunta_secreta,
            respuesta_secreta=request.vars.respuesta_secreta,
            nombre=request.vars.nombre,
            pais=request.vars.pais,
            estado=request.vars.estado,
            telefono=request.vars.telefono,
            direccion=request.vars.direccion,
        )

        # Registramos la Empresa
        empresa.update_record(
            usuario=usuarioExterno.id,
            correo=request.vars.correo,
            area_laboral=request.vars.area_laboral,
            direccion_web=request.vars.direccion_web,
            descripcion=request.vars.descripcion,
            contacto_RRHH=request.vars.contacto_RRHH
        )

        db(db.auth_user.id == auth.user.id).update(
            email=request.vars.correo,
            first_name=request.vars.nombre,
            password=db.auth_user.password.validate(request.vars.password)[0]
        )
        session.flash = T('Perfil actualizado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()