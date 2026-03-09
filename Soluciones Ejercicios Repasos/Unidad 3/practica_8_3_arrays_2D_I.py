# ============================================================
#  PRACTICA 8.3 -- EJERCICIOS CON ARRAYS BIDIMENSIONALES I
#  En Python los arrays 2D son listas de listas.
# ============================================================

import random


# ------------------------------------------------------------
# EJERCICIO 1
# a) Crear una matriz de 10x10 llamada 'tabla'.
# b) Filas pares se rellenan con 1, filas impares con 0.
#    (Recordar: fila 0 es par, fila 1 es impar, etc.)
# c) Mostrar su contenido en pantalla.
# ------------------------------------------------------------
print("=" * 50)
print("EJERCICIO 1 -- Matriz 10x10 pares=1 impares=0")
print("=" * 50)

# a) Crear la matriz vacia 10x10
tabla = []
fila  = 0
while fila < 10:
    fila_nueva = []
    columna    = 0
    while columna < 10:
        fila_nueva.append(0)    # valor inicial, se sobreescribe abajo
        columna = columna + 1
    tabla.append(fila_nueva)
    fila = fila + 1

# b) Rellenar segun si la fila es par o impar
fila = 0
while fila < 10:
    columna = 0
    while columna < 10:
        if fila % 2 == 0:
            tabla[fila][columna] = 1    # fila par --> 1
        else:
            tabla[fila][columna] = 0    # fila impar --> 0
        columna = columna + 1
    fila = fila + 1

# c) Mostrar en pantalla
print("\nContenido de la tabla (10x10):")
fila = 0
while fila < 10:
    linea   = ""
    columna = 0
    while columna < 10:
        linea   = linea + str(tabla[fila][columna]) + " "
        columna = columna + 1
    print(linea)
    fila = fila + 1


# ------------------------------------------------------------
# EJERCICIO 2
# a) Crear una tabla de 5x5 llamada 'diagonal'.
# b) Los elementos de la diagonal principal valen 1, el resto 0.
#    (La diagonal principal es donde fila == columna)
# c) Mostrar en pantalla.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 2 -- Matriz identidad 5x5")
print("=" * 50)

# a) Crear la matriz vacia 5x5
diagonal = []
fila      = 0
while fila < 5:
    fila_nueva = []
    columna    = 0
    while columna < 5:
        fila_nueva.append(0)
        columna = columna + 1
    diagonal.append(fila_nueva)
    fila = fila + 1

# b) Rellenar: 1 en la diagonal, 0 en el resto
fila = 0
while fila < 5:
    columna = 0
    while columna < 5:
        if fila == columna:
            diagonal[fila][columna] = 1    # diagonal principal
        else:
            diagonal[fila][columna] = 0
        columna = columna + 1
    fila = fila + 1

# c) Mostrar
print("\nMatriz diagonal (5x5):")
fila = 0
while fila < 5:
    linea   = ""
    columna = 0
    while columna < 5:
        linea   = linea + str(diagonal[fila][columna]) + " "
        columna = columna + 1
    print(linea)
    fila = fila + 1


# ------------------------------------------------------------
# EJERCICIO 3
# Visualizar la matriz transpuesta de la del ejercicio 2.
# Si la matriz es cuadrada, mostrar tambien la diagonal principal.
#
# Transponer: intercambiar filas por columnas.
# El elemento [i][j] de la original pasa a [j][i] en la transpuesta.
#
# Ejemplo del enunciado (matriz no cuadrada 3x5):
#  3  2  5  0  9
#  9 10  2  3  1
# -3  2  3 43  1
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 3 -- Matriz transpuesta")
print("=" * 50)

# Usamos la matriz del ejercicio 2 (5x5 cuadrada)
original = diagonal

filas_orig = len(original)
cols_orig  = len(original[0])

# Crear la transpuesta con dimensiones invertidas (cols x filas)
transpuesta = []
j = 0
while j < cols_orig:
    fila_nueva = []
    i = 0
    while i < filas_orig:
        fila_nueva.append(0)
        i = i + 1
    transpuesta.append(fila_nueva)
    j = j + 1

