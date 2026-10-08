# Ejercicio 3: conversor
# Pide un número con input(), valida que lo sea y repite la pregunta hasta que lo sea.
# (El conversor elige tú qué convierte: km a millas, °C a °F, euros a dólares...)
#
# Pistas:
# - input() siempre devuelve un str, aunque el usuario escriba "42".
# - int() o float() convierten un str a número. Si el texto no es un número,
#   lanzan una excepción: mira cuál es y captúrala con try/except.
#   Es el equivalente a try/catch de JS.
# - Para repetir hasta que salga bien hay un patrón típico:
#   un bucle infinito (while True) y salir de él cuando la conversión funcione.
# - Si metes la lectura en su propia función (que devuelva ya el número),
#   el resto del programa queda más limpio.

def leer_numero(mensaje):
    while True:
        num = input(mensaje)
        try:
            return float(num)
        except ValueError:
            print("No es numero :(")


km = leer_numero("Añade numero para transformar de km a millas: ")
millas = km * 0.621371
print(km, "km son", round(millas, 2), "millas.")
