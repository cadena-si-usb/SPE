db.define_table('Area_Proyecto',
                Field('nombre', 'string', required=True, ondelete='CASCADE',
                      notnull=True, label='Área del Proyecto'),
                Field('descripcion', 'text', required=True, notnull=True, label=T('Descripcion del Area del Proyecto')),
                format='%(nombre)s')

db.Area_Proyecto.nombre.requires=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
db.Area_Proyecto.nombre.requires+=[IS_LENGTH(512)]
db.Area_Proyecto.nombre.requires+=[IS_NOT_IN_DB(db, 'Area_Proyecto.nombre',error_message=T('Area de Proyecto ya registrada'))]
