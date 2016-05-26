# -*- coding: utf-8 -*-

# Proceso de registro en el cual un tutor solicita un registro a una Empresa
def solicitar_registro_tutor():
    # Agregamos los campos en el orden deseado, comenzamos con el login y el password
    fields =[
       db.Tutor_Industrial.correo,
        db.UsuarioExterno.nombre,
        db.Tutor_Industrial.apellido,
        db.Tutor_Industrial.tipo_documento,
        db.Tutor_Industrial.numero_documento,
        db.UsuarioExterno.clave
    ]
    # Agregamos un campo extra de comfirm password el cual debera tener el mismo valor que el password para ser aceptado
    fields += [Field('comfirm_Password','password', label=T('Comfirm Password'),
                     requires = [IS_EXPR('value==%s' % repr(request.vars.password),error_message=T('Las contraseñas no coinciden'))])]
    # Agregamos el resto de los campos
    fields +=[
        db.Tutor_Industrial.Empresa,
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
    col3 = {'email':T('Identificación de acceso unica asignada a la Empresa'),
            'nombre':T('Nombre comercial de la Empresa'),
            'apellido':T('Nombre comercial de la Empresa'),
            'tipo_documento': T('Tipo De Documento'),
            'numero_documento':T('Numero De Documento'),
            'password':T('Contraseña para acceder al sistema'),
            'comfirm_Password':T('Repita su contraseña'),
            'pregunta_secreta':T('Si necesita obtener de nuevo su contraseña se le hara esta pregunta'),
            'respuesta_pregunta_secreta':T('Respuesta a su pregunta secreta'),
            'Empresa':T('Empresa en la que trabaja'),
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

        # Registramos al tutor
        db.Tutor_Industrial.insert(
            usuario=usuarioExterno.id,
            apellido=request.vars.apellido,
            tipo_documento=request.vars.tipo_documento,
            numero_documento=request.vars.numero_documento,
            Empresa=request.vars.Empresa,
            profesion=request.vars.profesion,
            cargo=request.vars.cargo,
            departamento=request.vars.departamento,
            universidad=request.vars.universidad,
            comfirmado_Por_Empresa=0
        )

        #Insertamos en la tabla user de Web2py
        result = db.auth_user.insert(
            first_name = request.vars.nombre,
            last_name  = request.vars.apellido,
            password   = db.auth_user.password.validate(request.vars.clave)[0],
            email      = request.vars.correo,
        )

        generar_Correo_Verificacion(request.vars.correo)

        EmpresaSet = db(db.Empresa.id == request.vars.Empresa).select()
        Empresa = EmpresaSet[0].nombre

        paisSet = db(db.Pais.id == request.vars.pais).select()
        pais = paisSet[0].nombre

        estadoSet = db(db.Estado.id == request.vars.estado).select()
        estado = estadoSet[0].nombre

        universidadSet = db(db.Universidad.id == request.vars.universidad).select()
        universidad = universidadSet[0].nombre

        # Mensaje de exito
        response.flash = T("Registro Exitoso")
        # Nos dirigimos a la pagina de exito
        return response.render('Tutor_Industrial/registrarTutorIndustrial/registro_Tutor_Industrial_exitoso.html',message=T("Registrarse como Tutor Industrial"),
                               result=T("El registro de su tutor ha sido exitoso!"),
                               email = request.vars.correo,
                               nombre = request.vars.nombre,
                               apellido = request.vars.apellido,
                               tipo_documento=request.vars.tipo_documento,
                               numero_documento=request.vars.numero_documento,
                               Empresa = Empresa, # Cableado mientras se resuelven problemas
                               profesion = request.vars.profesion,
                               cargo = request.vars.cargo,
                               departamento = request.vars.departamento,
                               direccion = request.vars.direccion,
                               estado = estado, #Estara asi hasta que se implemente la tabla estado
                               pais = pais, #Estara asi hasta que se implemente la tabla estado
                               universidad = universidad,
                               telefono = request.vars.telefono)
    # Caso 2: El form no se lleno de manera correcta asi que recargamos la pagina
    else:
        return response.render('Tutor_Industrial/registrarTutorIndustrial/registrar_Tutor_Industrial.html',message=T("Registrarse como Tutor Industrial"),form=form)

# -*- coding: utf-8 -*-

def justificar_retiro_Empresa():
    # Argumentos son: codigo, año, periodo(nombre)
    pasantia=None
    if len(request.args)==4:
        pasantia = db((db.pasantia.codigo==request.args[0]) &
                (db.pasantia.anio==request.args[1]) &
                (db.pasantia.periodo==request.args[2]) &
                (db.pasantia.estudiante==request.args[3])
                ).select()[0]
        field =[db.pasantia.motivo_retiro_Tutor_Industrial]
        form = SQLFORM.factory(
            *field,submit_button='Subir Carta',
            separator=': ',
            buttons=['submit'],
            type='text',
            col3 = {'motivo':T('Motivo justificativo')}
            )
        if form.process().accepted:
            pasantia = db((db.pasantia.codigo==request.args[0]) &
                (db.pasantia.anio==request.args[1]) &
                (db.pasantia.periodo==request.args[2]) &
                (db.pasantia.estudiante==request.args[3])
                )
            pasantia.update(motivo_retiro_Tutor_Industrial = request.vars.motivo_retiro_Tutor_Industrial)
            response.flash = 'Actualizado el motivo'
            redirect(URL('justificacion_retiro_Empresa/'+request.args[0]+'/'+request.args[1]+'/'+request.args[2]+'/'+request.args[3]))

        elif form.errors:
            response.flash = 'Error'

    else:
        pasantias = db((db.pasantia.Tutor_Industrial==auth.user.username) &
            (db.pasantia.motivo_retiro_estudiante!=None)
        )

        opciones = []
        periodos = {}
        pasantias2 = {}
        for p in pasantias.select():
            periodo = db.periodo(p.periodo)
            periodos[periodo.nombre] = p.periodo
            datos_estudiante = db(db.usuario.usbid==p.estudiante).select()[0]
            opciones.append('['+p.codigo+'] '+periodo.nombre+' '+str(p.anio)+' '+p.titulo+' '+datos_estudiante.nombre+' '+datos_estudiante.apellido+' '+datos_estudiante.usbid)
            pasantias2[opciones[-1]] = p

        form = SQLFORM.factory(
            Field('pasantia', requires = IS_IN_SET(opciones)),submit_button='Buscar')
        if form.process().accepted:
            # Datos: codigo, periodo(nombre), año
            # datos = form.vars.pasantia.split()
            # datos[0] = datos[0][1:-1]
            pasantia = pasantias2[form.vars.pasantia]
            redirect(URL('justificar_retiro_Empresa/'+str(pasantia.codigo)+'/'+str(pasantia.anio)+'/'+str(pasantia.periodo)+'/'+str(pasantia.estudiante)))

        elif form.errors:
            response.flash = 'Error'

    return dict(form=form,pasantia=pasantia)

def justificacion_retiro_Empresa():
    pasantia = db((db.pasantia.codigo==request.args[0]) &
                (db.pasantia.anio==request.args[1]) &
                (db.pasantia.periodo==request.args[2]) &
                (db.pasantia.estudiante==request.args[3])
                ).select()[0]
    estudiante = db(db.usuario.usbid==request.args[3]).select()[0]
    return dict(pasantia=pasantia,estudiante=estudiante)