# ============================================================
#  PRACTICA 8.4 -- EJERCICIOS CON ARRAYS BIDIMENSIONALES II
# ============================================================

import random


# ------------------------------------------------------------
# EJERCICIO 1
# Dibujar un cuadrado magico de orden impar n (introducido por
# el usuario).
# Un cuadrado magico es aquel donde todos los numeros del 1 al
# n*n aparecen una sola vez y todas las filas, columnas y
# las dos diagonales suman lo mismo.
#
# ALGORITMO DE SIAMESE (para ordenes impares):
#   1. Colocar el 1 en el centro de la primera fila.
#   2. Para cada numero siguiente, mover una casilla arriba y
#      una a la derecha.
#   3. Si la casilla esta ocupada, bajar una fila en vez de
#      subir y no desplazarse a la derecha.
#   4. Los bordes son circulares (si te sales por arriba,
#      entras por abajo; si te sales por la derecha, entras
#      por la izquierda).
# ------------------------------------------------------------
print("=" * 50)
print("EJERCICIO 1 -- Cuadrado magico de orden impar")
print("=" * 50)

n = int(input("Introduce el orden del cuadrado magico (impar): "))

# Validar que sea impar y mayor que 0
while n % 2 == 0 or n <= 0:
    print("Error: el orden debe ser un numero impar positivo.")
    n = int(input("Introduce el orden del cuadrado magico (impar): "))

# Crear la matriz n x n con ceros
cuadrado = []
i = 0
while i < n:
    fila_nueva = []
    j = 0
    while j < n:
        fila_nueva.append(0)
        j = j + 1
    cuadrado.append(fila_nueva)
    i = i + 1

# Algoritmo de Siamese
fila    = 0              # empezamos en la primera fila
columna = n // 2         # centro de la primera fila

numero = 1
while numero <= n * n:
    cuadrado[fila][columna] = numero

    # Calcular la siguiente posicion (arriba-derecha)
    nueva_fila    = (fila - 1) % n      # circular: si sale por arriba entra por abajo
    nueva_columna = (columna + 1) % n   # circular: si sale por derecha entra por izquierda

    if cuadrado[nueva_fila][nueva_columna] != 0:
        # La casilla esta ocupada: bajar una fila en lugar de subir
        nueva_fila    = (fila + 1) % n
        nueva_columna = columna

    fila    = nueva_fila
    columna = nueva_columna
    numero  = numero + 1

# Mostrar el cuadrado
print(f"\nCuadrado magico de orden {n}:")
i = 0
while i < n:
    linea = ""
    j     = 0
    while j < n:
        linea = linea + f"{cuadrado[i][j]:4d}"
        j     = j + 1
    print(linea)
    i = i + 1

# Verificar: mostrar la suma magica esperada
suma_magica = n * (n * n + 1) // 2
print(f"\nSuma magica esperada: {suma_magica}")


# ------------------------------------------------------------
# EJERCICIO 2
# Cargar desde teclado una tabla de enteros de dimension 3x4.
# Mostrar la fila en la que la suma de sus elementos sea mayor.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 2 -- Fila con mayor suma en tabla 3x4")
print("=" * 50)

# Cargar la tabla 3x4
tabla = []
print("Introduce los valores de la tabla 3x4:")
i = 0
while i < 3:
    fila_nueva = []
    j          = 0
    while j < 4:
        valor = int(input(f"  [{i}][{j}]: "))
        fila_nueva.append(valor)
        j = j + 1
    tabla.append(fila_nueva)
    i = i + 1

# Buscar la fila con mayor suma
mayor_suma      = None
fila_mayor_suma = 0

i = 0
while i < 3:
    suma_fila = 0
    j         = 0
    while j < 4:
        suma_fila = suma_fila + tabla[i][j]
        j         = j + 1

    if mayor_suma is None or suma_fila > mayor_suma:
        mayor_suma      = suma_fila
        fila_mayor_suma = i

    i = i + 1

print(f"\nLa fila con mayor suma es la fila {fila_mayor_suma}:")
print(f"  Elementos: {tabla[fila_mayor_suma]}")
print(f"  Suma     : {mayor_suma}")


