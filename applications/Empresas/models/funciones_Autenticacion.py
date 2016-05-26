# Funciones disponibles en todo el codigo.

def es_Empresa(correo):
    empresa = db(db.Empresa,db.Empresa.usuario == db.UsuarioExterno.id)(db.UsuarioExterno.correo == correo).select()

    if (empresa):
        return empresa
    else:
        return None

def es_Tutor_Industrial(correo):
    tutor_Industrial = db(db.Tutor_Industrial,db.Tutor_Industrial.usuario == db.UsuarioExterno.id)(db.UsuarioExterno.correo == correo).select()

    if (tutor_Industrial):
        return tutor_Industrial
    else:
        return None