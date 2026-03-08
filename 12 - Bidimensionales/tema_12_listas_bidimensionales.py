# ============================================================
#  TEMA 12 -- LISTAS BIDIMENSIONALES Y BUCLES ANIDADOS
# ============================================================

# ------------------------------------------------------------
# 1. QUE ES UNA LISTA BIDIMENSIONAL
# ------------------------------------------------------------

# Una lista normal es una fila de datos (1 dimension)
fila = [10, 20, 30, 40]

# Una lista bidimensional es una lista de listas (2 dimensiones)
# Piensala como una tabla con FILAS y COLUMNAS, como Excel

matriz = [
    [1, 2, 3],    # fila 0
    [4, 5, 6],    # fila 1
    [7, 8, 9]     # fila 2
]
#          col0 col1 col2

# Visualizacion mental:
#         col0  col1  col2
# fila0:    1     2     3
# fila1:    4     5     6
# fila2:    7     8     9

# ------------------------------------------------------------
# 2. ACCEDER A ELEMENTOS
# ------------------------------------------------------------

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Sintaxis: matriz[fila][columna]
print(matriz[0][0])    # 1   --> fila 0, columna 0  (esquina superior izquierda)
print(matriz[0][2])    # 3   --> fila 0, columna 2
print(matriz[1][1])    # 5   --> fila 1, columna 1  (centro)
print(matriz[2][2])    # 9   --> fila 2, columna 2  (esquina inferior derecha)
print(matriz[-1][-1])  # 9   --> ultima fila, ultima columna

# Acceder a una fila completa
print(matriz[0])       # [1, 2, 3]  --> toda la fila 0
print(matriz[1])       # [4, 5, 6]  --> toda la fila 1

# Modificar un elemento
matriz[1][1] = 99
print(matriz[1])       # [4, 99, 6]

# ------------------------------------------------------------
# 3. RECORRER CON BUCLES ANIDADOS
# ------------------------------------------------------------

# REGLA CLAVE:
#   -- bucle EXTERIOR --> recorre filas
#   -- bucle INTERIOR --> recorre columnas de esa fila

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Forma 1 -- solo valores (cuando no necesitas la posicion)
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()    # salto de linea al terminar cada fila
# 1 2 3
# 4 5 6
# 7 8 9

# Forma 2 -- con indices (cuando necesitas saber en que posicion estas)
for i in range(len(matriz)):           # i recorre 0, 1, 2 (filas)
    for j in range(len(matriz[i])):    # j recorre 0, 1, 2 (columnas)
        print(f"[{i}][{j}] = {matriz[i][j]}")
# [0][0] = 1   [0][1] = 2   [0][2] = 3
# [1][0] = 4   [1][1] = 5   ...

# ------------------------------------------------------------
# 4. DIMENSIONES DE UNA MATRIZ
# ------------------------------------------------------------

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

num_filas    = len(matriz)        # 3  --> cuantas filas hay
num_columnas = len(matriz[0])     # 3  --> cuantas columnas tiene la primera fila

print(f"Dimensiones: {num_filas} x {num_columnas}")   # 3 x 3

# Matriz no cuadrada (mas filas que columnas)
tabla = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
]

print(len(tabla))      # 3  --> filas
print(len(tabla[0]))   # 4  --> columnas

# ------------------------------------------------------------
# 5. CREAR MATRICES CON BUCLES
# ------------------------------------------------------------

# Crear matriz de ceros (forma correcta)
filas    = 3
columnas = 4

ceros = []
for i in range(filas):
    fila_nueva = []
    for j in range(columnas):
        fila_nueva.append(0)
    ceros.append(fila_nueva)

print(ceros)
# [[0, 0, 0, 0],
#  [0, 0, 0, 0],
#  [0, 0, 0, 0]]

# TRAMPA COMUN -- no hagas esto para crear matrices
# mal = [[0] * 3] * 3    --> las 3 filas son EL MISMO objeto en memoria
# Si modificas una fila, se modifican todas

