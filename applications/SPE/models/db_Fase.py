db.define_table('Fase',
    Field('titulo','string',
          requires=[IS_NOT_EMPTY
                        (error_message='Es necesario una Descripcion')],
          label = 'Titulo'),
    Field('descripcion','text',
          requires=[IS_NOT_EMPTY
                        (error_message='Es necesario una Descripcion')],
          label='Descripcion'),
    Field('plan_trabajo',##referencia a tabla Plan_Trabajo.
          label='Plan de Trabajo')
)