# ------------------------------------------------------------
# EJERCICIO 3
# Decidir si una matriz cuadrada es magica.
# Si no lo es, listar la suma de cada fila, columna y diagonal.
# Una matriz magica tiene la misma suma en todas sus filas,
# columnas y diagonales.
#
# Ejemplo del enunciado (4x4):
#  16  3  2 13
#   5 10 11  8
#   9  6  7 12
#   4 15 14  1
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 3 -- Comprobar si una matriz es magica")
print("=" * 50)

n = int(input("Introduce el orden de la matriz cuadrada: "))

# Cargar la matriz n x n
matriz = []
print(f"Introduce los valores de la matriz {n}x{n}:")
i = 0
while i < n:
    fila_nueva = []
    j          = 0
    while j < n:
        valor = int(input(f"  [{i}][{j}]: "))
        fila_nueva.append(valor)
        j = j + 1
    matriz.append(fila_nueva)
    i = i + 1

# Calcular todas las sumas
sumas_filas    = []
sumas_columnas = []

# Sumas de filas
i = 0
while i < n:
    suma = 0
    j    = 0
    while j < n:
        suma = suma + matriz[i][j]
        j    = j + 1
    sumas_filas.append(suma)
    i = i + 1

# Sumas de columnas
j = 0
while j < n:
    suma = 0
    i    = 0
    while i < n:
        suma = suma + matriz[i][j]
        i    = i + 1
    sumas_columnas.append(suma)
    j = j + 1

# Diagonal principal (fila == columna)
suma_diag_principal = 0
i = 0
while i < n:
    suma_diag_principal = suma_diag_principal + matriz[i][i]
    i = i + 1

# Diagonal secundaria (fila + columna == n - 1)
suma_diag_secundaria = 0
i = 0
while i < n:
    suma_diag_secundaria = suma_diag_secundaria + matriz[i][n - 1 - i]
    i = i + 1

# Comprobar si es magica: todas las sumas deben ser iguales
valor_referencia = sumas_filas[0]
es_magica        = True

i = 0
while i < n:
    if sumas_filas[i] != valor_referencia:
        es_magica = False
    if sumas_columnas[i] != valor_referencia:
        es_magica = False
    i = i + 1

if suma_diag_principal != valor_referencia:
    es_magica = False
if suma_diag_secundaria != valor_referencia:
    es_magica = False

if es_magica:
    print(f"\nLa matriz ES magica. Suma magica = {valor_referencia}")
else:
    print("\nLa matriz NO es magica. Detalle de sumas:")

    print("\n  Sumas por fila:")
    i = 0
    while i < n:
        print(f"    Fila {i}: {sumas_filas[i]}")
        i = i + 1

    print("\n  Sumas por columna:")
    j = 0
    while j < n:
        print(f"    Columna {j}: {sumas_columnas[j]}")
        j = j + 1

    print(f"\n  Diagonal principal : {suma_diag_principal}")
    print(f"  Diagonal secundaria: {suma_diag_secundaria}")


# ------------------------------------------------------------
# EJERCICIO 8
# Multiplicacion de dos matrices de orden 3.
# Para multiplicar matrices A (3x3) por B (3x3):
#   C[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + A[i][2]*B[2][j]
# Es decir: fila i de A  x  columna j de B
#
# Ejemplo del enunciado:
#     A              B              C
# [2 0 1]       [1 0 1]       [3 1 2]
# [3 0 0]   x   [1 2 1]   =   [3 0 3]
# [5 1 1]       [1 1 0]       [7 3 6]
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 8 -- Multiplicacion de dos matrices 3x3")
print("=" * 50)

# Cargar la primera matriz
print("Introduce la primera matriz A (3x3):")
A = []
i = 0
while i < 3:
    fila_nueva = []
    j          = 0
    while j < 3:
        valor = int(input(f"  A[{i}][{j}]: "))
        fila_nueva.append(valor)
        j = j + 1
    A.append(fila_nueva)
    i = i + 1

# Cargar la segunda matriz
print("\nIntroduce la segunda matriz B (3x3):")
B = []
i = 0
while i < 3:
    fila_nueva = []
    j          = 0
    while j < 3:
        valor = int(input(f"  B[{i}][{j}]: "))
        fila_nueva.append(valor)
        j = j + 1
    B.append(fila_nueva)
    i = i + 1

