# Funciones disponibles en todo el codigo.

def es_Estudiante(usbid):
    estudiante = db(db.Estudiante,db.Estudiante.usuario == db.UsuarioUSB.id)(db.UsuarioUSB.usbid == usbid).select()

    if (estudiante):
        return estudiante
    else:
        return None

def es_Profesor(usbid):
    profesor = db(db.Profesor,db.Profesor.usuario == db.UsuarioUSB.id)(db.UsuarioUSB.usbid == usbid).select()

    if (profesor):
        return profesor
    else:
        return None