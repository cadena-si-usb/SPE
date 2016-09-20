db.define_table('Fase',
    Field('numero','integer',
          requires=[IS_NOT_EMPTY
                        (error_message='Es necesario un numero de identificacion')],
          label = 'Numero'),
    Field('plan_trabajo', 'reference Plan_Trabajo', 
          requires=IS_IN_DB(db, db.Plan_Trabajo, '%(pasantia)s',
          error_message='Elija uno de los planes de trabajo.'),
          label='Pasantía (*)'),
    Field('descripcion','text',
          requires=[IS_NOT_EMPTY
                        (error_message='Es necesario una Descripcion')],
          label = 'Descripcón'),
)