# Crear la matriz resultado C (3x3) inicializada a ceros
C = []
i = 0
while i < 3:
    fila_nueva = [0, 0, 0]
    C.append(fila_nueva)
    i = i + 1

# Calcular C = A x B
# C[i][j] = suma de A[i][k] * B[k][j] para k=0,1,2
i = 0
while i < 3:
    j = 0
    while j < 3:
        suma = 0
        k    = 0
        while k < 3:
            suma = suma + A[i][k] * B[k][j]
            k    = k + 1
        C[i][j] = suma
        j        = j + 1
    i = i + 1

# Mostrar resultado
print("\nResultado A x B:")
i = 0
while i < 3:
    linea = ""
    j     = 0
    while j < 3:
        linea = linea + f"{C[i][j]:5d}"
        j     = j + 1
    print(linea)
    i = i + 1


# ------------------------------------------------------------
# EJERCICIO 9
# Capturar una matriz 3x3 y calcular su determinante.
# Formula de Sarrus para 3x3:
# det = (a11*a22*a33 + a12*a23*a31 + a21*a32*a13)
#     - (a13*a22*a31 + a12*a21*a33 + a23*a32*a11)
#
# Con indices de Python (empezando en 0):
# det = (m[0][0]*m[1][1]*m[2][2] + m[0][1]*m[1][2]*m[2][0] + m[1][0]*m[2][1]*m[0][2])
#     - (m[0][2]*m[1][1]*m[2][0] + m[0][1]*m[1][0]*m[2][2] + m[1][2]*m[2][1]*m[0][0])
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 9 -- Determinante de una matriz 3x3")
print("=" * 50)

print("Introduce los valores de la matriz 3x3:")
m = []
i = 0
while i < 3:
    fila_nueva = []
    j          = 0
    while j < 3:
        valor = float(input(f"  [{i}][{j}]: "))
        fila_nueva.append(valor)
        j = j + 1
    m.append(fila_nueva)
    i = i + 1

# Regla de Sarrus
diagonal_principal = (m[0][0] * m[1][1] * m[2][2]
                    + m[0][1] * m[1][2] * m[2][0]
                    + m[1][0] * m[2][1] * m[0][2])

diagonal_secundaria = (m[0][2] * m[1][1] * m[2][0]
                     + m[0][1] * m[1][0] * m[2][2]
                     + m[1][2] * m[2][1] * m[0][0])

determinante = diagonal_principal - diagonal_secundaria

print(f"\nDeterminante = {determinante}")


# ------------------------------------------------------------
# EJERCICIO 10
# Inventario de m piezas en n almacenes.
# La tabla es de m x n: tabla[pieza][almacen] = unidades.
# Hay un vector de costes de m elementos (precio por pieza).
# Calcular:
#   - Valor total general
#   - Valor total de una pieza en todos los almacenes
#   - Valor total de todas las piezas por almacen
#   - Valor de cada pieza por almacen
#
# Ejemplo: m=3 piezas, n=2 almacenes
#           Almacen1  Almacen2
# Pieza 1:    31        50
# Pieza 2:    42       101
# Pieza 3:    64       194
# Costes: [19.61, 23, 86.4]
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 10 -- Inventario de almacenes")
print("=" * 50)

m = int(input("Numero de piezas (m): "))
n = int(input("Numero de almacenes (n): "))

# Cargar la tabla de unidades: tabla[pieza][almacen]
tabla_inv = []
print(f"\nIntroduce las unidades (tabla {m}x{n}, filas=piezas, columnas=almacenes):")
i = 0
while i < m:
    fila_nueva = []
    j          = 0
    while j < n:
        unidades = int(input(f"  Pieza {i + 1} en Almacen {j + 1}: "))
        fila_nueva.append(unidades)
        j = j + 1
    tabla_inv.append(fila_nueva)
    i = i + 1

# Cargar el vector de costes
costes = []
print("\nIntroduce el coste de cada pieza:")
i = 0
while i < m:
    coste = float(input(f"  Coste pieza {i + 1}: "))
    costes.append(coste)
    i = i + 1

# Calculos
print("\n--- RESULTADOS ---")

