# Ejercicio 2: es_palindromo(texto)
# Devuelve True si el texto se lee igual al derecho y al revés,
# sin tener en cuenta mayúsculas ni espacios.
#
# Pistas:
# - Primero normaliza el texto: pásalo a minúsculas y quítale los espacios
#   (busca los métodos de str para cada cosa).
# - Invertir un string en Python no necesita split/reverse/join como en JS:
#   investiga el "slicing" con paso negativo, texto[inicio:fin:paso].
# - La comparación ya es un booleano: no hace falta un if para devolver True/False.
# - Casos para probar: "Anita lava la tina", "Ana", "Python".

def es_palindromo(texto):
    normalizado = texto.casefold()
    no_spaces = normalizado.replace(" ", "")
    volteado = no_spaces[::-1]
    return volteado == no_spaces


for prueba in ["Anita lava la tina", "Ana", "Python"]:
    result = "No es"
    if es_palindromo(prueba):
        result = "Es"
    print(prueba, "->", result, "palíndromo")
