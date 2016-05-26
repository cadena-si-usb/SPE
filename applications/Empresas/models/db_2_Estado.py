db.define_table('Estado',
    Field('nombre','string'),
    Field('Pais', 'reference Pais'))

db.Estado.Pais.requires=IS_IN_DB(db,db.Pais.id,'%(nombre)s')