from Usuarios import Usuario

Usuario = Usuario()

@auth.requires_login()
def ver():
    userid = session.currentUser.id
    # Preguntar aqui por usuario externo o usuarioUSB
    currentUser = db.UsuarioUSB(db.UsuarioUSB.id == userid)
    rol = db(db.Rol.id == session.currentUser.rol).select().first()
    usuario = {
        "apellido": currentUser.apellido,
        "nombre": currentUser.nombre,
        "rol":  rol.nombre,  
    }

    if (rol.nombre == 'Estudiante'):
        estudiante = db(((db.UsuarioUSB.id == userid) & (db.Estudiante.usuario == db.UsuarioUSB.id) & (db.Estudiante.carrera == db.Carrera.id) & (db.UsuarioUSB.rol == db.Rol.id))).select().first()
        sede = db(db.Sede.id == db.Estudiante.sede).select().first()
        curriculo = db(db.Curriculo.estudiante == estudiante.Estudiante.id).select().first()
        response.view = 'mi_perfil/ver_estudiante.html'

    elif (rol.nombre == 'Profesor') or (rol.nombre == 'TutorAcademico'):
        profesor = db(((db.UsuarioUSB.id == userid) & (db.Profesor.usuario == db.UsuarioUSB.id) & (db.Profesor.departamento == db.Departamento.id) & (db.Profesor.categoria == db.Categoria.id) & (db.Profesor.dedicacion == db.Dedicacion.id) & (db.Profesor.sede == db.Sede.id))).select().first()
        sede = db(db.Sede.id == db.Profesor.sede).select().first()
        response.view = 'mi_perfil/ver_profesor.html'

    elif (rol.nombre == 'CoordinadorCCT'):
        coordinador = db(((db.UsuarioUSB.id == userid) & (db.Coordinador.usuario == db.UsuarioUSB.id))).select().first()
        coordinacion = db(db.Coordinador.coordinacion == db.Coordinacion.id).select().first()
        response.view = 'mi_perfil/ver_coordinador.html'

    return locals()


def ver_estudiante():
    return locals()

def ver_profesor():
    # Meterle rol al profesor de tutor academico para que se vea
    return locals()    

def ver_coordinador():
    return locals()

# def ver_administrativo():


@auth.requires_login()
def configuracion():
    global estudiante
    fields = [
        'nombre',
        'apellido',
        'correo',
        'tipo_documento',
        'numero_documento',
        'telefono',
        'direcUsuario',
        'sexo'         
    ]

    if auth.is_logged_in():
        userid = str(auth.user['username'])

        usuario = db.UsuarioUSB(db.UsuarioUSB.usbid == userid)

        db.UsuarioUSB.nombre.default=usuario.nombre
        db.UsuarioUSB.apellido.default = usuario.apellido
        db.UsuarioUSB.correo.default = usuario.correo
        db.UsuarioUSB.tipo_documento.default = usuario.tipo_documento
        db.UsuarioUSB.numero_documento.default = usuario.numero_documento
        db.UsuarioUSB.telefono.default = usuario.telefono
        db.UsuarioUSB.direcUsuario.default = usuario.direcUsuario
        db.UsuarioUSB.sexo.default = usuario.sexo

        rol = db.Rol(db.Rol.id == usuario['rol'])

        if (rol.nombre == 'Estudiante'):
            estudiante = db.Estudiante(db.Estudiante.usuario == usuario.id)
            fields.append('carnet')
            fields.append('carrera')
            fields.append('sede')
            db.Estudiante.carnet.default = estudiante.carnet
            db.Estudiante.carrera.default = estudiante.carrera
            db.Estudiante.sede.default = estudiante.sede
            form = SQLFORM.factory(db.UsuarioUSB,db.Estudiante,fields=fields,submit_button='Actualizar', showid=False)
        elif (rol.nombre == 'Profesor'):
            profesor = db.Profesor(db.Profesor.usuario == usuario.id)
            fields.append('categoria')
            fields.append('dedicacion')
            fields.append('departamento')
            fields.append('sede')
            db.Profesor.carnet.default = profesor.categoria
            db.Profesor.carrera.default = profesor.dedicacion
            db.Profesor.sede.default = profesor.departamento
            db.Profesor.sede.default = profesor.sede
            form = SQLFORM.factory(db.UsuarioUSB,db.Estudiante,fields=fields,submit_button='Actualizar', showid=False)
        else:
            form = SQLFORM(db.UsuarioUSB, record=usuario, fields=fields, submit_button='Actualizar', showid=False)

        if (rol.nombre.lower() != 'Invitado'):
            response.view = 'mi_perfil/configuracion_' + rol.nombre.lower() + '.html'
    else:
        redirect(URL(c="default",f="index"))

    if form.process().accepted:
        # Actualizo los datos de usuario
        usuario.update_record(**db.UsuarioUSB._filter_fields(form.vars))
        if (rol.nombre == 'Estudiante'):
            # Actualizo los datos exclusivos de estudiante
            estudiante.update_record(**db.Estudiante._filter_fields(form.vars))
        elif (rol.nombre == 'Profesor'):
            # Actualizo los datos exclusivos de profesor
            profesor.update_record(**db.Profesor._filter_fields(form.vars))

        session.flash = T('Perfil actualizado exitosamente!')
        usuario.update_record(activo=True)
        session.currentUser = Usuario.getByRole(usuario['usbid'])
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

    userid = str(auth.user['username'])

    estudiante = db.Estudiante(db.Estudiante.carnet == userid)

    curriculo = db.Curriculo(db.Curriculo.estudiante == estudiante['id'])

    form = SQLFORM(db.Curriculo,record=curriculo,fields=fields,submit_button='Actualizar',showid=False)

    if form.process().accepted:
        session.flash = T('Perfil actualizado exitosamente!')
        curriculo.update_record(activo=True)
        redirect(URL(c="default",f="index"))        
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()