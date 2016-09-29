db.define_table('Acceso_Etapa',
    Field('rol',
          'reference Rol', '%(nombre)s',
          label='Rol (*)'),
    Field('etapa','reference Etapa',
          label='Etapas (*)'))