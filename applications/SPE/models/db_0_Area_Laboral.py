db.define_table('Area_Laboral',
                Field('nombre', 'string', required=True, ondelete='CASCADE',
                      notnull=True, label='Area Laboral'),
                Field('descripcion', 'text', required=True, notnull=True, label=T('Descripcion del Area Laboral')),
                format='%(nombre)s')

db.Area_Laboral.nombre.requires=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
db.Area_Laboral.nombre.requires+=[IS_LENGTH(512)]
db.Area_Laboral.nombre.requires+=[IS_NOT_IN_DB(db, 'Area_Laboral.nombre',error_message=T('Area Laboral ya registrado'))]
