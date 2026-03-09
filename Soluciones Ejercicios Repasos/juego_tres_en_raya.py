# ============================================================
#  JUEGO -- TRES EN RAYA
#  2 jugadores: X y O
#  El tablero es una lista de listas 3x3
# ============================================================

import random


# ------------------------------------------------------------
# FUNCIONES DEL JUEGO
# ------------------------------------------------------------

def crear_tablero():
    """Crea el tablero vacio 3x3 con numeros del 1 al 9
    para que el jugador sepa donde colocar su ficha."""
    tablero = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    return tablero


def mostrar_tablero(tablero):
    """Muestra el tablero en pantalla con formato visual."""
    print()
    print("  +-----------+")
    fila = 0
    while fila < 3:
        linea = "  |"
        columna = 0
        while columna < 3:
            celda = tablero[fila][columna]
            if celda == "X":
                linea = linea + " X |"
            elif celda == "O":
                linea = linea + " O |"
            else:
                linea = linea + " " + celda + " |"
            columna = columna + 1
        print(linea)
        if fila < 2:
            print("  +-----------+")
        fila = fila + 1
    print("  +-----------+")
    print()


def posicion_a_fila_columna(posicion):
    """Convierte una posicion del 1 al 9 en fila y columna.
    Ejemplo: posicion 5 --> fila 1, columna 1 (centro)"""
    posicion  = posicion - 1        # pasamos a rango 0-8
    fila      = posicion // 3       # division entera entre 3
    columna   = posicion % 3        # resto de dividir entre 3
    return fila, columna


def casilla_libre(tablero, posicion):
    """Comprueba si la casilla de la posicion dada esta libre.
    Devuelve True si esta libre, False si ya tiene X o O."""
    fila, columna = posicion_a_fila_columna(posicion)
    celda         = tablero[fila][columna]
    # La celda esta libre si tiene el numero (no X ni O)
    if celda == "X" or celda == "O":
        return False
    return True


def colocar_ficha(tablero, posicion, ficha):
    """Coloca la ficha (X u O) en la posicion indicada."""
    fila, columna             = posicion_a_fila_columna(posicion)
    tablero[fila][columna]    = ficha


def comprobar_ganador(tablero, ficha):
    """Comprueba si la ficha dada ha ganado el juego.
    Revisa filas, columnas y las dos diagonales.
    Devuelve True si ha ganado, False si no."""

    # Comprobar filas
    fila = 0
    while fila < 3:
        if (tablero[fila][0] == ficha and
            tablero[fila][1] == ficha and
            tablero[fila][2] == ficha):
            return True
        fila = fila + 1

    # Comprobar columnas
    columna = 0
    while columna < 3:
        if (tablero[0][columna] == ficha and
            tablero[1][columna] == ficha and
            tablero[2][columna] == ficha):
            return True
        columna = columna + 1

    # Comprobar diagonal principal (arriba-izquierda a abajo-derecha)
    if (tablero[0][0] == ficha and
        tablero[1][1] == ficha and
        tablero[2][2] == ficha):
        return True

    # Comprobar diagonal secundaria (arriba-derecha a abajo-izquierda)
    if (tablero[0][2] == ficha and
        tablero[1][1] == ficha and
        tablero[2][0] == ficha):
        return True

    return False


def tablero_lleno(tablero):
    """Comprueba si el tablero esta completamente lleno (empate).
    Devuelve True si no quedan casillas libres."""
    fila = 0
    while fila < 3:
        columna = 0
        while columna < 3:
            celda = tablero[fila][columna]
            if celda != "X" and celda != "O":
                return False    # hay al menos una casilla libre
            columna = columna + 1
        fila = fila + 1
    return True


def pedir_jugada(tablero, nombre, ficha):
    """Pide al jugador que introduzca una posicion valida (1-9)."""
    while True:
        entrada = input(f"  {nombre} ({ficha}), elige una casilla (1-9): ")

        # Comprobar que es un numero
        if not entrada.isdigit():
            print("  Error: introduce un numero del 1 al 9.")
            continue

        posicion = int(entrada)

        # Comprobar rango
        if posicion < 1 or posicion > 9:
            print("  Error: el numero debe estar entre 1 y 9.")
            continue

        # Comprobar que esta libre
        if not casilla_libre(tablero, posicion):
            print("  Esa casilla ya esta ocupada. Elige otra.")
            continue

        return posicion


