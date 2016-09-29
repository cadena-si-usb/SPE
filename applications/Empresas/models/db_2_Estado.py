db.define_table('Estado',
    Field('nombre','string'),
    Field('Pais', 'reference Pais'),
    format=lambda r: '%s - %s' % (r.Pais.nombre, r.nombre))