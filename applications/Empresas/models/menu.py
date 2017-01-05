# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('web',SPAN(2),'py'),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Universidad Simón Bolívar'
response.meta.description = 'Sistema de Pasantías Empresariales'
response.meta.keywords = 'pasantías, USB, Empresa'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (SPAN(' ', _class='fa fa-home fa-lg'), False, URL(a= 'Empresas',c='default', f='index'))
]

DEVELOPMENT_MENU = True

# Menu de autenticacion

if auth.is_logged_in():
    texto_principal = auth.user.first_name
    if es_Empresa(auth.user.email):
        menu_autenticado = [
            (texto_principal, False, '#', [
                ("Su Perfil", False, URL('Empresa', 'ver_Perfil_Empresa')),
                (SPAN(' Cerrar Sesión', _class='fa fa-sign-out'), False, URL('default', 'logout'))
            ])
        ]
    elif es_Tutor_Industrial(auth.user.email):
        menu_autenticado = [
            (texto_principal,False, '#',[
                ("Su Perfil", False, URL('tutor_industrial','verPerfil')),
                (SPAN(' Cerrar Sesión', _class='fa fa-sign-out'), False, URL('default','logout'))
            ])
        ]
else:
    texto_principal = "Bienvenido"
    menu_autenticado = [
        (texto_principal, False, '#', [])
    ]

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources

    # Entradas del menu si el usuario esta autenticado
    if auth.is_logged_in():
        # Caso 1: El usuario es una Empresa
        if es_Empresa(auth.user.email):
            response.menu += [
                ('Pasantias',False,"#",[
                    ('Consultar Pasantias', False, URL('Empresa','consultarPasantias'))
                    ]),
                ('Tutores Industriales',False,"#",[
                    ('Sus tutores industriales', False, URL(c='Empresa', f='consultarTutores')),
                    ('Registrar tutor industrial', False, URL(c='Empresa', f='registrar_Tutor_Industrial')),
                    ]),
                ('Reportes', False, "#")
            ]
        # Caso 2: El usuario es un tutor industrial
        elif es_Tutor_Industrial(auth.user.email):
            response.menu += [
                ('Tutor Industrial',False,"#",[
                    ('¿Qué es un tutor industrial?',False,"#"),
                    ('Consultar Pasantias',False,URL('tutor_industrial','consultarPasantias')),
                    ('Justificar Retiro Pasante',False,URL('tutor_industrial','justificar_retiro_empresa'))
                    ])
            ]
    # Entradas del menu si el usuario NO esta autenticado
    else:

        response.menu += [
            ('Empresa',False,"#",[
                ('¿Qué puede obtener tu Empresa?',False,"#"),
                ('Registrarse',False,URL(c='Empresa', f='registrar_Empresa'))])
        ]

        response.menu += [
            ('Tutor Industrial',False,"#",[
                ('¿Qué es un tutor industrial?',False,"#"),
                ('Registrarse',False,URL(c='tutor_industrial', f='solicitar_registro_tutor'))
                ])
        ]

if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()
