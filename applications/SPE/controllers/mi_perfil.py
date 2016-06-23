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

    elif (rol.nombre == 'Profesor'):
        profesor = db(((db.UsuarioUSB.id == userid) & (db.Profesor.usuario == db.UsuarioUSB.id) & (db.Profesor.departamento == db.Departamento.id) & (db.Profesor.categora == db.Categoria.id) & (db.Profesor.dedicacion == db.Dedicacion.id) & (db.Profesor.sede == db.Sede.id))).select().first()
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

@auth.requires(auth.has_membership(role='Estudiante'))
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