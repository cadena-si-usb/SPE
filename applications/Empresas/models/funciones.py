# Funciones disponibles en todo el codigo.

def enviar_Correo_Verificacion(email,codigoGenerado):

    if mail:
        mensaje1 = T("Su registro en el SPE ha sido exitoso, pero para poder utilizar" +
        " las funcionalidades del sistema debemos verificar que su la dirección " +
        "de email electrónico suministrada es la correcta\n\n")
        mensaje2 = T("Cuando intente iniciar sesion en el sistema se le solicitara " +
        "el siguiente codigo:\n\n")
        mensaje3 = T('  Codigo De Activación ') + "'" + codigoGenerado + "' \n\n"
        mensaje4 = T("Una vez introducido el codigo su cuenta sera activada y podra " +
        "disfrutar nuestros servicios\n\n")
        mensaje5 = T("Este email se ha enviado de manera automatica por el " +
        "Sistema Empresarial de Pasantias de la Universidad Simón Bolívar.\n\n")
        if mail.send(to=[email],
            subject=T('Activacion'),
            message= (mensaje1 + mensaje2 + mensaje3 + mensaje4 + mensaje5)):
                response.flash = T('email sent sucessfully.')
                resultado = True
        else:
            resultado = False
            response.flash = T('fail to send email sorry!')
    else:
        response.flash = T('Unable to send the email : email parameters not defined')
    return resultado

def generar_Correo_Verificacion(email):
    import string
    import random
    from random import randint

    resultado = False

    size = randint(4,11)
    i = 0
    codigoGenerado = ''

    for i in range(0,size):
                codigoGenerado += random.choice(string.lowercase + string.uppercase + string.digits)

    db.correo_por_verificar.insert(email = email,codigo = codigoGenerado)

    enviar_Correo_Verificacion(email,codigoGenerado)

def reenviar_Correo_Verificacion(email):

    correoVerificarSet = db(db.correo_por_verificar.email == request.vars.email).select()

    codigoGenerado = correoVerificarSet[0].codigo

    enviar_Correo_Verificacion(email,codigoGenerado)

def captcha_field(request=request):
    from gluon.tools import Recaptcha2
    w = lambda x,y: Recaptcha2(request,
                              '6LeFHBwTAAAAAAgmUVpEbEz0NpYaJBIYYw709HIZ',
                              '6LeFHBwTAAAAANvgDFc2Dy257hQ8nux3ZgvdgS8Q')

    return Field('captcha', 'string', widget=w, default='ok')