# Demostracion del error:
mal = [[0] * 3] * 3
mal[0][0] = 99
print(mal)    # [[99, 0, 0], [99, 0, 0], [99, 0, 0]] --> cambio las 3 filas

# Forma correcta -- cada fila es independiente:
bien = []
for i in range(3):
    bien.append([0, 0, 0])    # cada vez crea una lista NUEVA
bien[0][0] = 99
print(bien)   # [[99, 0, 0], [0, 0, 0], [0, 0, 0]] --> solo cambio la fila 0

# Crear matriz con valores incrementales
matriz_num = []
for i in range(filas):
    fila_nueva = []
    for j in range(columnas):
        fila_nueva.append(i * columnas + j)
    matriz_num.append(fila_nueva)
print(matriz_num)
# [[0, 1, 2, 3],
#  [4, 5, 6, 7],
#  [8, 9, 10, 11]]

# ------------------------------------------------------------
# 6. OPERACIONES TIPICAS DE EXAMEN
# ------------------------------------------------------------

notas = [
    [7.8, 9.2, 5.0],    # notas del alumno 0
    [4.5, 6.0, 8.1],    # notas del alumno 1
    [3.0, 7.5, 9.8]     # notas del alumno 2
]

# Suma de todos los elementos
total = 0
for fila in notas:
    for nota in fila:
        total += nota
print(f"Suma total: {total:.1f}")    # 60.9

# Maximo y minimo de toda la matriz
maximo = notas[0][0]    # empezamos asumiendo que el primero es el mayor
minimo = notas[0][0]
for fila in notas:
    for nota in fila:
        if nota > maximo:
            maximo = nota
        if nota < minimo:
            minimo = nota
print(f"Maximo: {maximo}  Minimo: {minimo}")   # 9.8 / 3.0

# Media por fila (media de cada alumno)
for i in range(len(notas)):
    suma = 0
    for nota in notas[i]:
        suma += nota
    media = suma / len(notas[i])
    print(f"Alumno {i}: media = {media:.2f}")
# Alumno 0: media = 7.33
# Alumno 1: media = 6.20
# Alumno 2: media = 6.77

# Media por columna (media de cada examen)
num_filas    = len(notas)
num_columnas = len(notas[0])

for j in range(num_columnas):
    suma_col = 0
    for i in range(num_filas):
        suma_col += notas[i][j]    # recorremos la misma columna j en cada fila
    media_col = suma_col / num_filas
    print(f"Examen {j}: media = {media_col:.2f}")
# Examen 0: media = 5.10
# Examen 1: media = 7.57
# Examen 2: media = 7.63

# Contar cuantos aprobados hay en toda la matriz
aprobados = 0
for fila in notas:
    for nota in fila:
        if nota >= 5:
            aprobados += 1
print(f"Aprobados: {aprobados}")   # 7

