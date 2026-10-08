# Ejercicio 1: contar_palabras(texto)
# Devuelve cuántas palabras tiene un texto y cuál es la más larga.
#
# Pistas:
# - Los str tienen un método que trocea por espacios y te da una lista.
#   Pruébalo sin argumentos: así también trata bien varios espacios seguidos
#   y los saltos de línea.
# - len() funciona con listas igual que .length en JS.
# - Para la más larga puedes hacer un bucle for guardando la mejor hasta ahora,
#   o mirar qué hace el parámetro `key` de la función max().
# - Una función de Python puede devolver dos valores a la vez:
#   `return a, b` devuelve una tupla, y luego se desempaqueta con `x, y = funcion()`.
# - ¿Qué debería pasar con un texto vacío ""? Pruébalo.

def contar_palabras(texto):
    palabras_sueltas = texto.split()
    if not palabras_sueltas:
        num_palabras = 0
        palabra_larga = "ninguna, no hay palabras"
    else:
        num_palabras = len(palabras_sueltas)
        palabra_larga = palabras_sueltas[0]
        for palabra in palabras_sueltas:
            if len(palabra) > len(palabra_larga):
                palabra_larga = palabra

    return num_palabras, palabra_larga


pruebas = [
    "Hace mucho tiempo que te quiero ver",
    "",
    "Hace mucho tiempo que te quiero ver" * 17,
]

for prueba in pruebas:
    num_palabras, palabra_larga = contar_palabras(prueba)
    print("Hay", num_palabras, "palabra(s) en el texto.")
    print("La palabra más larga del texto es:", palabra_larga)
