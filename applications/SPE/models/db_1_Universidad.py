'''
    `id`        int(11)         NOT NULL AUTO_INCREMENT,
    `nombre`    varchar(254)    NOT NULL,
    `id_pais`   int(11)         NOT NULL,
'''

db.define_table('Universidad',
                Field('nombre','string',required=True,ondelete='CASCADE',
                    notnull=True, unique=True,label='Universidad'),
                Field('id_pais','reference Pais', required=True, notnull=True,label=T('Pais')),
                format='%(nombre)s')

db.Universidad.nombre.requires=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
db.Universidad.nombre.requires+=[IS_LENGTH(512)]
db.Universidad.nombre.requires+=[IS_NOT_IN_DB(db, 'Universidad.nombre',error_message=T('Universidad ya registrada'))]

db.Universidad.id_pais.requires=IS_IN_DB(db,db.Pais.id,'%(nombre)s')
