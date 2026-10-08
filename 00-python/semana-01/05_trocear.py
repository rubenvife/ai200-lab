# Ejercicio 5: trocear(texto, tamano=100, solape=20)
# Devuelve una lista de fragmentos de `tamano` caracteres, donde cada uno empieza
# `solape` caracteres antes de que acabe el anterior.
# Pruébalo con un texto de 250 caracteres y comprueba a mano que los cortes cuadran.
#
# Pistas:
# - Antes de programar, haz la cuenta en papel: si un fragmento empieza en 0
#   y mide 100, ¿dónde empieza el siguiente si se solapan 20? ¿Y el tercero?
#   La distancia entre un inicio y el siguiente es siempre la misma.
# - range() acepta un tercer argumento, el paso: range(inicio, fin, paso).
# - El slicing texto[a:b] no falla si b se pasa del final: corta donde acaba el texto.
# - Con 250 caracteres, mira bien el último fragmento: ¿aporta algo nuevo
#   o ya estaba entero dentro del anterior? Decide qué quieres que pase.
# - ¿Qué pasa si solape >= tamano? Piensa qué debería hacer la función
#   (pista: puedes lanzar un ValueError).
# - Para generar un texto de prueba de 250 caracteres reconocibles, puedes
#   multiplicar un str: "0123456789" * 25.

def trocear(texto, tamano=100, solape=20):
    if solape >= tamano:
        raise ValueError("solape tiene que ser menor que tamano")

    inicios = range(0, len(texto), tamano - solape)
    fragmentos = []
    for inicio in inicios:
        fin = inicio + tamano
        fragmentos.append(texto[inicio:fin])
        if fin >= len(texto):
            break
    return fragmentos


texto_prueba = "0123456789" * 25
tamano = 100
solape = 20
fragmentos = trocear(texto_prueba, tamano, solape)

print("Hay", len(fragmentos), "fragmentos.")
for i, fragmentito in enumerate(fragmentos):
    inicio = i * (tamano - solape)
    fin = inicio + len(fragmentito)
    print("Fragmento", i, "-> del", inicio, "al", fin, "| tamaño:", len(fragmentito))

print("Solape correcto:", fragmentos[0][-solape:] == fragmentos[1][:solape])

for prueba in ["", "a" * 50, "a" * 100]:
    print(len(prueba), "caracteres ->", len(trocear(prueba)), "fragmento(s)")
