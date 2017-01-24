from Usuarios import Usuario

Usuario = Usuario()


@auth.requires_login()
def ver():
    userid = session.currentUser.id
    usuario = db.auth_user(id=auth.user.id)
    # Preguntar aqui por usuario externo o usuarioUSB
    currentUser = usuario
    tipo_documento = db.Tipo_Documento(id=currentUser.tipo_documento)

    if (auth.has_membership(role='Estudiante')):
        estudiante = db.Estudiante(usuario=userid)
        carrera = db.Carrera(id=estudiante.carrera)
        sede_estudiante = db.Sede(id=estudiante.sede)
        curriculo = db.Curriculo(estudiante=estudiante.id)

    if (auth.has_membership(role='Profesor') or auth.has_membership(role='TutorAcademico')):
        profesor = db(((db.auth_user.id == userid) & (db.Profesor.usuario == db.auth_user.id))).select().first()
        departamento = db.Departamento(id=profesor.Profesor.departamento)
        categoria = db.Categoria(id=profesor.Profesor.categoria)
        dedicacion = db.Dedicacion(id=profesor.Profesor.dedicacion)
        sede = db.Sede(id=profesor.Profesor.sede)

    if (auth.has_membership(role='CoordinadorCCT') or auth.has_membership(role='Coordinador')):
        coordinador = db(((db.auth_user.id == userid) & (db.Coordinador.usuario == db.auth_user.id))).select().first()
        coordinacion = db(db.Coordinador.coordinacion == db.Coordinacion.id).select().first()
    # Si no es uno de los roles basicos entonces es un empleado administrativo (el cual puede pertenecer a roles
    # personalizados)
    # o es un usuario con rol ajeno al sistema
    administrativo = db(((db.auth_user.id == userid) & (db.Administrativo.usuario == db.auth_user.id))).select()
    if administrativo:
        administrativo = administrativo.first()
        coordinacion = db(db.Administrativo.coordinacion == db.Coordinacion.id).select().first()
    return locals()


@auth.requires_login()
def configuracion():
    global estudiante
    if auth.is_logged_in():
        userid = str(auth.user['username'])
        usuario = db.auth_user(id=auth.user.id)

        if (auth.has_membership(role='Estudiante') and request.args(0) == "estudiante"):
            record = db.Estudiante(db.Estudiante.usuario == usuario.id)
            fields = [
                'carnet',
                'carrera',
                'sede',
            ]
            form = SQLFORM(db.Estudiante, record=record, fields=fields, submit_button='Actualizar Estudiante',
                           showid=False)
            response.view = 'mi_perfil/configuracion_estudiante.html'

        elif (auth.has_membership(role='Profesor') and request.args(0) == "profesor"):
            record = db.Profesor(db.Profesor.usuario == usuario.id)
            fields = [
                'categoria',
                'dedicacion',
                'departamento',
                'sede',
            ]
            form = SQLFORM(db.Profesor, record=record, fields=fields, submit_button='Actualizar Profesor', showid=False)
            response.view = 'mi_perfil/configuracion__profesor.html'

        elif ((auth.has_membership(role='CoordinadorCCT') or auth.has_membership(role='Coordinador')) and request.args(
                0) == "coordinador"):
            record = db.Coordinador(db.Coordinador.id == usuario.id)
            fields = [
                'carnet',
                'correo_Alternativo',
                'coordinacion',
            ]
            form = SQLFORM(db.Coordinador, record=record, fields=fields, submit_button='Actualizar Coordinador',
                           showid=False)
            response.view = 'mi_perfil/configuracion_coordinador.html'
        # Si no es uno de los roles basicos entonces es un empleado administrativo (el cual puede pertenecer a roles
        # personalizados)
        # o es un usuario con rol ajeno al sistema
        elif request.args(0) == "administrativo":
            record = db.Administrativo(usuario=auth.user.id)
            fields = [
                'carnet',
                'correo_Alternativo',
                'coordinacion',
            ]
            form = SQLFORM(db.Administrativo,
                           record=record,
                           fields=fields,
                           submit_button='Actualizar Administrativo',
                           showid=False)
            response.view = 'mi_perfil/configuracion_administrativo.html'
        else:
            fields = [
                'first_name',
                'last_name',
                'email',
                'tipo_documento',
                'numero_documento',
                'telefono',
                'direccion',
                'sexo',
                'image'
            ]
            response.view = 'mi_perfil/configuracion.html'
            form = SQLFORM(db.auth_user,
                           record=usuario,
                           upload=URL('download'),
                           fields=fields,
                           submit_button='Actualizar',
                           showid=False)
    else:
        redirect(URL(c="default", f="index"))

    if form.process().accepted:
        if (auth.has_membership(role='Estudiante') and request.args(0) == "estudiante"):
            # Actualizo los datos exclusivos de estudiante
            record.update_record(**db.Estudiante._filter_fields(form.vars))
        elif (auth.has_membership(role='Profesor') and request.args(0) == "profesor"):
            # Actualizo los datos exclusivos de profesor
            record.update_record(**db.Profesor._filter_fields(form.vars))
        elif ((auth.has_membership(role='CoordinadorCCT') or auth.has_membership(role='Coordinador')) and
                      request.args(0) == "coordinador"):
            # Actualizo los datos exclusivos de profesor
            record.update_record(**db.Coordinador._filter_fields(form.vars))
        elif request.args(0) == "administrativo":
            administrativo = db.Administrativo(usuario=auth.user.id)
            record.update_record(**db.Administrativo._filter_fields(form.vars))
        else:
            usuario.update_record(**db.auth_user._filter_fields(form.vars))
            auth.user = usuario
        session.flash = T('Perfil actualizado exitosamente!')
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

    estudiante = db.Estudiante(usuario=userid)

    curriculo = db.Curriculo(estudiante=estudiante['id'])

    form = SQLFORM(db.Curriculo, record=curriculo, fields=fields, submit_button='Actualizar', showid=False)

    if form.process().accepted:
        session.flash = T('Perfil actualizado exitosamente!')
        curriculo.update_record(activo=True)
        redirect(URL(c="default", f="index"))
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()

def download():
    return response.download(request, db)