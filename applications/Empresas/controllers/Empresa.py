# -*- coding: utf-8 -*-

# Proceso de registro de Empresa por medio de la opcion Empresa -> Registrarse, en el Index
def registrar_Empresa():
    # Agregamos los campos en el orden deseado, comenzamos con el correoin y el password
    fields = [db.UsuarioExterno.correo,db.UsuarioExterno.clave]
    # Agregamos un campo extra de comfirm password el cual debera tener el mismo valor que el password para ser aceptado
    fields += [Field('comfirm_Password','password', label=T('Comfirm Password'),
                     requires = [IS_EXPR('value==%s' % repr(request.vars.clave),error_message=T('Las contraseñas no coinciden'))])]
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
    # Generamos el SQLFORM utilizando los campos
    form = SQLFORM.factory(
    captcha_field(),
    *fields,
    submit_button='Submit',
    separator=': ',
    buttons=['submit'],
    col3 = {'correo':T('Identificación de acceso unica asignada a la Empresa'),
            'clave':T('Contraseña para acceder al sistema'),
            'comfirm_Password':T('Repita su contraseña'),
            'pregunta_secreta':T('Si necesita obtener de nuevo su contraseña se le hara esta pregunta'),
            'respuesta_secreta':T('Respuesta a su pregunta secreta'),
            'nombre':T('Nombre comercial de la Empresa'),
            'pais':T('Pais en el que se encuentra la Empresa'),
            'estado':T('Estado del pais en el que se encuentra'),
            'area_laboral':T('Area Laboral de la Empresa'),
            'direccion':T('Direccion de las instalaciones de la Empresa'),
            'direccion_web':T('Pagina Web de la Empresa'),
            'descripcion':T('Descripcion breve de la Empresa, su vision y sus funciones'),
            'telefono':T('Numero telefonico de contacto de la Empresa'),
            'contacto_RRHH':T('Correo de contacto del departamento de recursos humanos de la Empresa')}
    )

    # Caso 1: El form se lleno de manera correcta asi que registramos la Empresa y procedemos a la pagina de exito
    if form.process().accepted:

        # Insertamos en la tabla User de Web2py, para el correoin
        result = db.auth_user.insert(
            first_name=request.vars.nombre,
            password=db.auth_user.password.validate(request.vars.clave)[0],
            email=request.vars.correo,
        )
        group_id = auth.id_group(role='Empresa')
        auth.add_membership(group_id, result)

        # Registramos el usuario externo
        db.UsuarioExterno.insert(
            auth_User=result,
            correo=request.vars.correo,
            clave=request.vars.clave,
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
            usuario = usuarioExterno.id,
            area_laboral = request.vars.area_laboral,
            direccion_web = request.vars.direccion_web,
            descripcion = request.vars.descripcion,
            contacto_RRHH = request.vars.contacto_RRHH
        )



        generar_Correo_Verificacion(request.vars.correo)

        paisSet = db(db.Pais.id == request.vars.pais).select()
        pais = paisSet[0].nombre

        estadoSet = db(db.Estado.id == request.vars.estado).select()
        estado = estadoSet[0].nombre

        arealaboralSet = db(db.Area_Laboral.id == request.vars.area_laboral).select()
        area_laboral = arealaboralSet[0].nombre

        # Mensaje de exito
        response.flash = T("Registro Exitoso")
        # Nos dirigimos a la pagina de exito
        return response.render('Empresa/registrarEmpresa/registro_Empresa_exitoso.html',message=T("Registrar Empresa"),
                               result=T("El registro de su Empresa ha sido exitoso!"),
                               correo=request.vars.correo,
                               nombre=request.vars.nombre,
                               direccion=request.vars.direccion,
                               pais = pais,
                               estado = estado,
                               area_laboral = area_laboral,
                               direccion_web=request.vars.direccion_web,
                               descripcion=request.vars.descripcion,
                               telefono=request.vars.telefono,
                               contacto_RRHH=request.vars.contacto_RRHH,
                               pregunta_secreta=request.vars.pregunta_secreta,
                               respuesta_secreta=request.vars.respuesta_secreta)
    # Caso 2: El form no se lleno de manera correcta asi que recargamos la pagina
    else:
        return response.render('Empresa/registrarEmpresa/registrar_Empresa.html',message=T("Registrar Empresa"),form=form)

