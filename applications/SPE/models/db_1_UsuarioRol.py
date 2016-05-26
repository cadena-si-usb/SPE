db.define_table('UsuarioRol',
                Field('usuario','reference UsuarioUSB',required=True,ondelete='CASCADE',
                    notnull=True, unique=True,label='Usuario'),
                Field('rol','reference Rol', required=True, notnull=True,label=T('Rol')),
                format='%(nombre)s')

db.Universidad.nombre.requires=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
db.Universidad.nombre.requires+=[IS_LENGTH(512)]
db.Universidad.nombre.requires+=[IS_NOT_IN_DB(db, 'Universidad.nombre',error_message=T('Universidad ya registrada'))]

db.Universidad.id_pais.requires=IS_IN_DB(db,db.Pais.id,'%(nombre)s')