# Rellenar la transpuesta: transpuesta[j][i] = original[i][j]
i = 0
while i < filas_orig:
    j = 0
    while j < cols_orig:
        transpuesta[j][i] = original[i][j]
        j = j + 1
    i = i + 1

print("\nMatriz original:")
i = 0
while i < filas_orig:
    linea = ""
    j     = 0
    while j < cols_orig:
        linea = linea + str(original[i][j]) + " "
        j     = j + 1
    print(linea)
    i = i + 1

print("\nMatriz transpuesta:")
i = 0
while i < len(transpuesta):
    linea = ""
    j     = 0
    while j < len(transpuesta[i]):
        linea = linea + str(transpuesta[i][j]) + " "
        j     = j + 1
    print(linea)
    i = i + 1

# Si es cuadrada, mostrar la diagonal principal
if filas_orig == cols_orig:
    print("\nDiagonal principal de la original:")
    diagonal_valores = []
    i = 0
    while i < filas_orig:
        diagonal_valores.append(original[i][i])
        i = i + 1
    print(diagonal_valores)


# ------------------------------------------------------------
# EJERCICIO 4
# Capturar una matriz de 4x4 por teclado.
# Comprobar si es una matriz identidad:
#   - La diagonal principal tiene 1
#   - El resto de posiciones tiene 0
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 4 -- Comprobar si es matriz identidad 4x4")
print("=" * 50)

# Capturar la matriz 4x4
matriz = []
print("Introduce los valores de la matriz 4x4:")
i = 0
while i < 4:
    fila_nueva = []
    j          = 0
    while j < 4:
        valor = int(input(f"  Elemento [{i}][{j}]: "))
        fila_nueva.append(valor)
        j = j + 1
    matriz.append(fila_nueva)
    i = i + 1

# Comprobar si es identidad
es_identidad = True
i            = 0
while i < 4:
    j = 0
    while j < 4:
        if i == j:
            if matriz[i][j] != 1:
                es_identidad = False
        else:
            if matriz[i][j] != 0:
                es_identidad = False
        j = j + 1
    i = i + 1

if es_identidad:
    print("La matriz ES una matriz identidad")
else:
    print("La matriz NO es una matriz identidad")


# ------------------------------------------------------------
# EJERCICIO 5
# a) Crear una tabla 5x5 llamada 'matriz'.
# b) Cargar con valores enteros.
# c) Sumar todos los elementos de cada fila y cada columna.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 5 -- Suma de filas y columnas (5x5)")
print("=" * 50)

# b) Cargar la tabla con valores por teclado
matriz = []
print("Introduce los valores de la matriz 5x5:")
i = 0
while i < 5:
    fila_nueva = []
    j          = 0
    while j < 5:
        valor = int(input(f"  [{i}][{j}]: "))
        fila_nueva.append(valor)
        j = j + 1
    matriz.append(fila_nueva)
    i = i + 1

# c) Mostrar la matriz
print("\nMatriz introducida:")
i = 0
while i < 5:
    linea = ""
    j     = 0
    while j < 5:
        linea = linea + f"{matriz[i][j]:5d}"
        j     = j + 1
    print(linea)
    i = i + 1

# Suma de cada fila
print("\nSuma por filas:")
i = 0
while i < 5:
    suma_fila = 0
    j         = 0
    while j < 5:
        suma_fila = suma_fila + matriz[i][j]
        j         = j + 1
    print(f"  Fila {i}: {suma_fila}")
    i = i + 1

# Suma de cada columna
print("\nSuma por columnas:")
j = 0
while j < 5:
    suma_col = 0
    i        = 0
    while i < 5:
        suma_col = suma_col + matriz[i][j]
        i        = i + 1
    print(f"  Columna {j}: {suma_col}")
    j = j + 1


