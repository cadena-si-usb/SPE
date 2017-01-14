# -*- coding: utf-8 -*-
from Tutores_Industriales import Tutor_Industrial

import Encoder
from applications.SPE_lib.modules.grids import simple_spe_grid
Tutor_Industrial = Tutor_Industrial()

def sqlform_grid():
    fields = [db.Tutor_Industrial.usuario,
              db.Tutor_Industrial.Empresa]
    if not request.args:
        return simple_spe_grid(db.Tutor_Industrial,
                                     fields=fields)
    elif request.args[-2] == 'new':
        return agregar(request)
    elif request.args[-3] == 'edit':
        return modificar(request)
    elif request.args[-3] == 'view':
        return ver(request)
    else:
        return simple_spe_grid(db.Tutor_Industrial)

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows)

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def agregar(request):
    # Agregamos los campos en el orden deseado, comenzamos con el login y el password
    fields = [
        db.auth_user.email,
        db.auth_user.first_name,
        db.Tutor_Industrial.last_name,
        db.Tutor_Industrial.tipo_documento,
        db.Tutor_Industrial.numero_documento,
        db.auth_user.password
    ]
    # Agregamos el resto de los campos
    fields += [
        db.auth_user.pregunta_secreta,
        db.auth_user.respuesta_secreta,
        db.Tutor_Industrial.profesion,
        db.Tutor_Industrial.cargo,
        db.Tutor_Industrial.departamento,
        db.auth_user.pais,
        db.auth_user.estado,
        db.Tutor_Industrial.Empresa,
        db.Tutor_Industrial.universidad,
        db.auth_user.direccion,
        db.auth_user.telefono
    ]
    # Generamos el SQLFORM utilizando los campos
    form = SQLFORM.factory(
        *fields,
        submit_button='Submit',
        separator=': ',
        buttons=['submit'],
        col3={
            'email': T('Identificación de acceso unica asignada a la Empresa'),
            'first_name': T('Nombre comercial de la Empresa'),
            'last_name': T('Nombre comercial de la Empresa'),
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
    referrer = session.get('_web2py_grid_referrer_' + 'web2py_grid', url())
    form.process.next = referrer
    # Caso 1: El form se lleno de manera correcta asi que registramos al tutor y procedemos a la pagina de exito
    if form.process().accepted:
        # Insertamos en la tabla user de Web2py
        result = db.auth_user.insert(
            username=request.vars.email,
            first_name=request.vars.first_name,
            last_name=request.vars.last_name,
            password=db.auth_user.password.validate(request.vars.password)[0],
            email=request.vars.email,pregunta_secreta=request.vars.pregunta_secreta,
            respuesta_secreta=request.vars.respuesta_secreta,
            pais=request.vars.pais,
            estado=request.vars.estado,
            telefono=request.vars.telefono,
            direccion=request.vars.direccion,

        )
        # Registramos al tutor
        db.Tutor_Industrial.insert(
            id=result,
            usuario=result,
            last_name=request.vars.last_name,
            tipo_documento=request.vars.tipo_documento,
            numero_documento=request.vars.numero_documento,
            Empresa=request.vars.Empresa,
            profesion=request.vars.profesion,
            cargo=request.vars.cargo,
            departamento=request.vars.departamento,
            universidad=request.vars.universidad,
            comfirmado_Por_Empresa=0
        )
        # Actualizo los datos exclusivos de estudiante
        session.flash = T('Perfil actualizado exitosamente!')
        return simple_spe_grid(db.Tutor_Industrial)
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return form

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def count():
    obj = Encoder.to_dict(request.vars)
    count = Tutor_Industrial.count(obj)

    return count

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def get():
    obj = Encoder.to_dict(request.vars)

    empresa_auth = db.auth_user.with_alias('empresa_auth')

    rows = db((db.Tutor_Industrial.usuario == db.auth_user.id) &
              (db.Tutor_Industrial.Empresa == db.Empresa.id) & (db.Empresa.usuario == db.empresa_auth.id)).select()

    return rows.as_json()

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def modificar(request):
    # Buscamos la informacion de tutor
    tutor = db.Tutor_Industrial(id=request.args[-1])
    # Buscamos la informacion general del usuario
    auth_user = db.auth_user(id=tutor.usuario)


    db.auth_user.email.requires = []
    db.auth_user.email.default = auth_user.email
    db.auth_user.pregunta_secreta.default = auth_user.pregunta_secreta
    db.auth_user.respuesta_secreta.default = auth_user.respuesta_secreta
    db.auth_user.first_name.default = auth_user.first_name
    db.auth_user.pais.default = auth_user.pais
    db.auth_user.estado.default = auth_user.estado

    db.auth_user.last_name.default = auth_user.last_name
    db.Tutor_Industrial.Empresa.default = tutor.Empresa
    db.Tutor_Industrial.profesion.default = tutor.profesion
    db.auth_user.tipo_documento.default = auth_user.tipo_documento
    db.auth_user.numero_documento.default = auth_user.numero_documento
    db.Tutor_Industrial.cargo.default = tutor.cargo
    db.Tutor_Industrial.departamento.default = tutor.departamento
    db.Tutor_Industrial.universidad.default = tutor.universidad
    db.auth_user.direccion.default = auth_user.direccion
    db.auth_user.telefono.default = auth_user.telefono

    fields = [
        'email',
        'first_name',
        'last_name',
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
    form = SQLFORM.factory(db.auth_user, db.Tutor_Industrial, fields=fields, submit_button='Actualizar',
                           showid=False)
    referrer = session.get('_web2py_grid_referrer_' + 'web2py_grid', request.controller + '/' + request.function)
    form.process().next = referrer
    if form.accepts(request.vars):
        id = auth_user.update_record(**db.auth_user._filter_fields(form.vars))
        id = tutor.update_record(**db.Tutor_Industrial._filter_fields(form.vars))
        redirect(URL('sqlform_grid'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return form

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def ver(request):
    # Buscamos la informacion de tutor
    tutor = db.Tutor_Industrial(id=request.args[-1])
    # Buscamos la informacion general del usuario
    auth_user = db.auth_user(id=tutor.usuario)

    db.auth_user.email.requires = []
    db.auth_user.email.default = auth_user.email
    db.auth_user.pregunta_secreta.default = auth_user.pregunta_secreta
    db.auth_user.respuesta_secreta.default = auth_user.respuesta_secreta
    db.auth_user.first_name.default = auth_user.first_name
    db.auth_user.pais.default = auth_user.pais
    db.auth_user.estado.default = auth_user.estado

    db.auth_user.last_name.default = auth_user.last_name
    db.Tutor_Industrial.Empresa.default = tutor.Empresa
    db.Tutor_Industrial.profesion.default = tutor.profesion
    db.auth_user.tipo_documento.default = auth_user.tipo_documento
    db.auth_user.numero_documento.default = auth_user.numero_documento
    db.Tutor_Industrial.cargo.default = tutor.cargo
    db.Tutor_Industrial.departamento.default = tutor.departamento
    db.Tutor_Industrial.universidad.default = tutor.universidad
    db.auth_user.direccion.default = auth_user.direccion
    db.auth_user.telefono.default = auth_user.telefono

    fields = [
        'email',
        'first_name',
        'last_name',
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
    form = SQLFORM.factory(db.auth_user, db.Tutor_Industrial, fields=fields, submit_button='Actualizar',readonly=True,
                           showid=False)

    if form.accepts(request.vars):
        id = auth_user.update_record(**db.auth_user._filter_fields(form.vars))
        id = tutor.update_record(**db.Tutor_Industrial._filter_fields(form.vars))
        session.flash = T('Perfil actualizado exitosamente!')
        redirect(URL('sqlform_grid'))
    elif form.errors:
        response.flash = T('La forma tiene errores, por favor llenela correctamente.')
    else:
        response.flash = T('Por favor llene la forma.')

    return form