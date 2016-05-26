db.define_table('Estado',
    Field('nombre','string'),
    Field('Pais', 'reference Pais'),
    format='%(nombre)s')

db.Estado.Pais.requires=IS_IN_DB(db,db.Pais.id,'%(nombre)s')