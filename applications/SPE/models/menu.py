from Usuarios import Usuario
Usuario=Usuario()

response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description

response.menu = [
    (SPAN(' ', _class='fa fa-home fa-lg'), False, URL(a='Empresas', c='default', f='index'))
]

DEVELOPMENT_MENU = True

# Menu de autenticacion

if auth.is_logged_in():
    texto_principal = auth.user.first_name
else:
    texto_principal = "Bienvenido"

opciones = []

opciones_administrativo = [
    ((SPAN(_class='fa fa-user'), '  Ver Perfil'), False, '/SPE/mi_perfil/ver'),
    ((SPAN(_class='fa fa-cog'), '  Configuración '), False, '/SPE/mi_perfil/configuracion'),
    ((SPAN(_class='fa fa-sign-out'), '  Cerrar Sesión'), False, URL('default', 'logout'))
]

opciones_estudiante = [
    ((SPAN(_class='fa fa-user'), '  Ver Perfil'), False, '/SPE/mi_perfil/ver'),
    ((SPAN(_class='fa fa-list'), '  Mis Pasantias'), False, '/SPE/mis_pasantias/listar'),
    ((SPAN(_class='fa fa-cog'), '  Configuración '), False, '/SPE/mi_perfil/configuracion'),
    ((SPAN(_class='fa fa-sign-out'), '  Cerrar Sesión'), False, URL('default', 'logout'))
]

opciones_coordinadorCCT = [
    ((SPAN(_class='fa fa-user'), '  Ver Perfil'), False, '/SPE/mi_perfil/ver'),
    ((SPAN(_class='fa fa-cog'), '  Configuración'), False, '/SPE/mi_perfil/configuracion'),
    ((SPAN(_class='fa fa-sign-out'), '  Cerrar Sesión'), False, URL('default', 'logout'))
]

opciones_coordinador = [
    ((SPAN(_class='fa fa-user'), '  Ver Perfil'), False, '/SPE/mi_perfil/ver'),
    ((SPAN(_class='fa fa-list'), '  Mis Pasantias'), False, '/SPE/Coordinador/consultarPasantias'),
    ((SPAN(_class='fa fa-cog'), '  Configuración'), False, '/SPE/mi_perfil/configuracion'),
    ((SPAN(_class='fa fa-sign-out'), '  Cerrar Sesión'), False, URL('default', 'logout'))
]

opciones_profesor = [
    ((SPAN(_class='fa fa-user'), '  Ver Perfil'), False, '/SPE/mi_perfil/ver'),
    ((SPAN(_class='fa fa-list'), '  Mis Pasantias'), False, '/SPE/mis_pasantias_tutor/listar'),
    ((SPAN(_class='fa fa-cog'), '  Configuración'), False, '/SPE/mi_perfil/configuracion'),
    ((SPAN(_class='fa fa-sign-out'), '  Cerrar Sesión'), False, URL('default', 'logout'))
]

if auth.has_membership(role='CoordinadorCCT'):
    opciones = opciones_coordinadorCCT
    response.menu = [
        (T('Índice'), URL('default', 'index') == URL(), URL('default', 'index'), []),
        (T('Administracion'), False, "#",[
            ((SPAN(_class='fa fa-cog'), '  Catalogos'), False, '/SPE/materias/listar'),
            ((SPAN(_class='fa fa-list'), '  Pasantias'), False, '/SPE/pasantias/listar'),
            ((SPAN(_class='fa fa-user'), '  Usuarios'), False, '/SPE/usuarios/listar')
        ]),
        (T('Reportes Y Estadisticas'), False, "#", []),
    ]
elif auth.has_membership(role='Estudiante'):
    opciones = opciones_estudiante
    response.menu = [
        (T('Índice'), URL('default', 'index') == URL(), URL('default', 'index'), []),
    ]
elif auth.has_membership(role='Profesor'):
    opciones = opciones_profesor
    response.menu = [
        (T('Índice'), URL('default', 'index') == URL(), URL('default', 'index'), []),
    ]
elif auth.has_membership(role='Coordinador'):
    opciones = opciones_coordinador
    response.menu = [
        (T('Índice'), URL('default', 'index') == URL(), URL('default', 'index'), []),
    ]
elif not auth.is_logged_in():
    response.menu = [
        (T('Índice'), URL('default', 'index') == URL(), URL('default', 'index'), []),
    ]
# Si no es alguno de los roles estandares entonces es un administrativo con rol personalizado o un usuario externo a la aplicacion
else:
    response.menu = [
        (T('Índice'), URL('default', 'index') == URL(), URL('default', 'index'), []),
    ]
    roles=auth.user_groups
    opciones = opciones_administrativo
    administrativeMenu=[]
    # Buscamos entre los roles del usuario si tiene acciones pertenecientes al contexto, si las tiene agregamos ese menu
    # de ese contexto
    for rol in roles:
        accion = Usuario.getUserActions('catalogos')
        if accion:
            url=accion[0]
            administrativeMenu.append(((SPAN(_class='fa fa-cog'), '  Catalogos'), False, url))
    for rol in roles:
        accion = Usuario.getUserActions('pasantias')
        if accion:
            url = accion[0]
            administrativeMenu.append(((SPAN(_class='fa fa-list'), '  Pasantias'), False, url))
    for rol in roles:
        accion = Usuario.getUserActions('coordinacion')
        if accion:
            url = accion[0]
            administrativeMenu.append(((SPAN(_class='fa fa-cog'), '  Usuarios'), False, url))

    if len(administrativeMenu)>0:
        response.menu.append((T('Administracion'), False, "#",administrativeMenu))


menu_autenticado = [
    (texto_principal, False, '#', opciones)
]
