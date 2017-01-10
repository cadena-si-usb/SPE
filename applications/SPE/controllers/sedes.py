# -*- coding: utf-8 -*-
from Sedes import Sede
from Usuarios import Usuario
from applications.SPE_lib.modules.grids import single_table_spe_grid
Usuario=Usuario()
import Encoder
Sede = Sede()

def sqlform_grid():
    sqlform_grid = single_table_spe_grid(db.Sede)
    return sqlform_grid

@auth.requires(Usuario.checkUserPermission(construirAccion(request.application,request.controller)))
def listar():
    session.rows = []
    return dict(rows=session.rows,id="prueba")