# Buscar un valor y devolver su posicion (fila, columna)
def buscar_en_matriz(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return (i, j)    # devuelve (fila, columna)
    return None

pos = buscar_en_matriz(notas, 9.8)
print(f"Nota 9.8 en posicion: {pos}")    # (2, 2)

# ------------------------------------------------------------
# 7. MATRIZ TRANSPUESTA
# ------------------------------------------------------------

# Transponer = convertir filas en columnas y viceversa
# Original 3x2     Transpuesta 2x3
# [1, 2]           [1, 3, 5]
# [3, 4]    --->   [2, 4, 6]
# [5, 6]

original = [
    [1, 2],
    [3, 4],
    [5, 6]
]

filas_orig = len(original)       # 3
cols_orig  = len(original[0])    # 2

# Crear matriz vacia con las dimensiones invertidas
transpuesta = []
for j in range(cols_orig):
    fila_nueva = []
    for i in range(filas_orig):
        fila_nueva.append(0)
    transpuesta.append(fila_nueva)

# Rellenar copiando con filas y columnas intercambiadas
for i in range(filas_orig):
    for j in range(cols_orig):
        transpuesta[j][i] = original[i][j]   # el truco: intercambiamos i y j

print(transpuesta)    # [[1, 3, 5], [2, 4, 6]]

# ------------------------------------------------------------
# 8. CASOS PRACTICOS
# ------------------------------------------------------------

# TABLERO DE AJEDREZ
def crear_tablero(n):
    tablero = []
    for i in range(n):
        fila = []
        for j in range(n):
            if (i + j) % 2 == 0:
                fila.append("#")
            else:
                fila.append(".")
        tablero.append(fila)
    return tablero

tablero = crear_tablero(4)
for fila in tablero:
    print(" ".join(fila))
# # . # .
# . # . #
# # . # .
# . # . #

# MAPA DE UN JUEGO
mapa = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", ".", "P", ".", "#"],    # P = jugador
    ["#", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#"]
]

for fila in mapa:
    print("".join(fila))

# Encontrar la posicion del jugador
def encontrar_jugador(mapa, simbolo="P"):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == simbolo:
                return (i, j)
    return None

print(encontrar_jugador(mapa))    # (2, 2)

# NOTAS DE CLASE -- ejemplo completo tipo examen
alumnos     = ["Lucas", "Ana", "Pedro"]
asignaturas = ["Mates", "Lengua", "Python"]

notas = [
    [8.0, 7.5, 9.2],    # Lucas
    [5.5, 9.0, 7.8],    # Ana
    [4.0, 6.5, 5.0]     # Pedro
]

print("\nINFORME DE NOTAS")
print("Alumno     Mates   Lengua   Python    Media")
print("-" * 46)

for i in range(len(alumnos)):
    suma = 0
    for nota in notas[i]:
        suma += nota
    media = suma / len(notas[i])

    print(f"{alumnos[i]:<10}", end="")
    for nota in notas[i]:
        print(f"{nota:>8.1f}", end="")
    print(f"{media:>8.2f}")

# ------------------------------------------------------------
# 9. OBTENER COLUMNA Y DIAGONAL
# ------------------------------------------------------------

matriz = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]

# Obtener una columna completa (columna 1)
columna_1 = []
for fila in matriz:
    columna_1.append(fila[1])
print(columna_1)    # [2, 6, 10, 14]

# Obtener la diagonal principal (donde fila == columna)
diagonal = []
for i in range(len(matriz)):
    diagonal.append(matriz[i][i])
print(diagonal)     # [1, 6, 11, 16]

# Obtener la diagonal secundaria
n = len(matriz)
diagonal_sec = []
for i in range(n):
    diagonal_sec.append(matriz[i][n - 1 - i])
print(diagonal_sec)  # [4, 7, 10, 13]

# ============================================================
#  HOJA DE TRUCOS -- TEMA 12
# ============================================================
"""
CREAR
    matriz = [[1, 2], [3, 4]]           # manual

    # con bucles (forma segura)
    m = []
    for i in range(filas):
        fila = []
        for j in range(cols):
            fila.append(0)
        m.append(fila)

    TRAMPA: [[0]*cols]*filas --> todas las filas son el mismo objeto, NO USAR

ACCEDER
    matriz[fila][columna]
    matriz[0]              --> fila completa
    matriz[-1][-1]         --> ultimo elemento
    len(matriz)            --> numero de filas
    len(matriz[0])         --> numero de columnas

RECORRER (2 formas principales)
    for fila in matriz:                    --> solo valores
        for elemento in fila:

    for i in range(len(matriz)):           --> con indices (cuando necesitas posicion)
        for j in range(len(matriz[i])):
            print(matriz[i][j])

MEDIA POR FILA
    for i in range(len(notas)):
        suma = 0
        for nota in notas[i]:
            suma += nota
        media = suma / len(notas[i])

MEDIA POR COLUMNA
    for j in range(num_columnas):
        suma = 0
        for i in range(num_filas):
            suma += matriz[i][j]      --> misma columna j en cada fila

COLUMNA
    col = []
    for fila in matriz:
        col.append(fila[j])

DIAGONAL PRINCIPAL
    for i in range(len(m)):
        diagonal.append(m[i][i])     --> fila == columna

TRANSPONER
    transpuesta[j][i] = original[i][j]   --> intercambiar i y j
"""
