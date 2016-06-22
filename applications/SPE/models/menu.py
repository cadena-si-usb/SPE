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

rol = {}

if ('currentUser' in session):
    currentUser = session.currentUser
    rol = db(db.Rol.id == currentUser.rol).select().first()
else:
    rol['nombre'] = 'Invitado'

opciones = []

opciones_estudiante = [
    ((SPAN(_class='fa fa-user'), '  Ver Perfil'), False, '/SPE/mi_perfil/ver'),
    ((SPAN(_class='fa fa-list'), '  Mis Pasantias'), False, '/SPE/mis_pasantias/listar'),
    ((SPAN(_class='fa fa-cog'), '  Configuración '), False, '/SPE/mi_perfil/configuracion'),
    ((SPAN(_class='fa fa-sign-out'), '  Cerrar Sesión'), False, URL('default', 'logout'))
]

opciones_coordinador = [
    ((SPAN(_class='fa fa-user'), '  Ver Perfil'), False, '/SPE/mi_perfil/ver'),
    ((SPAN(_class='fa fa-list'), '  Administracion'), False, '/SPE/pasantias/listar'),
    ((SPAN(_class='fa fa-cog'), '  Configuración'), False, '/SPE/mi_perfil/configuracion'),
    ((SPAN(_class='fa fa-sign-out'), '  Cerrar Sesión'), False, URL('default', 'logout'))
]

if rol['nombre'] == 'Coordinador_CCT':
    opciones = opciones_coordinador
else:
    opciones = opciones_estudiante

menu_autenticado = [
    (texto_principal, False, '#', opciones)
]

response.menu = [
    (T('Índice'), URL('default', 'index') == URL(), URL('default', 'index'), []),
]
