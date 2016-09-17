from Etapas import Etapa

import Encoder

Etapa = Etapa()

def etapas():
    obj = Encoder.to_dict(request.vars)

    rows = Etapa.find(obj)

    response.view = 'mis_pasantias/etapas.load.html'
    return dict(etapas=rows.as_list(),id="id")