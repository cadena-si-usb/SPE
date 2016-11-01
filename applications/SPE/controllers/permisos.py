# -*- coding: utf-8 -*-
from Permisos import Permiso
from Permisos_Evaluacion import Permiso_Evaluacion
from gluon import current
import Encoder

Permiso = Permiso()
Permiso_Evaluacion = Permiso_Evaluacion()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows)


''' Refactorizar: Separar en dos funciones, una que sea agregar y agregarPorRol 
    para evitar el try
'''
@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar():
    try:
        tipo = request.args[0]
    except IndexError:
        tipo = None 

    currentRoles = current.auth.user_groups.values()
    permisoBD = db.Permiso
    fieldsEstudianteInscr = ['Tipo','pasantia','justificacion']
    fieldsCoordinadorCCTInscr = ['Estudiante', 'Tipo', 'pasantia', 'justificacion']
    fieldsEstudianteEval = ['Tipo','pasantia', 'justificacion', 'calendario_compromisos']
    fieldsCoordinadorCCTEval = ['Estudiante', 'Tipo', 'pasantia', 'justificacion', 'calendario_compromisos']
    

    if 'Estudiante' in currentRoles:
        permisoBD.Estudiante.writable = False
        permisoBD.Estudiante.default = current.auth.user_id
        
        permisoBD.Tipo.writable = False
        if tipo == 'Inscripcion Extemporanea':
            permisoBD.Tipo.default = 'Inscripcion Extemporanea'
            form = Permiso.form(fieldsEstudianteInscr)
        elif tipo == 'Retiro Extemporaneo':
            permisoBD.Tipo.default = 'Retiro Extemporaneo'
            form = Permiso.form(fieldsEstudianteInscr)
        elif tipo == 'Evaluacion Extemporanea':
            permisoBD.Tipo.default = 'Evaluacion Extemporanea'
            form = Permiso.form(fieldsEstudianteEval)

    # Caso en el que se llama a la funcion agregar desde la interfaz con ajax
    elif ('CoordinadorCCT' in currentRoles) or not tipo:

        if tipo == 'Inscripcion Extemporanea':
            permisoBD.Tipo.writable = False
            permisoBD.Tipo.default = 'Inscripcion Extemporanea'
            form = Permiso.form(fieldsCoordinadorCCTInscr)
        elif tipo == 'Retiro Extemporaneo':
            permisoBD.Tipo.writable = False
            permisoBD.Tipo.default = 'Retiro Extemporaneo'
            form = Permiso.form(fieldsCoordinadorCCTInscr)
        elif tipo == 'Evaluacion Extemporanea':
            permisoBD.Tipo.writable = False
            permisoBD.Tipo.default = 'Evaluacion Extemporanea'
            form = Permiso.form(fieldsCoordinadorCCTEval)
        elif not tipo:
            form = Permiso.form(fieldsCoordinadorCCTEval)

    else:
        redirect(URL(c='default', f='index'))


    if form.process().accepted:
        session.flash = T('El material fue agregado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')
  
    return locals()



@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def count():
    obj = Encoder.to_dict(request.vars)
    count = Permiso.count(obj)
    return count


''' Hacer que devuelva ambos tipos de pasantía'''
@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    rows = Permiso.find(obj).as_json()
    return rows


@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar():

    currentRoles = current.auth.user_groups.values()
    record = (db.Permiso(request.args(0)) or db.Permiso_Evaluacion(request.args(0))) or redirect(URL('agregar'))

    if 'Estudiante' in currentRoles:
        fields = ['justificacion']
        form = SQLFORM(db.Permiso,record,fields=fields,showid=False)
    if 'Profesor' in currentRoles:
        fields = ['aprobacion_tutor_academico']
        form = SQLFORM(db.Permiso,record,fields=fields,showid=False)
    elif 'Coordinador' in currentRoles:
        fields = ['aprobacion_coordinacion']
        form = SQLFORM(db.Permiso,record,fields=fields,showid=False)
    elif 'CoordinadorCCT' in currentRoles:
        form = SQLFORM(db.Permiso,record,fields=None,showid=False)
    else:
        redirect(URL(c='default', f='index'))


    if form.process().accepted:
        session.flash = T('El material fue agregado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')
    
    return locals()



@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def ver():
    record = db.Permiso(request.args(0))
    return locals()
