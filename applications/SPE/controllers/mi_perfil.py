from Usuarios import Usuario

Usuario = Usuario()

@auth.requires_login()
def ver():
    userid = session.currentUser.id
    usuario = auth.user
    # Preguntar aqui por usuario externo o usuarioUSB
    currentUser = usuario

    if (auth.has_membership(role='Estudiante')):
        estudiante = db.Estudiante(usuario=userid)
        carrera=db.Carrera(id=estudiante.carrera)
        sede_estudiante = db.Sede(id=estudiante.sede)
        curriculo = db.Curriculo(estudiante=estudiante.id)
    if (auth.has_membership(role='Profesor') or auth.has_membership(role='TutorAcademico')):
        profesor = db.Profesor(usuario=userid)
        departamento = db.Departamento(id=profesor.Profesor.departamento)
        categoria = db.Categoria(id=profesor.Profesor.categoria)
        dedicacion= db.Dedicacion(id=profesor.Profesor.dedicacion)
        sede_profesor = db.Sede(id= profesor.Profesor.sede)
    if (auth.has_membership(role='CoordinadorCCT') or auth.has_membership(role='Coordinador')):
        coordinador = db.Coordinador(usuario=userid)
        db.Coordinacion(id=coordinador.coordinacion)
        coordinacion = db(db.Coordinador.coordinacion == db.Coordinacion.id).select().first()
    # Si no es uno de los roles basicos entonces es un empleado administrativo (el cual puede pertenecer a roles personalizados)
    # o es un usuario con rol ajeno al sistema
    administrativo = db.Administrativo(usuario=usuario.id)
    if administrativo:
        coordinacion = db.Coordinacion(id=administrativo.coordinacion)
    return locals()

@auth.requires_login()
def configuracion():
    global estudiante
    fields = [
        'first_name',
        'last_name',
        'email',
        'tipo_documento',
        'numero_documento',
        'telefono',
        'direccion',
        'sexo'         
    ]

    if auth.is_logged_in():
        userid = str(auth.user['username'])
        usuario = auth.user

        db.auth_user.last_name.default = usuario.last_name
        db.auth_user.email.default = usuario.email
        db.auth_user.tipo_documento.default = usuario.tipo_documento
        db.auth_user.numero_documento.default = usuario.numero_documento
        db.auth_user.telefono.default = usuario.telefono
        db.auth_user.direccion.default = usuario.direccion
        db.auth_user.sexo.default = usuario.sexo

        if (auth.has_membership(role='Estudiante')):
            estudiante = db.Estudiante(db.Estudiante.usuario == usuario.id)
            fields.append('carnet')
            fields.append('carrera')
            fields.append('sede')
            db.Estudiante.carnet.default = estudiante.carnet
            db.Estudiante.carrera.default = estudiante.carrera
            db.Estudiante.sede.default = estudiante.sede
            form = SQLFORM.factory(db.auth_user,db.Estudiante,fields=fields,submit_button='Actualizar', showid=False)
            response.view = 'mi_perfil/configuracion_estudiante.html'
        elif (auth.has_membership(role='Profesor') or auth.has_membership(role='TutorAcademico')):
            profesor = db.Profesor(db.Profesor.usuario == usuario.id)
            fields.append('categoria')
            fields.append('dedicacion')
            fields.append('departamento')
            fields.append('sede')
            db.Profesor.categoria.default = profesor.categoria
            db.Profesor.dedicacion.default = profesor.dedicacion
            db.Profesor.departamento.default = profesor.departamento
            db.Profesor.sede.default = profesor.sede
            form = SQLFORM.factory(db.auth_user,db.Profesor,fields=fields,submit_button='Actualizar', showid=False)
            response.view = 'mi_perfil/configuracion__profesor.html'
        elif (auth.has_membership(role='CoordinadorCCT') or auth.has_membership(role='Coordinador')):
            coordinador = db.Coordinador(db.Coordinador.id == usuario.id)
            fields.append('carnet')
            fields.append('correo_Alternativo')
            db.Coordinador.carnet.default = coordinador.carnet
            db.Coordinador.correo_Alternativo.default = coordinador.correo_Alternativo
            form = SQLFORM.factory(db.auth_user,db.Coordinador,fields=fields,submit_button='Actualizar', showid=False)
            response.view = 'mi_perfil/configuracion_coordinador.html'
        # Si no es uno de los roles basicos entonces es un empleado administrativo (el cual puede pertenecer a roles personalizados)
        # o es un usuario con rol ajeno al sistema
        else:
            administrativo = db(((db.auth_user.id == auth.user.id) & (db.Administrativo.usuario == db.auth_user.id))).select()
            if administrativo:
                fields.append('carnet')
                fields.append('correo_Alternativo')
                fields.append('coordinacion')
                administrativo = administrativo.first()
                db.Administrativo.carnet.default = administrativo.Administrativo.carnet
                db.Administrativo.coordinacion.default = administrativo.Administrativo.coordinacion
                db.Administrativo.correo_Alternativo.default = administrativo.Administrativo.correo_Alternativo
                form = SQLFORM.factory(db.auth_user, db.Administrativo, fields=fields, submit_button='Actualizar',
                                       showid=False)
            else:
                form = SQLFORM(db.auth_user, record=usuario, fields=fields, submit_button='Actualizar', showid=False)
    else:
        redirect(URL(c="default",f="index"))

    if form.process().accepted:
        # Actualizo los datos de usuario
        usuario.update_record(**db.auth_user._filter_fields(form.vars))
        if (auth.has_membership(role='Estudiante')):
            # Actualizo los datos exclusivos de estudiante
            estudiante.update_record(**db.Estudiante._filter_fields(form.vars))
        elif (auth.has_membership(role='Profesor') or auth.has_membership(role='TutorAcademico')):
            # Actualizo los datos exclusivos de profesor
            profesor.update_record(**db.Profesor._filter_fields(form.vars))
        elif (auth.has_membership(role='CoordinadorCCT') or auth.has_membership(role='Coordinador')):
            # Actualizo los datos exclusivos de profesor
            coordinador.update_record(**db.Coordinador._filter_fields(form.vars))

        session.flash = T('Perfil actualizado exitosamente!')
        usuario.update_record(activo=True)
        session.currentUser = Usuario.getByRole(usuario.id)
        redirect(URL('ver'))
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()

@auth.requires(auth.has_membership(role='Estudiante'))
def editar_curriculo():
    fields = [
        'electivas',
        'cursos',
        'aficiones',
        'idiomas'         
    ]

    userid = str(auth.user['id'])

    estudiante = db.Estudiante(usuario = userid)

    curriculo = db.Curriculo(estudiante = estudiante['id'])

    form = SQLFORM(db.Curriculo,record=curriculo,fields=fields,submit_button='Actualizar',showid=False)

    if form.process().accepted:
        session.flash = T('Perfil actualizado exitosamente!')
        curriculo.update_record(activo=True)
        redirect(URL(c="default",f="index"))
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()
