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

opciones_estudiante = [
    ((SPAN(_class='fa fa-user'), '  Ver Perfil'), False, '/SPE/mi_perfil/ver'),
    ((SPAN(_class='fa fa-list'), '  Mis Pasantias'), False, '/SPE/mis_pasantias/listar'),
    ((SPAN(_class='fa fa-cog'), '  Configuración '), False, '/SPE/mi_perfil/configuracion'),
    ((SPAN(_class='fa fa-sign-out'), '  Cerrar Sesión'), False, URL('default', 'logout'))
]

opciones_coordinadorCCT = [
    ((SPAN(_class='fa fa-user'), '  Ver Perfil'), False, '/SPE/mi_perfil/ver'),
    ((SPAN(_class='fa fa-list'), '  Administracion'), False, '/SPE/pasantias/listar'),
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
            ('Catalogos', False, URL(c='tutor_industrial', f='solicitar_registro_tutor')),
            ('Pasantias', False, URL(c='tutor_industrial', f='solicitar_registro_tutor')),
            ('Usuarios', False, URL(c='tutor_industrial', f='solicitar_registro_tutor'))
        ]),
        (T('Reportes Y Estadisticas'), False, "#", []),
    ]
elif auth.has_membership(role='Estudiante'):
    opciones = opciones_estudiante
elif auth.has_membership(role='Profesor'):
    opciones = opciones_profesor
elif auth.has_membership(role='Coordinador'):
    opciones = opciones_coordinador
elif not auth.is_logged_in():
    response.menu = [
        (T('Índice'), URL('default', 'index') == URL(), URL('default', 'index'), []),
    ]
else:
    response.menu = [
        (T('Índice'), URL('default', 'index') == URL(), URL('default', 'index'), []),
    ]

menu_autenticado = [
    (texto_principal, False, '#', opciones)
]
