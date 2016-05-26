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

        #Insertamos en la tabla User de Web2py, para el correoin

        auth.get_or_create_user({
            "first_name":request.vars.nombre,
            "password":db.auth_user.password.validate(request.vars.password)[0],
            "email":request.vars.correo})

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
    db.Tutor_Industrial.email.requires += [IS_NOT_IN_DB(db, 'Empresa.correo',error_message=T('Correo No Disponible'))]
    # Agregamos los campos en el orden deseado, comenzamos con el correoin y el password
    fields =[
       db.Tutor_Industrial.email,
        db.Tutor_Industrial.nombre,
        db.Tutor_Industrial.apellido,
        db.Tutor_Industrial.ci,
        db.Tutor_Industrial.clave
    ]
    # Agregamos un campo extra de comfirm password el cual debera tener el mismo valor que el password para ser aceptado
    fields += [Field('comfirm_Password','password', label=T('Comfirm Password'),
                     requires = [IS_EXPR('value==%s' % repr(request.vars.password),error_message=T('Las contraseñas no coinciden'))])]
    # Agregamos el resto de los campos
    fields +=[
        db.Tutor_Industrial.pregunta_secreta,
        db.Tutor_Industrial.respuesta_secreta,
        db.Tutor_Industrial.profesion,
        db.Tutor_Industrial.cargo,
        db.Tutor_Industrial.departamento,
        db.Tutor_Industrial.direccion,
        db.Tutor_Industrial.pais,
        db.Tutor_Industrial.estado,
        db.Tutor_Industrial.universidad,
        db.Tutor_Industrial.telefono
    ]


    # Generamos el SQLFORM utilizando los campos
    form = SQLFORM.factory(
    captcha_field(),
    *fields,
    submit_button='Submit',
    separator=': ',
    buttons=['submit'],
    col3 = {'email':T('Identificación de acceso unica asignada a la Empresa'),
            'nombre':T('Nombre comercial de la Empresa'),
            'apellido':T('Nombre comercial de la Empresa'),
            'ci':T('Nombre comercial de la Empresa'),
            'password':T('Contraseña para acceder al sistema'),
            'comfirm_Password':T('Repita su contraseña'),
            'pregunta_secreta':T('Si necesita obtener de nuevo su contraseña se le hara esta pregunta'),
            'respuesta_secreta':T('Respuesta a su pregunta secreta'),
            'profesion':T('Profesion del tutor industrial'),
            'cargo':T('Cargo que ocupa en la Empresa'),
            'departamento':T('Departamento de la Empresa en la que trabaja'),
            'direccion':T('Direccion del tutor industrial'),
            'pais':T('Pais en el que se encuentra domiciliado el tutor industrial'),
            'estado':T('Estado en el que se encuentra domiciliado el tutor industrial'),
            'universidad':T('Universidad de la cual egreso el tutor'),
            'telefono':T('Numerico telefonico del tutor industrial')
           })
    # Caso 1: El form se lleno de manera correcta asi que registramos al tutor y procedemos a la pagina de exito
    if form.process().accepted:
        # Buscamos el id de la Empresa
        EmpresaRegistradoraSet = db(db.Empresa.correo == auth.user.username).select()
        EmpresaRegistradora = EmpresaRegistradoraSet[0]
        # Registramos la Empresa
        db.Tutor_Industrial.insert(
            email = request.vars.email,
            nombre = request.vars.nombre,
            apellido = request.vars.apellido,
            ci = request.vars.ci,
            password = request.vars.password,
            pregunta_secreta = request.vars.pregunta_secreta,
            respuesta_secreta = request.vars.respuesta_secreta,
            Empresa = EmpresaRegistradora.id,
            profesion = request.vars.profesion,
            cargo = request.vars.cargo,
            departamento = request.vars.departamento,
            direccion = request.vars.direccion,
            pais = request.vars.pais,
            estado = request.vars.estado,
            universidad = request.vars.universidad,
            telefono = request.vars.telefono)

        #Insertamos en la tabla user de Web2py
        result = db.auth_user.insert(
            first_name = request.vars.nombre,
            last_name  = request.vars.apellido,
            username   = request.vars.email,
            password   = db.auth_user.password.validate(request.vars.password)[0],
            email      = request.vars.email,
            user_Type  = 'Tutor_Industrial'
        )

        generar_Correo_Verificacion(request.vars.email)

        paisSet = db(db.pais.id == request.vars.pais).select()
        pais = paisSet[0].nombre

        estadoSet = db(db.estado.id == request.vars.estado).select()
        estado = estadoSet[0].nombre

        universidadSet = db(db.universidad.id == request.vars.universidad).select()
        universidad = universidadSet[0].nombre

        # Mensaje de exito
        response.flash = T("Registro Exitoso")
        # Nos dirigimos a la pagina de exito
        return response.render('Empresa/registrarTutorIndustrial/registro_Tutor_Industrial_exitoso.html',message=T("Registrar Tutor Industrial"),
                               result=T("El registro de su tutor ha sido exitoso!"),
                               email = request.vars.email,
                               nombre = request.vars.nombre,
                               apellido = request.vars.apellido,
                               ci = request.vars.ci,
                               Empresa = EmpresaRegistradora.nombre, # Cableado mientras se resuelven problemas
                               profesion = request.vars.profesion,
                               cargo = request.vars.cargo,
                               departamento = request.vars.departamento,
                               direccion = request.vars.direccion,
                               pais = pais,
                               estado = estado,
                               universidad = universidad,
                               telefono = request.vars.telefono)
    # Caso 2: El form no se lleno de manera correcta asi que recargamos la pagina
    else:
        return response.render('Empresa/registrarTutorIndustrial/registrar_Tutor_Industrial.html',message=T("Registrar Tutor Industrial"),form=form)

