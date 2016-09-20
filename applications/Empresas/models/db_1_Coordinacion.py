# -*- coding: utf-8 -*-

# Actividad
db.define_table('Coordinacion',
                Field('nombre','string',required=True),
                Field('usbid','string',required=True),
                Field('sede','reference Sede',
				          requires=IS_IN_DB(db, db.Sede, '%(nombre)s',
				          error_message='Elija una de los sedes.'),
				          label='Sedes (*)'),
                format='%(nombre)s'
               )

db.Coordinacion.usbid.requires+=[IS_NOT_IN_DB(db, 'Coordinacion.usbid',error_message=T('Coordinacion ya registrado'))]
