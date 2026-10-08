# Ejercicio 4: clasificar_codigo(status)
# Recibe un código HTTP y devuelve "éxito", "redirección", "error cliente" o "error servidor".
# Hazlo dos veces: una con if/elif y otra con match.
#
# Pista (solo para la versión con match):
# - match no es el switch de JS: no hay fallthrough ni break.
#   Para rangos, un case puede llevar una condición: `case x if ...:`.

def clasificar_codigo(status):
    if 200 <= status < 300:
        texto = "éxito"
    elif 300 <= status < 400:
        texto = "redirección"
    elif 400 <= status < 500:
        texto = "error cliente"
    elif 500 <= status < 600:
        texto = "error servidor"
    else:
        texto = "error desconocido"

    return texto


def clasificar_codigo2(status):
    match status:
        case _ if 200 <= status < 300:
            texto = "éxito"
        case _ if 300 <= status < 400:
            texto = "redirección"
        case _ if 400 <= status < 500:
            texto = "error cliente"
        case _ if 500 <= status < 600:
            texto = "error servidor"
        case _:
            texto = "error desconocido"

    return texto


for status in [99, 201, 302, 404, 503]:
    print(status, "->", clasificar_codigo(status), "|", clasificar_codigo2(status))