def registrar_Tutor_Industrial():
    # Agregamos los campos en el orden deseado, comenzamos con el login y el password
    fields = [
        db.UsuarioExterno.correo,
        db.UsuarioExterno.nombre,
        db.Tutor_Industrial.apellido,
        db.Tutor_Industrial.tipo_documento,
        db.Tutor_Industrial.numero_documento,
        db.UsuarioExterno.clave
    ]
    # Agregamos un campo extra de comfirm password el cual debera tener el mismo valor que el password para ser aceptado
    fields += [Field('comfirm_Password', 'password', label=T('Comfirm Password'),
                     requires=[IS_EXPR('value==%s' % repr(request.vars.clave),
                                       error_message=T('Las contraseñas no coinciden'))])]
    # Agregamos el resto de los campos
    fields += [
        db.UsuarioExterno.pregunta_secreta,
        db.UsuarioExterno.respuesta_secreta,
        db.Tutor_Industrial.profesion,
        db.Tutor_Industrial.cargo,
        db.Tutor_Industrial.departamento,
        db.UsuarioExterno.pais,
        db.UsuarioExterno.estado,
        db.Tutor_Industrial.universidad,
        db.UsuarioExterno.direccion,
        db.UsuarioExterno.telefono
    ]
    # Generamos el SQLFORM utilizando los campos
    form = SQLFORM.factory(
        captcha_field(),
        *fields,
        submit_button='Submit',
        separator=': ',
        buttons=['submit'],
        col3={
            'correo': T('Identificación de acceso unica asignada a la Empresa'),
            'nombre': T('Nombre comercial de la Empresa'),
            'apellido': T('Nombre comercial de la Empresa'),
            'tipo_documento': T('Tipo De Documento'),
            'numero_documento': T('Numero De Documento'),
            'clave': T('Contraseña para acceder al sistema'),
            'comfirm_Password': T('Repita su contraseña'),
            'pregunta_secreta': T('Si necesita obtener de nuevo su contraseña se le hara esta pregunta'),
            'respuesta_secreta': T('Respuesta a su pregunta secreta'),
            'profesion': T('Profesion del tutor industrial'),
            'cargo': T('Cargo que ocupa en la Empresa'),
            'departamento': T('Departamento de la Empresa en la que trabaja'),
            'direccion': T('Direccion del tutor industrial'),
            'pais': T('Pais en el que se encuentra domiciliado el tutor industrial'),
            'estado': T('Estado en el que se encuentra domiciliado el tutor industrial'),
            'universidad': T('Universidad de la cual egreso el tutor'),
            'telefono': T('Numerico telefonico del tutor industrial')
              })
    # Caso 1: El form se lleno de manera correcta asi que registramos al tutor y procedemos a la pagina de exito
    if form.process().accepted:

        # Registramos el usuario externo
        db.UsuarioExterno.insert(
            correo=request.vars.correo,
            clave=request.vars.clave,
            pregunta_secreta=request.vars.pregunta_secreta,
            respuesta_secreta=request.vars.respuesta_secreta,
            nombre=request.vars.nombre,
            pais=request.vars.pais,
            estado=request.vars.estado,
            telefono=request.vars.telefono,
            direccion=request.vars.direccion,
        )

        usuarioExternoSet = db(db.UsuarioExterno,db.UsuarioExterno.correo == request.vars.correo).select()
        usuarioExterno = usuarioExternoSet[0]

        empresa = \
            db(db.Empresa, db.Empresa.usuario == usuarioExterno.id).select()[0]

        # Registramos al tutor
        db.Tutor_Industrial.insert(
            usuario=usuarioExterno.id,
            apellido=request.vars.apellido,
            tipo_documento=request.vars.tipo_documento,
            numero_documento=request.vars.numero_documento,
            Empresa=empresa.id,
            profesion=request.vars.profesion,
            cargo=request.vars.cargo,
            departamento=request.vars.departamento,
            universidad=request.vars.universidad,
            comfirmado_Por_Empresa=1
        )

        # Insertamos en la tabla user de Web2py
        result = db.auth_user.insert(
            first_name=request.vars.nombre,
            last_name=request.vars.apellido,
            password=db.auth_user.password.validate(request.vars.clave)[0],
            email=request.vars.correo,
        )

        generar_Correo_Verificacion(request.vars.correo)

        paisSet = db(db.Pais.id == request.vars.pais).select()
        pais = paisSet[0].nombre

        estadoSet = db(db.Estado.id == request.vars.estado).select()
        estado = estadoSet[0].nombre

        universidadSet = db(db.Universidad.id == request.vars.universidad).select()
        universidad = universidadSet[0].nombre

        # Mensaje de exito
        response.flash = T("Registro Exitoso")
        # Nos dirigimos a la pagina de exito
        return response.render('Empresa/registrarTutorIndustrial/registro_Tutor_Industrial_exitoso.html',
                               message=T("Registrar Tutor Industrial"),
                               result=T("El registro de su tutor ha sido exitoso!"),
                               correo=request.vars.correo,
                               nombre=request.vars.nombre,
                               apellido=request.vars.apellido,
                               tipo_documento=request.vars.tipo_documento,
                               numero_documento=request.vars.numero_documento,
                               Empresa=usuarioExterno.nombre,
                               profesion=request.vars.profesion,
                               cargo=request.vars.cargo,
                               departamento=request.vars.departamento,
                               direccion=request.vars.direccion,
                               estado=estado,
                               pais=pais,
                               universidad=universidad,
                               telefono=request.vars.telefono)
    # Caso 2: El form no se lleno de manera correcta asi que recargamos la pagina
    else:
        return response.render('Empresa/registrarTutorIndustrial/registrar_Tutor_Industrial.html',
                               message=T("Registrar Tutor Industrial"), form=form)

