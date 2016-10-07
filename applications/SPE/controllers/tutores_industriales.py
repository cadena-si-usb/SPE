# -*- coding: utf-8 -*-
from Estudiantes import Estudiante

import Encoder

Estudiante = Estudiante()

def listar():
    session.rows = []
    return dict(rows=session.rows)

def agregar():
    # Agregamos los campos en el orden deseado, comenzamos con el login y el password
    fields = [
        db.UsuarioExterno.correo,
        db.UsuarioExterno.nombre,
        db.Tutor_Industrial.apellido,
        db.Tutor_Industrial.tipo_documento,
        db.Tutor_Industrial.numero_documento,
        db.auth_user.password
    ]
    # Agregamos el resto de los campos
    fields += [
        db.UsuarioExterno.pregunta_secreta,
        db.UsuarioExterno.respuesta_secreta,
        db.Tutor_Industrial.profesion,
        db.Tutor_Industrial.cargo,
        db.Tutor_Industrial.departamento,
        db.UsuarioExterno.pais,
        db.UsuarioExterno.estado,
        db.Tutor_Industrial.universidad,
        db.UsuarioExterno.direccion,
        db.UsuarioExterno.telefono
    ]
    # Generamos el SQLFORM utilizando los campos
    form = SQLFORM.factory(
        *fields,
        submit_button='Submit',
        separator=': ',
        buttons=['submit'],
        col3={
            'correo': T('Identificación de acceso unica asignada a la Empresa'),
            'nombre': T('Nombre comercial de la Empresa'),
            'apellido': T('Nombre comercial de la Empresa'),
            'tipo_documento': T('Tipo De Documento'),
            'numero_documento': T('Numero De Documento'),
            'password': T('Contraseña para acceder al sistema'),
            'comfirm_Password': T('Repita su contraseña'),
            'pregunta_secreta': T('Si necesita obtener de nuevo su contraseña se le hara esta pregunta'),
            'respuesta_secreta': T('Respuesta a su pregunta secreta'),
            'profesion': T('Profesion del tutor industrial'),
            'cargo': T('Cargo que ocupa en la Empresa'),
            'departamento': T('Departamento de la Empresa en la que trabaja'),
            'direccion': T('Direccion del tutor industrial'),
            'pais': T('Pais en el que se encuentra domiciliado el tutor industrial'),
            'estado': T('Estado en el que se encuentra domiciliado el tutor industrial'),
            'universidad': T('Universidad de la cual egreso el tutor'),
            'telefono': T('Numerico telefonico del tutor industrial')
              })
    # Caso 1: El form se lleno de manera correcta asi que registramos al tutor y procedemos a la pagina de exito
    if form.process().accepted:

        # Insertamos en la tabla user de Web2py
        result = db.auth_user.insert(
            first_name=request.vars.nombre,
            last_name=request.vars.apellido,
            password=db.auth_user.password.validate(request.vars.password)[0],
            email=request.vars.correo,
        )

        # Registramos el usuario externo
        db.UsuarioExterno.insert(
            id=result,
            auth_User=result,
            correo=request.vars.correo,
            pregunta_secreta=request.vars.pregunta_secreta,
            respuesta_secreta=request.vars.respuesta_secreta,
            nombre=request.vars.nombre,
            pais=request.vars.pais,
            estado=request.vars.estado,
            telefono=request.vars.telefono,
            direccion=request.vars.direccion,
        )

        usuarioExternoSet = db(db.UsuarioExterno,db.UsuarioExterno.correo == request.vars.correo).select()
        usuarioExterno = usuarioExternoSet[0]

        empresa = \
            db(db.Empresa, db.Empresa.usuario == usuarioExterno.id).select()[0]

        # Registramos al tutor
        db.Tutor_Industrial.insert(
            id=result,
            usuario=result,
            apellido=request.vars.apellido,
            tipo_documento=request.vars.tipo_documento,
            numero_documento=request.vars.numero_documento,
            Empresa=empresa.id,
            profesion=request.vars.profesion,
            cargo=request.vars.cargo,
            departamento=request.vars.departamento,
            universidad=request.vars.universidad,
            comfirmado_Por_Empresa=0
        )
        # Actualizo los datos exclusivos de estudiante
        session.flash = T('Perfil actualizado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()

def count():
    obj = Encoder.to_dict(request.vars)
    count = Estudiante.count(obj)

    return count

def get():
    obj = Encoder.to_dict(request.vars)

    rows = db((db.Tutor_Industrial.usuario == db.auth_user.id) &
              (db.Tutor_Industrial.Empresa == db.Empresa.id) & (db.Empresa.usuario == db.UsuarioExterno.id)).select()

    return rows.as_json()

def modificar():
    prueba=request.args[0]
    tutor = db(db.Tutor_Industrial.id == request.args[0]).select().first()
    usuarioExterno = db(tutor.usuario == db.UsuarioExterno.id).select().first()

    db.UsuarioExterno.correo.requires = []
    db.UsuarioExterno.correo.default = usuarioExterno.correo
    db.UsuarioExterno.pregunta_secreta.default = usuarioExterno.pregunta_secreta
    db.UsuarioExterno.respuesta_secreta.default = usuarioExterno.respuesta_secreta
    db.UsuarioExterno.nombre.default = usuarioExterno.nombre
    db.UsuarioExterno.pais.default = usuarioExterno.pais
    db.UsuarioExterno.estado.default = usuarioExterno.estado

    db.Tutor_Industrial.apellido.default = tutor.apellido
    db.Tutor_Industrial.Empresa.default = tutor.Empresa
    db.Tutor_Industrial.profesion.default = tutor.profesion
    db.Tutor_Industrial.tipo_documento.default = tutor.tipo_documento
    db.Tutor_Industrial.numero_documento.default = tutor.numero_documento
    db.Tutor_Industrial.cargo.default = tutor.cargo
    db.Tutor_Industrial.departamento.default = tutor.departamento
    db.Tutor_Industrial.universidad.default = tutor.universidad
    db.UsuarioExterno.direccion.default = usuarioExterno.direccion
    db.UsuarioExterno.telefono.default = usuarioExterno.telefono

    db.Tutor_Industrial.Empresa.writable = False

    fields = [
        'correo',
        'nombre',
        'apellido',
        'tipo_documento',
        'numero_documento',
        'Empresa',
        'pregunta_secreta',
        'respuesta_secreta',
        'profesion',
        'cargo',
        'departamento',
        'pais',
        'estado',
        'universidad',
        'direccion',
        'telefono'
    ]
    form = SQLFORM.factory(db.UsuarioExterno, db.Tutor_Industrial, fields=fields, submit_button='Actualizar',
                           showid=False)

    if form.accepts(request.vars):
        db(db.auth_user.id == auth.user.id).update(
            email=request.vars.correo,
            first_name=request.vars.nombre,
            last_name=request.vars.apellido,
        )

        id = usuarioExterno.update_record(**db.UsuarioExterno._filter_fields(form.vars))
        form.vars.client = id
        id = tutor.update_record(**db.Tutor_Industrial._filter_fields(form.vars))
        session.flash = T('Perfil actualizado exitosamente!')
        redirect(URL('listar'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return locals()