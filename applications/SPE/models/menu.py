response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description

response.menu = [
    (SPAN(' ', _class='fa fa-home fa-lg'), False, URL(a= 'Empresas',c='default', f='index'))
]

DEVELOPMENT_MENU = True

# Menu de autenticacion

if auth.is_logged_in():
    texto_principal = auth.user.first_name
else:
    texto_principal = "Bienvenido"

menu_autenticado = [
    (texto_principal,False, '#',[
        ("Su Perfil", False, '#'),
        (SPAN(' Cerrar Sesión', _class='fa fa-sign-out'), False, URL('default','logout'))
    ])
]

response.menu = [
(T('Índice'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Catálogo'),URL('catalogo','catalogue')==URL(),URL('catalogo','catalogue'),[]),
(T('Notificaciones'),URL('notificaciones','notifications')==URL(),URL('notificaciones','notifications'),[]),
(T('Perfil'),URL('usuarios','perfil')==URL(),URL('usuarios','perfil'),[])
]