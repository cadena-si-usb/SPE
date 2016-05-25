# -*- coding: utf-8 -*-


db.define_table('Plan_Trabajo',
    Field('pasantia','reference Pasantia',
          label='Pasantia' ),
    Field('objetivo_general','string',
          label='Obejtivos Especificos')
)
