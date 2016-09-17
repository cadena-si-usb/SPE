db.define_table('Acceso_Etapa',
    Field('rol',
          requires=IS_IN_DB(db, db.Rol, '%(nombre)s',
          error_message='Elija uno de los roles.'),
          label='Rol (*)'),
    Field('etapa',
          requires=IS_IN_DB(db, db.Etapa, '%(nombre)s',
          error_message='Elija una de las etapas.'),
          label='Etapas (*)'))