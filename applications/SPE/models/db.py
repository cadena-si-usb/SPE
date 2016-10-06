# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

## app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig
from gluon import current

from applications.SPE_lib.modules.db_0_Area_Laboral import Area_Laboral
from applications.SPE_lib.modules.db_0_Area_Proyecto import Area_Proyecto
from applications.SPE_lib.modules.db_0_Categoria import Categoria
from applications.SPE_lib.modules.db_0_Dedicacion import Dedicacion
from applications.SPE_lib.modules.db_0_Division import Division
from applications.SPE_lib.modules.db_0_Etapa import Etapa
from applications.SPE_lib.modules.db_0_Periodo import Periodo
from applications.SPE_lib.modules.db_0_Sede import Sede
from applications.SPE_lib.modules.db_0_Tipo_Documento import Tipo_Documento
from applications.SPE_lib.modules.db_1_Acceso_Etapa import Acceso_Etapa
from applications.SPE_lib.modules.db_1_Accion_Usuario import Accion_Usuario
from applications.SPE_lib.modules.db_1_Coordinacion import Coordinacion
from applications.SPE_lib.modules.db_1_correo_Por_Verificar import correo_por_verificar
from applications.SPE_lib.modules.db_1_Departamento import Departamento
from applications.SPE_lib.modules.db_1_Materia import Materia
from applications.SPE_lib.modules.db_1_Pais import Pais
from applications.SPE_lib.modules.db_1_Universidad import Universidad
from applications.SPE_lib.modules.db_1_UsuarioUSB import UsuarioUSB
from applications.SPE_lib.modules.db_2_Administrativo import Administrativo
from applications.SPE_lib.modules.db_2_Carrera import Carrera
from applications.SPE_lib.modules.db_2_Coordinador import Coordinador
from applications.SPE_lib.modules.db_2_Estado import Estado
from applications.SPE_lib.modules.db_2_Profesor import Profesor
from applications.SPE_lib.modules.db_2_UsuarioExterno import UsuarioExterno
from applications.SPE_lib.modules.db_3_Empresa import Empresa
from applications.SPE_lib.modules.db_3_Estudiante import Estudiante
from applications.SPE_lib.modules.db_3_Tutor_Industrial import Tutor_Industrial

from applications.SPE_lib.modules.db_4_Curriculo import Curriculo
from applications.SPE_lib.modules.db_4_Pasantia import Pasantia
from applications.SPE_lib.modules.db_4_Permiso import Permiso
from applications.SPE_lib.modules.db_4_Retiro import Retiro

from applications.SPE_lib.modules.db_5_Colocacion import Colocacion
from applications.SPE_lib.modules.db_5_Ejecucion import Ejecucion
from applications.SPE_lib.modules.db_5_Inscripcion import Inscripcion
from applications.SPE_lib.modules.db_5_Plan_Trabajo import Plan_Trabajo
from applications.SPE_lib.modules.db_5_Preinscripcion import Preinscripcion

from applications.SPE_lib.modules.db_6_Fase import Fase

from applications.SPE_lib.modules.db_7_Actividad import Actividad
from applications.SPE_lib.modules.db_7_Materia_Periodo import Materia_Periodo

from applications.SPE_lib.modules.fixtures import load_fixtures

## once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)


if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL(myconf.take('db.uri'), 
      pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'],migrate=True)
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

current.db = db
## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## choose a style for forms
# or 'bootstrap3_stacked' or 'bootstrap2' or other
response.formstyle = myconf.take('forms.formstyle')  
response.form_label_separator = myconf.take('forms.separator')


## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Service, PluginManager,Mail

auth = Auth(db)
service = Service()
plugins = PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=True, signature=False)
## configure email
mail = Mail()
mail.settings.server = 'smtp.gmail.com:587'
mail.settings.sender = 'sistemapasantiaEmpresarialusb@gmail.com'
mail.settings.login = 'sistemapasantiaEmpresarialusb@gmail.com:speusb2016'
mail.settings.tls = True

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
auth.enable_record_versioning(db)

mail.settings.server = settings.email_server
mail.settings.sender = settings.email_sender
mail.settings.login = settings.email_login
# Cargamos Nuestros Modelos
Area_Laboral(db,T)
Area_Proyecto(db,T)
Categoria(db,T)
Dedicacion(db,T)
Division(db,T)
Etapa(db,T)
Periodo(db,T)
Sede(db,T)
Tipo_Documento(db,T)
Acceso_Etapa(db,T)
Accion_Usuario(db,T)
Coordinacion(db,T)
correo_por_verificar(db,T)
Departamento(db,T)
Materia(db,T)
Pais(db,T)
Universidad(db,T)
UsuarioUSB(db,T)
Administrativo(db,T)
Carrera(db,T)
Coordinador(db,T)
Estado(db,T)
Profesor(db,T)
UsuarioExterno(db,T)
Empresa(db,T)
Estudiante(db,T)
Tutor_Industrial(db,T)
Curriculo(db,T)
Pasantia(db,T)
Permiso(db,T)
Retiro(db,T)
Colocacion(db,T)
Ejecucion(db,T)
Inscripcion(db,T)
Plan_Trabajo(db,T)
Preinscripcion(db,T)
Fase(db,T)
Actividad(db,T)
Materia_Periodo(db,T)
# Cargamos La Data Predeterminada
load_fixtures(db,T)