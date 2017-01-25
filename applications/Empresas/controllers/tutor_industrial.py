# -*- coding: utf-8 -*-

# Proceso de registro en el cual un tutor solicita un registro a una Empresa
from shlex import shlex

def tutorNoComfirmado():
    message = T(
        'Usted Aun No Ha Sido Comfirmado Como Tutor Industrial Por Su Empresa, Por Lo Que Aun No Puede ' \
        'Iniciar Sesion')
    response.view = 'Tutor_Industrial/tutorNoComfirmado.html'
    return locals()

def solicitar_registro_tutor():
    # Agregamos los campos en el orden deseado, comenzamos con el login y el password
    fields =[
        db.auth_user.email,
        db.auth_user.first_name,
        db.Tutor_Industrial.last_name,
        db.Tutor_Industrial.tipo_documento,
        db.Tutor_Industrial.numero_documento,
        db.auth_user.password
    ]
    # Agregamos un campo extra de comfirm password el cual debera tener el mismo valor que el password para ser aceptado
    fields += [Field('comfirm_Password','password', label=T('Comfirm Password'),
                     requires = [IS_EXPR('value==%s' % repr(request.vars.password),error_message=T('Las contraseñas no coinciden'))])]
    # Agregamos el resto de los campos
    fields +=[
        db.Tutor_Industrial.Empresa,
        db.auth_user.pregunta_secreta,
        db.auth_user.respuesta_secreta,
        db.Tutor_Industrial.profesion,
        db.Tutor_Industrial.cargo,
        db.Tutor_Industrial.departamento,
        db.auth_user.pais,
        db.auth_user.estado,
        db.Tutor_Industrial.universidad,
        db.auth_user.direccion,
        db.auth_user.telefono
    ]
    # Generamos el SQLFORM utilizando los campos
    form = SQLFORM.factory(
    captcha_field(),
    *fields,
    submit_button='Submit',
    separator=': ',
    buttons=['submit'],
    col3 = {
        'email':T('Identificación de acceso unica asignada a la Empresa'),
        'first_name':T('Nombre comercial de la Empresa'),
        'last_name':T('Nombre comercial de la Empresa'),
        'tipo_documento': T('Tipo De Documento'),
        'numero_documento':T('Numero De Documento'),
        'password':T('Contraseña para acceder al sistema'),
        'comfirm_Password':T('Repita su contraseña'),
        'pregunta_secreta':T('Si necesita obtener de nuevo su contraseña se le hara esta pregunta'),
        'respuesta_secreta':T('Respuesta a su pregunta secreta'),
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

        result = db.auth_user.insert(
            username=request.vars.email,
            first_name=request.vars.first_name,
            last_name=request.vars.last_name,
            password=db.auth_user.password.validate(request.vars.password)[0],
            email=request.vars.email,
            pregunta_secreta=request.vars.pregunta_secreta,
            respuesta_secreta=request.vars.respuesta_secreta,
            pais=request.vars.pais,
            estado=request.vars.estado,
            telefono=request.vars.telefono,
            direccion=request.vars.direccion,
            miembro_usb=False,
        )

        usuarioExternoSet = db(db.auth_user.email == request.vars.email).select()
        usuarioExterno = usuarioExternoSet[0]


        # Registramos al tutor
        db.Tutor_Industrial.insert(
            usuario=usuarioExterno.id,
            last_name=request.vars.last_name,
            tipo_documento=request.vars.tipo_documento,
            numero_documento=request.vars.numero_documento,
            Empresa=request.vars.Empresa,
            profesion=request.vars.profesion,
            cargo=request.vars.cargo,
            departamento=request.vars.departamento,
            universidad=request.vars.universidad,
            comfirmado_Por_Empresa=0
        )



        group_id = auth.id_group(role='Tutor_Industrial')
        auth.add_membership(group_id, result)

        generar_Correo_Verificacion(request.vars.email)

        EmpresaSet = db(db.auth_user.id == request.vars.Empresa).select()
        Empresa = EmpresaSet[0].first_name

        paisSet = db(db.Pais.id == request.vars.pais).select()
        pais = paisSet[0].first_name

        estadoSet = db(db.Estado.id == request.vars.estado).select()
        estado = estadoSet[0].first_name

        universidadSet = db(db.Universidad.id == request.vars.universidad).select()
        universidad = universidadSet[0].first_name

        # Mensaje de exito
        response.flash = T("Registro Exitoso")
        # Nos dirigimos a la pagina de exito
        return response.render('Tutor_Industrial/registrarTutorIndustrial/registro_Tutor_Industrial_exitoso.html',message=T("Registrarse como Tutor Industrial"),
                               result=T("El registro de su tutor ha sido exitoso!"),
                               email = request.vars.email,
                               first_name = request.vars.first_name,
                               last_name = request.vars.last_name,
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

@auth.requires(auth.is_logged_in() and auth.has_membership(role='Tutor Industrial'))
def verPerfil():
    # Buscamos la informacion general del usuario
    auth_user = db.auth_user(id=auth.user_id)
    # Buscamos la informacion de tutor
    tutor = db.Tutor_Industrial(usuario=auth_user)
    # Llenamos el valor de los campos
    db.auth_user.email.default = auth_user.email
    db.auth_user.pregunta_secreta.default = auth_user.pregunta_secreta
    db.auth_user.respuesta_secreta.default = auth_user.respuesta_secreta
    db.auth_user.first_name.default = auth_user.first_name
    db.auth_user.pais.default = auth_user.pais
    db.auth_user.estado.default = auth_user.estado
    # Llenamos el valor de los campos
    db.Tutor_Industrial.last_name.default = tutor.last_name
    db.Tutor_Industrial.Empresa.default = tutor.Empresa
    db.Tutor_Industrial.profesion.default = tutor.profesion
    db.Tutor_Industrial.tipo_documento.default = tutor.tipo_documento
    db.Tutor_Industrial.numero_documento.default = tutor.numero_documento
    db.Tutor_Industrial.cargo.default = tutor.cargo
    db.Tutor_Industrial.departamento.default = tutor.departamento
    db.Tutor_Industrial.universidad.default = tutor.universidad
    db.auth_user.direccion.default = auth_user.direccion
    db.auth_user.telefono.default = auth_user.telefono
    # Seleccionamos los campos a mostrar
    fields = [
        'email',
        'first_name',
        'last_name',
        'tipo_documento',
        'numero_documento',
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
    # Construimos el formulario
    form = SQLFORM.factory(db.auth_user, db.Tutor_Industrial, fields=fields, submit_button='Actualizar', showid=False,readonly=True)
    # Elegimos la vista a renderizar
    response.view = 'Tutor_Industrial/verPerfil.html'
    return locals()

@auth.requires(auth.is_logged_in() and auth.has_membership(role='Tutor Industrial'))
def editarPerfil():
    message = T("Editar Perfil")

    # Buscamos la informacion general del usuario
    auth_user = db.auth_user(id=auth.user_id)
    # Buscamos la informacion de tutor
    tutor = db.Tutor_Industrial(usuario=auth_user)
    db.auth_user.email.default = auth_user.email
    db.auth_user.pregunta_secreta.default = auth_user.pregunta_secreta
    db.auth_user.respuesta_secreta.default = auth_user.respuesta_secreta
    db.auth_user.first_name.default = auth_user.first_name
    db.auth_user.pais.default = auth_user.pais
    db.auth_user.estado.default = auth_user.estado

    db.auth_user.last_name.default = auth_user.last_name
    db.Tutor_Industrial.Empresa.default = tutor.Empresa
    db.Tutor_Industrial.profesion.default = tutor.profesion
    db.auth_user.tipo_documento.default = auth_user.tipo_documento
    db.auth_user.numero_documento.default = auth_user.numero_documento
    db.Tutor_Industrial.cargo.default = tutor.cargo
    db.Tutor_Industrial.departamento.default = tutor.departamento
    db.Tutor_Industrial.universidad.default = tutor.universidad
    db.auth_user.direccion.default = auth_user.direccion
    db.auth_user.telefono.default = auth_user.telefono

    db.auth_user.email.writable=False
    db.Tutor_Industrial.Empresa.writable = False

    fields = [
        'email',
        'first_name',
        'last_name',
        'tipo_documento',
        'numero_documento',
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
    form = SQLFORM.factory(db.auth_user, db.Tutor_Industrial, fields=fields, submit_button='Actualizar', showid=False)

    if form.accepts(request.vars):
        auth_user = db.auth_user(id=auth.user.id).update_record(**db.auth_user._filter_fields(form.vars))
        id = tutor.update_record(**db.Tutor_Industrial._filter_fields(form.vars))
        # Nos dirigimos a la pagina de exito
        redirect(URL(c='tutor_industrial', f='verPerfil'))

    response.view = 'Tutor_Industrial/editarPerfil.html'
    return locals()

@auth.requires(auth.is_logged_in() and auth.has_membership(role='Tutor Industrial'))
def consultarPasantias():
    email = auth.user.email

    tutor_industrial = db.Tutor_Industrial(usuario=auth.user_id)

    pasantias = ((db.Pasantia.tutor_industrial == tutor_industrial))
    #Define the fields to show on grid. Note: (you need to specify id field in fields section in 1.99.2
    # this is not required in later versions)
    fields = (db.Pasantia.titulo, db.Pasantia.estudiante,db.Pasantia.etapa, db.Pasantia.status)

    #Define headers as tuples/dictionaries
    headers = {
            'Pasantia.titulo': 'Titulo',
            'Pasantia.estudiante':'Estudiante',
            'Pasantia.etapa':'Etapa',
            'Pasantia.status': 'Status' }

    #Let's specify a default sort order on date_of_birth column in grid
    default_sort_order=[db.Pasantia.titulo]
    links = [lambda row: A('Detalle', _href=URL(a='Empresas',c='Pasantia',f='verDetallePasantia',args=[row.id]))]

    #Creating the grid object
    form = SQLFORM.grid(query=pasantias, fields=fields, headers=headers, orderby=default_sort_order,
                create=False, deletable=False, editable=False, maxtextlength=64, paginate=25,details=False,
                links=links,csv=False,user_signature=False)

    response.view = 'Tutor_Industrial/Consultar_Pasantias.html'
    return locals()

