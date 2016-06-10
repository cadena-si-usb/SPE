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
