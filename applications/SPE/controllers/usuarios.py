# -*- coding: utf-8 -*-
from Usuarios import Usuario
from Carreras import Carrera
from Sedes import Sede
from Tipos_Documento import Tipo_Documento

import Encoder

Usuario = Usuario()
Carrera = Carrera()
Sede = Sede()
Tipo_Documento = Tipo_Documento()

def listar():
    session.rows = []
    return dict(rows=session.rows)

def agregar():
   # fields = ['id','nombre','apellido','ci']

    form = SQLFORM(db.Usuario)

    if form.process().accepted:
        session.flash = T('El material fue agregado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()

def count():
    obj = Encoder.to_dict(request.vars)
    count = Usuario.count(obj)

    return count

def get():
    obj = Encoder.to_dict(request.vars)

    rows = Usuario.find(obj)

    rows = rows.as_json()

    return rows

def modificar():
    record = db.Usuario(request.args(0)) or redirect(URL('agregar'))
    form = SQLFORM(db.Usuario, record)
    if form.process().accepted:
        session.flash = T('El material fue modificado exitosamente!')
        redirect(URL('listar'))
    else:
        response.flash = T('Por favor llene la forma.')
    return locals()

def perfil():
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

    userid = str(auth.user['username'])

    usuario = db.UsuarioUSB(db.UsuarioUSB.usbid == userid)


    form = SQLFORM(db.UsuarioUSB,record=usuario,fields=fields,submit_button='Actualizar',showid=False)

    if form.process().accepted:
        session.flash = T('Perfil actualizado exitosamente!')
        usuario.update_record(activo=True)
        session.currentUser = Usuario.getByRole(usuario['usbid'])
        redirect(URL('perfil'))
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()

def perfil_estudiante():
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


def curriculo():
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
        redirect(URL('curriculo'))
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()