db.define_table('Estado',
    Field('nombre','string'),
    Field('Pais', 'reference Pais'))