def jugada_maquina(tablero, ficha_maquina, ficha_rival):
    """La maquina elige su jugada con una estrategia basica:
       1. Si puede ganar en este turno, gana.
       2. Si el rival puede ganar el siguiente turno, bloquea.
       3. Si no, elige una casilla libre al azar."""

    # Paso 1: buscar si la maquina puede ganar ahora
    posicion = 1
    while posicion <= 9:
        if casilla_libre(tablero, posicion):
            # Probar colocar la ficha de la maquina
            colocar_ficha(tablero, posicion, ficha_maquina)
            if comprobar_ganador(tablero, ficha_maquina):
                # Deshacer y devolver esa posicion (ganar!)
                fila, columna = posicion_a_fila_columna(posicion)
                tablero[fila][columna] = str(posicion)
                return posicion
            # Deshacer el intento
            fila, columna = posicion_a_fila_columna(posicion)
            tablero[fila][columna] = str(posicion)
        posicion = posicion + 1

    # Paso 2: bloquear al rival si puede ganar
    posicion = 1
    while posicion <= 9:
        if casilla_libre(tablero, posicion):
            # Probar colocar la ficha del rival
            colocar_ficha(tablero, posicion, ficha_rival)
            if comprobar_ganador(tablero, ficha_rival):
                # Deshacer y bloquear esa posicion
                fila, columna = posicion_a_fila_columna(posicion)
                tablero[fila][columna] = str(posicion)
                return posicion
            # Deshacer el intento
            fila, columna = posicion_a_fila_columna(posicion)
            tablero[fila][columna] = str(posicion)
        posicion = posicion + 1

    # Paso 3: elegir el centro si esta libre
    if casilla_libre(tablero, 5):
        return 5

    # Paso 4: elegir una esquina libre
    esquinas = [1, 3, 7, 9]
    i        = 0
    while i < len(esquinas):
        if casilla_libre(tablero, esquinas[i]):
            return esquinas[i]
        i = i + 1

    # Paso 5: elegir cualquier casilla libre
    posicion = 1
    while posicion <= 9:
        if casilla_libre(tablero, posicion):
            return posicion
        posicion = posicion + 1


# ------------------------------------------------------------
# BUCLE PRINCIPAL DEL JUEGO
# ------------------------------------------------------------

print("=" * 40)
print("     TRES EN RAYA")
print("=" * 40)

# Marcador global
victorias_j1  = 0
victorias_j2  = 0
empates       = 0

# Elegir modo de juego
print("\nModos de juego:")
print("  1. Jugador vs Jugador")
print("  2. Jugador vs Maquina")

modo = 0
while modo != 1 and modo != 2:
    entrada = input("Elige el modo (1 o 2): ")
    if entrada.isdigit():
        modo = int(entrada)

# Pedir nombres
nombre_j1 = input("\nNombre del jugador 1 (X): ")
if modo == 1:
    nombre_j2 = input("Nombre del jugador 2 (O): ")
else:
    nombre_j2 = "Maquina"

print(f"\nBienvenidos {nombre_j1} y {nombre_j2}!")
print("Las casillas se numeran del 1 al 9 de izquierda a derecha y de arriba abajo.")

# Bucle de partidas
while True:

    # Nueva partida
    tablero     = crear_tablero()
    turno       = 1           # 1 = jugador 1 (X), 2 = jugador 2 (O)
    partida_activa = True

    print("\n" + "-" * 40)
    print("    NUEVA PARTIDA")
    print(f"  {nombre_j1} (X)  vs  {nombre_j2} (O)")
    print("-" * 40)
    mostrar_tablero(tablero)

    while partida_activa:

        if turno == 1:
            # Turno del jugador 1 (siempre humano)
            posicion = pedir_jugada(tablero, nombre_j1, "X")
            colocar_ficha(tablero, posicion, "X")
            mostrar_tablero(tablero)

            if comprobar_ganador(tablero, "X"):
                print(f"  *** {nombre_j1} gana la partida! ***")
                victorias_j1  = victorias_j1 + 1
                partida_activa = False

            elif tablero_lleno(tablero):
                print("  *** Empate! ***")
                empates       = empates + 1
                partida_activa = False

            else:
                turno = 2

        else:
            # Turno del jugador 2 (humano o maquina)
            if modo == 2:
                print(f"  {nombre_j2} (O) esta pensando...")
                posicion = jugada_maquina(tablero, "O", "X")
                print(f"  {nombre_j2} elige la casilla {posicion}")
                colocar_ficha(tablero, posicion, "O")
                mostrar_tablero(tablero)
            else:
                posicion = pedir_jugada(tablero, nombre_j2, "O")
                colocar_ficha(tablero, posicion, "O")
                mostrar_tablero(tablero)

            if comprobar_ganador(tablero, "O"):
                print(f"  *** {nombre_j2} gana la partida! ***")
                victorias_j2  = victorias_j2 + 1
                partida_activa = False

            elif tablero_lleno(tablero):
                print("  *** Empate! ***")
                empates       = empates + 1
                partida_activa = False

            else:
                turno = 1

    # Mostrar marcador
    print("\n--- MARCADOR ---")
    print(f"  {nombre_j1:15s}: {victorias_j1} victorias")
    print(f"  {nombre_j2:15s}: {victorias_j2} victorias")
    print(f"  {'Empates':15s}: {empates}")

    # Preguntar si jugar de nuevo
    respuesta = input("\nJugar otra partida? (S/N): ")
    if respuesta.upper() != "S":
        break

print("\nGracias por jugar! Hasta la proxima.")
