from Usuarios import Usuario

Usuario = Usuario()

def ver():
    ident = session.currentUser.id

    estudiante = db(((db.UsuarioUSB.id == ident) & (db.Estudiante.usuario == db.UsuarioUSB.id) & (db.Estudiante.carrera == db.Carrera.id) & (db.UsuarioUSB.rol == db.Rol.id))).select().first()

    pasantias = db(db.Pasantia.estudiante == estudiante.Estudiante.id).select().first()
    curriculo = db(db.Curriculo.estudiante == estudiante.Estudiante.id).select().first()

    response.view = 'estudiantes/perfil.html'

    return dict(estudiante=estudiante,pasantias=pasantias,curriculo=curriculo)

def configuracion():
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

        rol = db.Rol(db.Rol.id == usuario['rol'])

        if (rol.nombre.lower() != 'Invitado'):
            response.view = 'mi_perfil/configuracion_' + rol.nombre.lower() + '.html'
    else:
        redirect(URL(c="default",f="index"))


    form = SQLFORM(db.UsuarioUSB,record=usuario,fields=fields,submit_button='Actualizar',showid=False)

    if form.process().accepted:
        session.flash = T('Perfil actualizado exitosamente!')
        usuario.update_record(activo=True)
        session.currentUser = Usuario.getByRole(usuario['usbid'])
        redirect(URL('ver'))
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()

def configuracion_estudiante():
    fields = [
        'carrera',
        'sede'         
    ]

    userid = str(auth.user['username'])

    estudiante = db.Estudiante(db.Estudiante.carnet == userid)

    form = SQLFORM(db.Estudiante,record=estudiante,fields=fields,submit_button='Actualizar',showid=False)

    if form.process().accepted:
        session.flash = T('Perfil actualizado exitosamente!')
        estudiante.update_record(activo=True)
        redirect(URL('perfil_estudiante'))
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()

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