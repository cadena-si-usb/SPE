from Etapas import Etapa

import Encoder
from applications.SPE_lib.modules.grids import single_table_spe_grid
Etapa = Etapa()

def sqlform_grid():
    sqlform_grid = single_table_spe_grid(db.Etapa)
    return sqlform_grid

def etapas():
    userid = session.currentUser.id
    currentUser = db.auth_user(db.auth_user.id == userid)
    estudiante = db(((db.auth_user.id == userid) & (db.Estudiante.usuario == db.auth_user.id))).select().first()
    pasantia = db(db.Pasantia.estudiante == estudiante.Estudiante).select().first()

    obj = Encoder.to_dict(request.vars)
    rows = Etapa.find(obj)

    response.view = 'mis_pasantias/etapas.load.html'
    return dict(etapas=rows.as_list(), id="id", pasantia=pasantia)
