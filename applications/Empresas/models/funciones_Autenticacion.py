# Funciones disponibles en todo el codigo.

def es_Empresa(correo):
    empresa = db((db.UsuarioExterno.correo == correo) & (db.Empresa.usuario == db.UsuarioExterno.id)).select().first()

    if (empresa):
        return empresa
    else:
        return None

def es_Tutor_Industrial(correo):
    tutor_Industrial = db((db.UsuarioExterno.correo == correo) & (db.Tutor_Industrial.usuario == db.UsuarioExterno.id)).select().first()

    if (tutor_Industrial):
        return tutor_Industrial
    else:
        return None