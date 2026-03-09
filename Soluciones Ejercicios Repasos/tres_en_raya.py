from utilities import imprimirMatriz

fichas = ["✖","⏺︎"]
def introducirTamano():
    longX = int(input("¿Cuál es la longitud de X del tablero? => "))
    longY = int(input("¿Cuál es la longitud de Y del tablero? => "))
    while longX < 3 or longY <3:
        if longX < 3:
            longX = int(input("Introduce un número de largo mayor o igual a 3 => "))
        if longY < 3:
            longY = int(input("Introduce un número de ancho mayor o igual a 3 => "))
    return longX, longY

def generarTablero(largo, ancho):
    matriz = []
    for i in range(ancho):
        matriz.append([])
        for j in range(largo):
            matriz[i].append(" ")
    return matriz

def pedirPosicion(tablero):
    posicion = (int(input("Posición X: ")), int(input("Posición Y: ")))
    while posicion[0] > len(tablero[0]) or posicion[1] > len(tablero) or posicion[0] < 0 or posicion[1] < 0:
        print(f"No existe esa posición. Repítela: 0-{len(tablero)} | 0-{len(tablero[0])}")
        posicion = (int(input("Posición X: ")), int(input("Posición Y: ")))
    return posicion

def ponerFicha(tablero, ficha):
    posicion = pedirPosicion(tablero)
    while tablero[posicion[0]][posicion[1]] in fichas:
        print("Este espacio está cogido. Introduce otro.")
        posicion = pedirPosicion(tablero)
    tablero[posicion[1]][posicion[0]] = ficha

largo, ancho = introducirTamano()
tablero = generarTablero(largo, ancho)
imprimirMatriz(tablero)

ponerFicha(tablero, "⏺")
ponerFicha(tablero, "⏺")
ponerFicha(tablero, "⏺")
imprimirMatriz(tablero)