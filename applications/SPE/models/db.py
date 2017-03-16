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

from applications.SPE_lib.modules.db_0_Auth_Tables import spe_auth_tables
from applications.SPE_lib.modules.db_0_Area_Laboral import Area_Laboral_Table
from applications.SPE_lib.modules.db_0_Area_Proyecto import Area_Proyecto_Table
from applications.SPE_lib.modules.db_0_Categoria import Categoria_Table
from applications.SPE_lib.modules.db_0_Dedicacion import Dedicacion_Table
from applications.SPE_lib.modules.db_0_Division import Division_Table
from applications.SPE_lib.modules.db_0_Etapa import Etapa_Table
from applications.SPE_lib.modules.db_0_Periodo import Periodo_Table
from applications.SPE_lib.modules.db_0_Sede import Sede_Table
from applications.SPE_lib.modules.db_0_Tipo_Documento import Tipo_Documento_Table
from applications.SPE_lib.modules.db_1_Accion import Accion_Table
from applications.SPE_lib.modules.db_1_Acceso_Etapa import Acceso_Etapa_Table
from applications.SPE_lib.modules.db_1_Accion_Usuario import Accion_Usuario_Table
from applications.SPE_lib.modules.db_1_Coordinacion import Coordinacion_Table
from applications.SPE_lib.modules.db_1_correo_Por_Verificar import correo_por_verificar_Table
from applications.SPE_lib.modules.db_1_Departamento import Departamento_Table
from applications.SPE_lib.modules.db_1_Materia import Materia_Table
from applications.SPE_lib.modules.db_1_Pais import Pais_Table
from applications.SPE_lib.modules.db_1_Universidad import Universidad_Table
from applications.SPE_lib.modules.db_2_Administrativo import Administrativo_Table
from applications.SPE_lib.modules.db_2_Carrera import Carrera_Table
from applications.SPE_lib.modules.db_2_Coordinador import Coordinador_Table
from applications.SPE_lib.modules.db_2_Estado import Estado_Table
from applications.SPE_lib.modules.db_2_Profesor import Profesor_Table
from applications.SPE_lib.modules.db_3_Empresa import Empresa_Table
from applications.SPE_lib.modules.db_3_Estudiante import Estudiante_Table
from applications.SPE_lib.modules.db_3_Tutor_Industrial import Tutor_Industrial_Table

from applications.SPE_lib.modules.db_4_Curriculo import Curriculo_Table
from applications.SPE_lib.modules.db_4_Pasantia import Pasantia_Table
from applications.SPE_lib.modules.db_4_Permiso import Permiso_Table
from applications.SPE_lib.modules.db_4_Permiso_Evaluacion import Permiso_Evaluacion_Table
from applications.SPE_lib.modules.db_4_Retiro import Retiro_Table

from applications.SPE_lib.modules.db_5_Colocacion import Colocacion_Table
from applications.SPE_lib.modules.db_5_Ejecucion import Ejecucion_Table
from applications.SPE_lib.modules.db_5_Inscripcion import Inscripcion_Table
from applications.SPE_lib.modules.db_5_Plan_Trabajo import Plan_Trabajo_Table
from applications.SPE_lib.modules.db_5_Preinscripcion import Preinscripcion_Table
from applications.SPE_lib.modules.db_5_Calendario import Calendario_Table

from applications.SPE_lib.modules.db_6_Fase import Fase_Table

from applications.SPE_lib.modules.db_7_Actividad import Actividad_Table
from applications.SPE_lib.modules.db_7_Materia_Periodo import Materia_Periodo_Table
from applications.SPE_lib.modules.db_7_Solicitud_Modificacion import Solicitud_Modificacion_Table

from applications.SPE_lib.modules.fixtures import load_auth_fixtures
# Se importan aqui para no tener que importarlos en el resto del sistema
from Acciones_Usuario import construirAccion as construirAccion
from Usuarios import Usuario

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

Sede_Table(db,T)
Tipo_Documento_Table(db,T)
Pais_Table(db,T)
Estado_Table(db,T)
auth = spe_auth_tables(db,T)

current.auth = auth
service = Service()
plugins = PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=True, signature=False)

def format_user(row):
    if row.username:
        return row.username + ": " + row.first_name + " " + row.last_name
    elif not row.username and row.last_name:
        return row.email + ": " + row.first_name + " " + row.last_name
    elif not row.username and not row.last_name:
        return row.email + ": " + row.first_name

db.auth_user._format = lambda row: format_user(row)
db.auth_user.username.readonly=True
db.auth_user.email.readonly=True
db.auth_user.username.label="USB-ID"
db.auth_user.first_name.label="Nombre"
db.auth_user.last_name.label="Apellidos"
db.auth_user.image.label="Foto de perfil"

load_auth_fixtures(db,T)

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
Area_Laboral_Table(db,T)
Area_Proyecto_Table(db,T)
Categoria_Table(db,T)
Dedicacion_Table(db,T)
Division_Table(db,T)
Etapa_Table(db,T)
Periodo_Table(db,T)
Acceso_Etapa_Table(db,T)
Accion_Table(db,T)
Accion_Usuario_Table(db,T)
Coordinacion_Table(db,T)
correo_por_verificar_Table(db,T)
Departamento_Table(db,T)
Materia_Table(db,T)
Universidad_Table(db,T)
Administrativo_Table(db,T)
Carrera_Table(db,T)
Coordinador_Table(db,T)
Profesor_Table(db,T)
Empresa_Table(db,T)
Estudiante_Table(db,T)
Tutor_Industrial_Table(db,T)
Curriculo_Table(db,T)
Pasantia_Table(db,T)
Permiso_Table(db,T)
Permiso_Evaluacion_Table(db,T)
Retiro_Table(db,T)
Calendario_Table(db,T)
Colocacion_Table(db,T)
Ejecucion_Table(db,T)
Inscripcion_Table(db,T)
Plan_Trabajo_Table(db,T)
Preinscripcion_Table(db,T)
Fase_Table(db,T)
Actividad_Table(db,T)
Materia_Periodo_Table(db,T)
Solicitud_Modificacion_Table(db,T)
# Cargamos La Data Predeterminada