# Valor total general
valor_total_general = 0.0
i = 0
while i < m:
    j = 0
    while j < n:
        valor_total_general = valor_total_general + tabla_inv[i][j] * costes[i]
        j = j + 1
    i = i + 1
print(f"\nValor total general: {valor_total_general:.2f} EUR")

# Valor total de cada pieza en todos los almacenes
print("\nValor total de cada pieza (todos los almacenes):")
i = 0
while i < m:
    total_pieza = 0.0
    j           = 0
    while j < n:
        total_pieza = total_pieza + tabla_inv[i][j] * costes[i]
        j           = j + 1
    print(f"  Pieza {i + 1}: {total_pieza:.2f} EUR")
    i = i + 1

# Valor total de todas las piezas por almacen y valor de cada pieza por almacen
print("\nValor por almacen (desglose por pieza):")
j = 0
while j < n:
    total_almacen = 0.0
    print(f"\n  Almacen {j + 1}:")
    i = 0
    while i < m:
        valor_pieza_almacen = tabla_inv[i][j] * costes[i]
        total_almacen       = total_almacen + valor_pieza_almacen
        print(f"    Pieza {i + 1}: {tabla_inv[i][j]} uds x {costes[i]:.2f} EUR = {valor_pieza_almacen:.2f} EUR")
        i = i + 1
    print(f"  Total almacen {j + 1}: {total_almacen:.2f} EUR")
    j = j + 1


# ------------------------------------------------------------
# EJERCICIO 11
# Cambio de divisas.
# Tabla de equivalencias en euros:
#   Dolar          --> 0.82 EUR
#   Libra esterlina --> 1.072 EUR
#   Yen            --> 0.0075 EUR
#   Dirham         --> 0.084 EUR
#
# Se pide la moneda origen y cantidad, luego la moneda destino.
# Para convertir: euros = cantidad * equivalencia_origen
#                 resultado = euros / equivalencia_destino
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 11 -- Cambio de divisas")
print("=" * 50)

# Almacenamos las divisas en dos listas paralelas
nombres_divisas = ["Euro", "Dolar", "Libra", "Yen", "Dirham"]
valor_en_euros  = [1.0,    0.82,   1.072,  0.0075, 0.084]

print("\nDivisas disponibles:")
i = 0
while i < len(nombres_divisas):
    print(f"  {i}. {nombres_divisas[i]}")
    i = i + 1

# Paso 1: que moneda tienes y cantidad
idx_origen = int(input("\nQue moneda tienes? (introduce el numero): "))
cantidad   = float(input("Cuanta cantidad tienes: "))

# Convertir a euros primero
cantidad_en_euros = cantidad * valor_en_euros[idx_origen]

# Paso 2: a que moneda quieres convertir
print("\nDivisas disponibles:")
i = 0
while i < len(nombres_divisas):
    print(f"  {i}. {nombres_divisas[i]}")
    i = i + 1

idx_destino = int(input("A que moneda quieres convertir? (introduce el numero): "))

# Convertir de euros a la moneda destino
resultado = cantidad_en_euros / valor_en_euros[idx_destino]

print(f"\n{cantidad:.2f} {nombres_divisas[idx_origen]} = {resultado:.4f} {nombres_divisas[idx_destino]}")


# ------------------------------------------------------------
# EJERCICIO 12
# Gestion de ventas de 5 empleados de la ferreteria TUERCA S.A.
# Cada empleado puede tener varios albaranes (ventas).
# Calcular:
#   - Venta total de cada vendedor
#   - Venta media de cada vendedor
#   - Venta total de la empresa
#   - Venta media de la ferreteria
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 12 -- Ventas de 5 empleados (TUERCA S.A.)")
print("=" * 50)

NUM_EMPLEADOS = 5

# Almacenamos las ventas en una lista de listas
# ventas[empleado] = lista de importes de sus ventas
ventas = []
i      = 0
while i < NUM_EMPLEADOS:
    print(f"\n-- Empleado {i + 1} --")
    ventas_empleado = []

    while True:
        importe = float(input("  Importe del albaran (0 para terminar): "))
        if importe == 0:
            break
        ventas_empleado.append(importe)

    ventas.append(ventas_empleado)
    i = i + 1

