db.define_table('Fase',
    Field('plan_trabajo', 'reference Plan_Trabajo',  ##referencia a tabla Plan_Trabajo.
          label='Plan de Trabajo'),
    Field('titulo','string',
          requires=[IS_NOT_EMPTY
                        (error_message='Es necesario una Descripcion')],
          label = 'Titulo'),
    Field('descripcion','text',
          requires=[IS_NOT_EMPTY
                        (error_message='Es necesario una Descripcion')],
          label='Descripcion'),
    Field('objetivo_especifico', 'String',
          label='Objetivo Especifico')
)
