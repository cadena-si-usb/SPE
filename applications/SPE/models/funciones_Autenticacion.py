# Funciones disponibles en todo el codigo.

def es_Estudiante(username):
    estudiante = db(db.Estudiante,db.Estudiante.usuario == db.auth_user.id)(db.auth_user.username == username).select()

    if (estudiante):
        return estudiante
    else:
        return None

def es_Profesor(username):
    profesor = db(db.Profesor,db.Profesor.usuario == db.auth_user.id)(db.auth_user.username == username).select()

    if (profesor):
        return profesor
    else:
        return None