# ------------------------------------------------------------
# EJERCICIO 6
# Cargar notas de 3 asignaturas para 15 alumnos.
# Cada FILA = una asignatura, cada COLUMNA = un alumno.
# Calcular:
#   - Nota media de cada alumno   (media de su columna)
#   - Nota media de cada asignatura (media de su fila)
#   - Nota media de la clase
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 6 -- Notas 3 asignaturas x 15 alumnos")
print("=" * 50)

NUM_ASIG   = 3
NUM_ALUMNOS = 15

# Cargar la tabla de notas (3 filas x 15 columnas)
notas = []
print(f"Introduce las notas ({NUM_ASIG} asignaturas x {NUM_ALUMNOS} alumnos):")
i = 0
while i < NUM_ASIG:
    fila_nueva = []
    print(f"\n  -- Asignatura {i + 1} --")
    j = 0
    while j < NUM_ALUMNOS:
        nota = float(input(f"    Alumno {j + 1}: "))
        fila_nueva.append(nota)
        j = j + 1
    notas.append(fila_nueva)
    i = i + 1

# Media de cada alumno (recorrer columna por columna)
print("\nNota media de cada alumno:")
suma_total_clase = 0.0
j = 0
while j < NUM_ALUMNOS:
    suma_alumno = 0.0
    i           = 0
    while i < NUM_ASIG:
        suma_alumno = suma_alumno + notas[i][j]
        i           = i + 1
    media_alumno     = suma_alumno / NUM_ASIG
    suma_total_clase = suma_total_clase + suma_alumno
    print(f"  Alumno {j + 1:2d}: {media_alumno:.2f}")
    j = j + 1

# Media de cada asignatura (recorrer fila por fila)
print("\nNota media de cada asignatura:")
i = 0
while i < NUM_ASIG:
    suma_asig = 0.0
    j         = 0
    while j < NUM_ALUMNOS:
        suma_asig = suma_asig + notas[i][j]
        j         = j + 1
    media_asig = suma_asig / NUM_ALUMNOS
    print(f"  Asignatura {i + 1}: {media_asig:.2f}")
    i = i + 1

# Media global de la clase
media_clase = suma_total_clase / (NUM_ASIG * NUM_ALUMNOS)
print(f"\nNota media de la clase: {media_clase:.2f}")


# ------------------------------------------------------------
# EJERCICIO 7
# a) Llenar array con notas de 3 clases x 30 alumnos.
# b) Visualizar el array.
# c) Calcular la nota maxima y minima con alumno y grupo.
#    Si se repiten, mostrar todas las ocurrencias.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 7 -- Notas 3 clases x 30 alumnos")
print("=" * 50)

NUM_CLASES  = 3
MAX_ALUMNOS = 30

# Para el ejemplo usamos notas aleatorias
# (En un programa real se pediriian por teclado)
print("Generando notas aleatorias para el ejemplo...")
notas_clases = []
i = 0
while i < NUM_CLASES:
    fila_nueva = []
    j          = 0
    while j < MAX_ALUMNOS:
        nota = random.randint(0, 10)
        fila_nueva.append(nota)
        j = j + 1
    notas_clases.append(fila_nueva)
    i = i + 1

# b) Mostrar el array
print("\nNotas por clase:")
i = 0
while i < NUM_CLASES:
    print(f"  Clase {i + 1}: {notas_clases[i]}")
    i = i + 1

# c) Buscar el maximo y minimo de toda la tabla
maximo = notas_clases[0][0]
minimo = notas_clases[0][0]

i = 0
while i < NUM_CLASES:
    j = 0
    while j < MAX_ALUMNOS:
        if notas_clases[i][j] > maximo:
            maximo = notas_clases[i][j]
        if notas_clases[i][j] < minimo:
            minimo = notas_clases[i][j]
        j = j + 1
    i = i + 1

# Mostrar todas las ocurrencias del maximo
print(f"\nNota MAXIMA: {maximo}")
i = 0
while i < NUM_CLASES:
    j = 0
    while j < MAX_ALUMNOS:
        if notas_clases[i][j] == maximo:
            print(f"  --> Clase {i + 1}, Alumno {j + 1}")
        j = j + 1
    i = i + 1

