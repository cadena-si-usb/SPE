# -*- coding: utf-8 -*-

# Proceso de registro en el cual un tutor solicita un registro a una Empresa
from shlex import shlex

@auth.requires(auth.is_logged_in() and auth.has_membership(role='Coordinador'))
def consultarPasantias():
    userId=auth.user.id
    coordinador=db.Coordinador(id=userId)
    coordinacion=db.Coordinacion(id=coordinador.coordinacion)
    carrera=db.Carrera(coordinacion=coordinacion.id)
    correo = auth.user.email
    pasantias=db((db.Estudiante.id==db.Pasantia.estudiante) & (db.Estudiante.carrera==carrera.id))

    prueba=pasantias.select().first()

    #Define the fields to show on grid. Note: (you need to specify id field in fields section in 1.99.2
    # this is not required in later versions)
    fields = (db.Pasantia.titulo, db.Pasantia.estudiante,db.Pasantia.etapa, db.Pasantia.status)

    #Define headers as tuples/dictionaries
    headers = {
            ''
            'Pasantia.titulo': 'Titulo',
            'Pasantia.estudiante':'Estudiante',
            'Pasantia.etapa':'Etapa',
            'Pasantia.status': 'Status' }

    #Let's specify a default sort order on date_of_birth column in grid
    default_sort_order=[db.Pasantia.titulo]
    links = [lambda row: A('Detalle', _href=URL(c='Pasantia',f='verDetallePasantia',args=[row.id]))]

    #Creating the grid object
    form = SQLFORM.grid(query=pasantias, fields=fields, headers=headers, orderby=default_sort_order,
                create=False, deletable=False, editable=False, maxtextlength=64, paginate=25,details=False,
                links=links,csv=False,user_signature=False)

    response.view = 'Coordinador/Consultar_Pasantias.html'
    return locals()