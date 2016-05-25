# -*- coding: utf-8 -*-

# Actividad
db.define_table('Coordinacion',
                Field('nombre','string',required=True),
                Field('usbid','string',required=True),
                Field('sede','string',required=True, requires=IS_IN_SET(['Sartenejas','Litoral'],zero=None)),
                format='%(sede)s - %(nombre)s'
               )

db.Coordinacion.usbid.requires+=[IS_NOT_IN_DB(db, 'Coordinacion.usbid',error_message=T('Coordinacion ya registrado'))]