# Mostrar todas las ocurrencias del minimo
print(f"\nNota MINIMA: {minimo}")
i = 0
while i < NUM_CLASES:
    j = 0
    while j < MAX_ALUMNOS:
        if notas_clases[i][j] == minimo:
            print(f"  --> Clase {i + 1}, Alumno {j + 1}")
        j = j + 1
    i = i + 1


# ------------------------------------------------------------
# EJERCICIO 8
# Dado un array bidimensional de 10x15, obtener un vector
# unidimensional donde cada elemento es la suma de una fila.
# (vector[0] = suma fila 0, vector[1] = suma fila 1, ...)
#
# Ejemplo del enunciado (matriz de 5x3 mostrada en el PDF):
#  3  9 -3
#  2 10  2
#  5  2  3
#  0  3 43
#  9  1  1
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 8 -- Sumas de filas en vector unidimensional")
print("=" * 50)

# Usamos el ejemplo del enunciado (5x3)
matriz_ej = [
    [ 3,  9, -3],
    [ 2, 10,  2],
    [ 5,  2,  3],
    [ 0,  3, 43],
    [ 9,  1,  1]
]

print("Matriz original:")
i = 0
while i < len(matriz_ej):
    linea = ""
    j     = 0
    while j < len(matriz_ej[i]):
        linea = linea + f"{matriz_ej[i][j]:5d}"
        j     = j + 1
    print(linea)
    i = i + 1

# Calcular el vector de sumas
vector_sumas = []
i = 0
while i < len(matriz_ej):
    suma_fila = 0
    j         = 0
    while j < len(matriz_ej[i]):
        suma_fila = suma_fila + matriz_ej[i][j]
        j         = j + 1
    vector_sumas.append(suma_fila)
    i = i + 1

print(f"\nVector de sumas por fila: {vector_sumas}")
# Salida esperada: [9, 14, 10, 46, 11]


# ------------------------------------------------------------
# EJERCICIO 9
# Crear una tabla 20x2 con las potencias de 2.
# Columna 0 = exponente (puede ser negativo), columna 1 = valor.
# El usuario introduce exponentes hasta que teclea -1000.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 9 -- Tabla de potencias de 2 (20 filas)")
print("=" * 50)

# Crear la tabla 20x2
# Los exponentes van de -10 a 9 (20 valores)
tabla_potencias = []
exp = -10
while exp <= 9:
    if exp >= 0:
        valor = 1
        i     = 0
        while i < exp:
            valor = valor * 2
            i     = i + 1
    else:
        # Para exponentes negativos: 2^(-n) = 1 / 2^n
        exp_pos = exp * -1
        valor   = 1.0
        i       = 0
        while i < exp_pos:
            valor = valor * 2
            i     = i + 1
        valor = 1.0 / valor

    tabla_potencias.append([exp, valor])
    exp = exp + 1

print("Tabla generada:")
print(f"{'Exponente':>12}  {'Valor':>15}")
print("-" * 30)
i = 0
while i < len(tabla_potencias):
    print(f"{tabla_potencias[i][0]:>12}  {tabla_potencias[i][1]:>15.6f}")
    i = i + 1

# El usuario consulta potencias hasta introducir -1000
print("\nConsulta de potencias (introduce -1000 para salir):")
while True:
    expo_consulta = int(input("Introduce el exponente que quieres consultar: "))

    if expo_consulta == -1000:
        break

    # Buscar en la tabla
    encontrado = False
    i          = 0
    while i < len(tabla_potencias):
        if tabla_potencias[i][0] == expo_consulta:
            print(f"  2 elevado a {expo_consulta} = {tabla_potencias[i][1]}")
            encontrado = True
            break
        i = i + 1

    if not encontrado:
        print(f"  El exponente {expo_consulta} no esta en la tabla (rango: -10 a 9)")