# Proceso de registro de Empresa por medio de la opcion Empresa -> Registrarse, en el Index
def ver_Perfil_Empresa():
    usuarioExterno = db(db.UsuarioExterno.correo == auth.user.email).select()[0]
    empresa = db(db.Empresa.usuario == usuarioExterno.id).select()[0]
    # Agregamos los campos en el orden deseado, comenzamos con el correoin y el password
    fields = [
        db.UsuarioExterno.correo,
        db.UsuarioExterno.clave,
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
        db.Empresa.contacto_RRHH]

    db.UsuarioExterno.correo.default = usuarioExterno.correo
    db.UsuarioExterno.clave.default = usuarioExterno.clave
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

    db.UsuarioExterno.correo.writable = False
    db.UsuarioExterno.clave.writable = False
    db.UsuarioExterno.pregunta_secreta.writable = False
    db.UsuarioExterno.respuesta_secreta.writable = False
    db.UsuarioExterno.nombre.writable = False
    db.UsuarioExterno.pais.writable = False
    db.UsuarioExterno.estado.writable = False
    db.Empresa.area_laboral.writable = False
    db.UsuarioExterno.direccion.writable = False
    db.Empresa.direccion_web.writable = False
    db.Empresa.descripcion.writable = False
    db.UsuarioExterno.telefono.writable = False
    db.Empresa.contacto_RRHH.writable = False

    # Generamos el SQLFORM utilizando los campos
    form = SQLFORM.factory(
    *fields,
    separator=': ',
    col3 = {'correo':T('Identificación de acceso unica asignada a la Empresa'),
            'clave':T('Contraseña para acceder al sistema'),
            'comfirm_Password':T('Repita su contraseña'),
            'pregunta_secreta':T('Si necesita obtener de nuevo su contraseña se le hara esta pregunta'),
            'respuesta_secreta':T('Respuesta a su pregunta secreta'),
            'nombre':T('Nombre comercial de la Empresa'),
            'pais':T('Pais en el que se encuentra la Empresa'),
            'estado':T('Estado del pais en el que se encuentra'),
            'area_laboral':T('Area Laboral de la Empresa'),
            'direccion':T('Direccion de las instalaciones de la Empresa'),
            'direccion_web':T('Pagina Web de la Empresa'),
            'descripcion':T('Descripcion breve de la Empresa, su vision y sus funciones'),
            'telefono':T('Numero telefonico de contacto de la Empresa'),
            'contacto_RRHH':T('Correo de contacto del departamento de recursos humanos de la Empresa')}
    )

    form.add_button(T('Editar'), URL('editar_Perfil_Empresa'))

    return response.render('Empresa/perfil_Empresa.html',message=T("Perfil Empresarial"),form=form)

