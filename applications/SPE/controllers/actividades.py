# -*- coding: utf-8 -*-
from Acceso_Etapa import Acceso_Etapa
from Usuarios import Usuario
import Encoder
from applications.SPE_lib.modules.grids import simple_spe_grid
Acceso_Etapa = Acceso_Etapa()
Usuario = Usuario()

def cambiar_estado():
    record = db.Actividad(request.args(0))
    fase = db.Fase(id=record.fase)
    plan_trabajo = db.Plan_Trabajo(id=fase.plan_trabajo)

    record.update_record(terminada=(not record.terminada))
    redirect(URL(c='mis_pasantias', f='ver', args=[plan_trabajo.pasantia]))