# Calcular y mostrar resultados
print("\n--- INFORME DE VENTAS ---")
venta_total_empresa = 0.0
total_ventas_empresa = 0

i = 0
while i < NUM_EMPLEADOS:
    total_empleado = 0.0
    num_ventas     = len(ventas[i])

    j = 0
    while j < num_ventas:
        total_empleado = total_empleado + ventas[i][j]
        j              = j + 1

    if num_ventas > 0:
        media_empleado = total_empleado / num_ventas
    else:
        media_empleado = 0.0

    venta_total_empresa  = venta_total_empresa + total_empleado
    total_ventas_empresa = total_ventas_empresa + num_ventas

    print(f"\nEmpleado {i + 1}:")
    print(f"  Numero de ventas : {num_ventas}")
    print(f"  Venta total      : {total_empleado:.2f} EUR")
    print(f"  Venta media      : {media_empleado:.2f} EUR")
    i = i + 1

if total_ventas_empresa > 0:
    venta_media_empresa = venta_total_empresa / total_ventas_empresa
else:
    venta_media_empresa = 0.0

print(f"\nVenta total de la empresa  : {venta_total_empresa:.2f} EUR")
print(f"Venta media de la ferreteria: {venta_media_empresa:.2f} EUR")


# ------------------------------------------------------------
# EJERCICIO 13
# Sistema de numeracion en base 13.
# Simbolos: + - * / = ? \ ! ¿ $ ( @ #
# Valores:  0 1 2 3 4 5 6 7 8 9 10 11 12
#
# Convertir un numero decimal a base 13 y viceversa.
# El algoritmo es el mismo que para cualquier base:
#   - Decimal --> base 13: divisiones sucesivas entre 13
#   - Base 13 --> decimal: multiplicar por potencias de 13
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 13 -- Sistema de numeracion en base 13")
print("=" * 50)

# Tabla de simbolos (indice = valor, contenido = simbolo)
simbolos = ["+", "-", "*", "/", "=", "?", "\\", "!", "¿", "$", "(", "@", "#"]

print("Tabla de simbolos:")
i = 0
while i < len(simbolos):
    print(f"  {simbolos[i]} = {i}")
    i = i + 1

while True:
    print("\nOpciones:")
    print("  1. Decimal --> Base 13")
    print("  2. Base 13 --> Decimal")
    print("  3. Salir")

    opcion = int(input("Elige una opcion: "))

    if opcion == 3:
        break

    elif opcion == 1:
        # Decimal a base 13
        numero = int(input("Introduce un numero decimal: "))

        if numero == 0:
            print(f"En base 13: {simbolos[0]}")
        else:
            restos = []
            n      = numero

            while n > 0:
                resto = n % 13
                restos.append(simbolos[resto])    # guardamos el simbolo
                n     = n // 13

            # Los restos se leen en orden inverso
            resultado = ""
            i = len(restos) - 1
            while i >= 0:
                resultado = resultado + restos[i]
                i         = i - 1

            print(f"{numero} en base 13 es: {resultado}")

    elif opcion == 2:
        # Base 13 a decimal
        cadena_b13 = input("Introduce el numero en base 13 (usa los simbolos): ")

        # Convertir cada caracter a su valor numerico
        valor_decimal = 0
        posicion      = len(cadena_b13) - 1    # empezamos desde la derecha (posicion 0)
        i             = 0

        while i < len(cadena_b13):
            caracter = cadena_b13[i]

            # Buscar el simbolo en la tabla
            valor_simbolo = -1
            j             = 0
            while j < len(simbolos):
                if simbolos[j] == caracter:
                    valor_simbolo = j
                    break
                j = j + 1

            if valor_simbolo == -1:
                print(f"Error: '{caracter}' no es un simbolo valido")
                valor_decimal = -1
                break

            # Calcular 13^posicion manualmente
            potencia = 1
            k        = 0
            while k < posicion:
                potencia = potencia * 13
                k        = k + 1

            valor_decimal = valor_decimal + valor_simbolo * potencia
            posicion      = posicion - 1
            i             = i + 1

        if valor_decimal >= 0:
            print(f"{cadena_b13} en decimal es: {valor_decimal}")

    else:
        print("Opcion no valida")