# Proceso de registro de Empresa por medio de la opcion Empresa -> Registrarse, en el Index
def editar_Perfil_Empresa():
    usuarioExterno = db(db.UsuarioExterno.correo == auth.user.email).select()[0]
    empresa = db(db.Empresa.usuario == usuarioExterno.id).select()[0]
    # Agregamos los campos en el orden deseado, comenzamos con el correoin y el password
    # Agregamos los campos en el orden deseado, comenzamos con el correoin y el password
    fields = [db.UsuarioExterno.correo,db.UsuarioExterno.clave]
    # Agregamos un campo extra de comfirm password el cual debera tener el mismo valor que el password para ser aceptado
    fields += [Field('comfirm_Password','password',default= usuarioExterno.clave, label=T('Comfirm Password'),
                     requires = [IS_EXPR('value==%s' % repr(request.vars.clave),error_message=T('Las contraseñas no coinciden'))])]
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

    db.UsuarioExterno.correo.default = usuarioExterno.correo
    db.UsuarioExterno.clave.default = usuarioExterno.clave
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

    db.UsuarioExterno.correo.writable = False
    db.UsuarioExterno.clave.writable = True
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
    col3 = {'correo':T('Identificación de acceso unica asignada a la Empresa'),
            'clave':T('Contraseña para acceder al sistema'),
            'comfirm_Password':T('Repita su contraseña'),
            'pregunta_secreta':T('Si necesita obtener de nuevo su contraseña se le hara esta pregunta'),
            'respuesta_secreta':T('Respuesta a su pregunta secreta'),
            'nombre':T('Nombre comercial de la Empresa'),
            'pais':T('Pais en el que se encuentra la Empresa'),
            'estado':T('Estado del pais en el que se encuentra'),
            'area_laboral':T('Area Laboral de la Empresa'),
            'direccion':T('Direccion de las instalaciones de la Empresa'),
            'direccion_web':T('Pagina Web de la Empresa'),
            'descripcion':T('Descripcion breve de la Empresa, su vision y sus funciones'),
            'telefono':T('Numero telefonico de contacto de la Empresa'),
            'contacto_RRHH':T('Correo de contacto del departamento de recursos humanos de la Empresa')}
    )
    # Caso 1: El form se lleno de manera correcta asi que registramos al tutor y procedemos a la pagina de exito
    if form.process().accepted:

        # Registramos el usuario externo
        db(db.UsuarioExterno.id == usuarioExterno.id).update(
            clave=request.vars.clave,
            pregunta_secreta=request.vars.pregunta_secreta,
            respuesta_secreta=request.vars.respuesta_secreta,
            nombre=request.vars.nombre,
            pais=request.vars.pais,
            estado=request.vars.estado,
            telefono=request.vars.telefono,
            direccion=request.vars.direccion,
        )

        # Registramos la Empresa
        db(db.Empresa.id == empresa.id).update(
            usuario=usuarioExterno.id,
            area_laboral=request.vars.area_laboral,
            direccion_web=request.vars.direccion_web,
            descripcion=request.vars.descripcion,
            contacto_RRHH=request.vars.contacto_RRHH
        )

        db(db.auth_user.id == auth.user.id).update(
            first_name=request.vars.nombre,
            password = db.auth_user.password.validate(request.vars.clave)[0]
        )

        # Mensaje de exito
        response.flash = T("Edicion Exitosa")
        # Nos dirigimos a la pagina de exito
        redirect(URL(c='Empresa', f='ver_Perfil_Empresa'))


    else:
        return response.render('Empresa/editar_Registrar_Empresa.html', message=T("Editando Perfil Empresa"),
                               form=form)