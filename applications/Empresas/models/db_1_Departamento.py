# -*- coding: utf-8 -*-
# Departamento
db.define_table('Departamento',
                Field('nombre','string', requires=IS_NOT_EMPTY(), default='', label="Nombre del Departamento"),
                Field('id_division','reference division', represent=lambda x, row: (db(db.Division.id==x)).select().first().nombre,requires=IS_IN_DB(db,'Division.id', '%(nombre)s',error_message='Division no Existe'), notnull=True, label='Nombre de División'),
                Field('email_dep','string',label='Correo Electrónico del Departamento'),
                Field('sede','string', requires=IS_IN_SET(['Sartenejas','Litoral'],error_message='Sede Inválida'), label='Sede', notnull=True))


# Validadores
db.Departamento.email_dep.requires=[IS_EMAIL(error_message=T('Este no es un correo valido'))]
db.Departamento.email_dep.requires+=[IS_LENGTH(100)]
db.Departamento.email_dep.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
