db.define_table('Acceso_Etapa',
    Field('rol',
          'reference auth_group', '%(nombre)s',
          label='Rol (*)'),
    Field('etapa','reference Etapa',
          label='Etapas (*)'))