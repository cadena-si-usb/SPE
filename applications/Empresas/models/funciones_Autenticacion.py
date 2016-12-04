# Funciones disponibles en todo el codigo.

def es_Empresa(email):
    empresa = db((db.auth_user.email == email) & (db.Empresa.usuario == db.auth_user.id)).select().first()

    if (empresa):
        return empresa
    else:
        return None

def es_Tutor_Industrial(email):
    tutor_Industrial = db((db.auth_user.email == email) & (db.Tutor_Industrial.usuario == db.auth_user.id)).select().first()

    if (tutor_Industrial):
        return tutor_Industrial
    else:
        return None