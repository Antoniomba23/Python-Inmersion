# ============================================================
#  PRACTICA 8.1 -- EJERCICIOS CON VECTORES (LISTAS) I
#  En Python los "arrays" o "vectores" de Java son listas.
# ============================================================

import random
import math


# ------------------------------------------------------------
# EJERCICIO 1
# Cargar un vector de 10 elementos desde teclado.
# Mostrar el valor del elemento mayor y cuantas veces se repite.
# ------------------------------------------------------------
print("=" * 50)
print("EJERCICIO 1 -- Mayor y cuantas veces se repite")
print("=" * 50)

vector = []
i      = 0
while i < 10:
    numero = float(input(f"Introduce el elemento {i}: "))
    vector.append(numero)
    i = i + 1

# Buscar el maximo recorriendo la lista
mayor = vector[0]
i     = 1
while i < len(vector):
    if vector[i] > mayor:
        mayor = vector[i]
    i = i + 1

# Contar cuantas veces aparece el maximo
veces = 0
i     = 0
while i < len(vector):
    if vector[i] == mayor:
        veces = veces + 1
    i = i + 1

print(f"\nEl valor mayor es {mayor} y aparece {veces} vez/veces")


# ------------------------------------------------------------
# EJERCICIO 2
# Dos vectores de 15 elementos generados aleatoriamente entre 0 y 100.
# Obtener un tercer vector donde cada elemento es la suma
# de los elementos en la misma posicion de los dos vectores.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 2 -- Suma de dos vectores elemento a elemento")
print("=" * 50)

vector1 = []
vector2 = []
vector3 = []

# Rellenar los dos vectores con numeros aleatorios
i = 0
while i < 15:
    vector1.append(random.randint(0, 100))
    vector2.append(random.randint(0, 100))
    i = i + 1

# Calcular vector3 = vector1 + vector2 (posicion a posicion)
i = 0
while i < 15:
    vector3.append(vector1[i] + vector2[i])
    i = i + 1

# Mostrar los tres vectores
print("Vector1:", vector1)
print("Vector2:", vector2)
print("Vector3:", vector3)


# ------------------------------------------------------------
# EJERCICIO 3
# Inicializar un array de 10 elementos y mostrar los que sean
# pares y la posicion en que se encuentran.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 3 -- Elementos pares y su posicion")
print("=" * 50)

# Array con 10 numeros fijos para demostrar
array = [4, 7, 12, 3, 8, 15, 6, 21, 10, 9]
print(f"Array: {array}")
print("\nElementos pares:")

i = 0
while i < len(array):
    if array[i] % 2 == 0:
        print(f"  Posicion {i}: {array[i]}")
    i = i + 1


# ------------------------------------------------------------
# EJERCICIO 4
# Cargar un vector de 10 elementos desde teclado.
# Calcular la media de los elementos en posiciones PARES (0,2,4...)
# y la media de los elementos en posiciones IMPARES (1,3,5...).
# La lista solo se recorre UNA vez.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 4 -- Media de posiciones pares e impares")
print("=" * 50)

vector = []
i      = 0
while i < 10:
    numero = float(input(f"Introduce el elemento {i}: "))
    vector.append(numero)
    i = i + 1

suma_pares   = 0.0
suma_impares = 0.0
cant_pares   = 0
cant_impares = 0

# Recorremos la lista UNA sola vez
i = 0
while i < len(vector):
    if i % 2 == 0:               # posicion par: 0, 2, 4, 6, 8
        suma_pares = suma_pares + vector[i]
        cant_pares = cant_pares + 1
    else:                        # posicion impar: 1, 3, 5, 7, 9
        suma_impares = suma_impares + vector[i]
        cant_impares = cant_impares + 1
    i = i + 1

media_pares   = suma_pares / cant_pares
media_impares = suma_impares / cant_impares

print(f"\nMedia de posiciones pares   (0,2,4...): {media_pares:.2f}")
print(f"Media de posiciones impares (1,3,5...): {media_impares:.2f}")


# ------------------------------------------------------------
# EJERCICIO 5
# 1. Llenar un array con estaturas de alumnos (N por teclado)
# 2. Calcular la suma de todas las estaturas
# 3. Calcular la media de estaturas
# 4. Mostrar cuantos son mas altos que la media y cuantos mas bajos
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 5 -- Estaturas de alumnos")
print("=" * 50)

N = int(input("Cuantos alumnos hay en la clase: "))

estaturas = []
i         = 0
while i < N:
    estatura = float(input(f"Estatura del alumno {i + 1} (en cm): "))
    estaturas.append(estatura)
    i = i + 1

# Calcular la suma
suma = 0.0
i    = 0
while i < N:
    suma = suma + estaturas[i]
    i    = i + 1

# Calcular la media
media = suma / N

# Contar mas altos y mas bajos
mas_altos  = 0
mas_bajos  = 0
i          = 0
while i < N:
    if estaturas[i] > media:
        mas_altos = mas_altos + 1
    elif estaturas[i] < media:
        mas_bajos = mas_bajos + 1
    i = i + 1

print(f"\nSuma de estaturas  : {suma:.1f} cm")
print(f"Media de estaturas : {media:.2f} cm")
print(f"Mas altos que media: {mas_altos} alumnos")
print(f"Mas bajos que media: {mas_bajos} alumnos")


# ------------------------------------------------------------
# EJERCICIO 6
# Cargar un vector con las notas de 40 alumnos.
# Mostrar: aprobados, suspensos, nota media, y cuantos
# tienen calificacion superior a la media.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 6 -- Notas de 40 alumnos")
print("=" * 50)

notas = []
i     = 0
while i < 40:
    nota = float(input(f"Nota del alumno {i + 1}: "))
    notas.append(nota)
    i = i + 1

# Calcular media, aprobados y suspensos
suma      = 0.0
aprobados = 0
suspensos = 0
i         = 0
while i < 40:
    suma = suma + notas[i]
    if notas[i] >= 5:
        aprobados = aprobados + 1
    else:
        suspensos = suspensos + 1
    i = i + 1

media = suma / 40

# Contar cuantos superan la media
sobre_media = 0
i           = 0
while i < 40:
    if notas[i] > media:
        sobre_media = sobre_media + 1
    i = i + 1

print(f"\nAprobados          : {aprobados}")
print(f"Suspensos          : {suspensos}")
print(f"Nota media         : {media:.2f}")
print(f"Sobre la media     : {sobre_media} alumnos")


# ------------------------------------------------------------
# EJERCICIO 7
# Cargar un vector TB_NUM de hasta 100 elementos desde teclado.
# Introducir un valor e intercalarlo en su posicion correcta
# dentro del vector (supuestamente ordenado).
# El valor antiguo de esa posicion se pierde.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 7 -- Intercalar valor en posicion correcta")
print("=" * 50)

# Cargar el vector ordenado (para el ejemplo usamos 10 elementos)
N = int(input("Cuantos elementos tiene el vector (max 100): "))

tb_num = []
print("Introduce los elementos en orden ascendente:")
i = 0
while i < N:
    elemento = float(input(f"Elemento {i}: "))
    tb_num.append(elemento)
    i = i + 1

# Buscar la posicion correcta para el nuevo valor
nuevo = float(input("Introduce el valor a intercalar: "))

posicion = N    # por defecto va al final
i        = 0
while i < N:
    if nuevo <= tb_num[i]:
        posicion = i
        break
    i = i + 1

# Sustituir el elemento en esa posicion (el valor antiguo se pierde)
if posicion < N:
    tb_num[posicion] = nuevo
else:
    # Si va al final y hay sitio, lo sustituimos en la ultima posicion
    # (segun el enunciado el valor que estaba se pierde)
    tb_num[N - 1] = nuevo

print(f"\nVector con el valor intercalado:")
print(tb_num)


# ------------------------------------------------------------
# EJERCICIO 8
# Cargar un vector TB_NUM desde teclado.
# Introducir una posicion y eliminar el elemento de esa posicion.
# Eliminar = desplazar todos los elementos posteriores una
# posicion a la izquierda. El ultimo queda en 0 o vacio.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 8 -- Eliminar elemento de una posicion")
print("=" * 50)

N = int(input("Cuantos elementos tiene el vector: "))

tb_num = []
i      = 0
while i < N:
    elemento = float(input(f"Elemento {i}: "))
    tb_num.append(elemento)
    i = i + 1

print(f"Vector original: {tb_num}")

posicion = int(input(f"Introduce la posicion a eliminar (0 a {N - 1}): "))

if posicion < 0 or posicion >= N:
    print("Posicion fuera de rango")
else:
    # Desplazar todos los elementos desde posicion+1 hacia la izquierda
    i = posicion
    while i < N - 1:
        tb_num[i] = tb_num[i + 1]
        i         = i + 1

    # El ultimo elemento ya no tiene valor util, lo eliminamos
    tb_num.pop()

    print(f"Vector sin el elemento: {tb_num}")


# ------------------------------------------------------------
# EJERCICIO 9
# Leer un numero entero y almacenarlo en un array de modo que
# cada cifra ocupe un elemento del array.
# Ejemplo: 23451 --> [2, 3, 4, 5, 1]
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 9 -- Cifras de un numero en un array")
print("=" * 50)

numero_str = input("Introduce un numero entero: ")

# Eliminamos el signo negativo si lo hay
if numero_str[0] == "-":
    numero_str = numero_str[1:]

array_cifras = []
i            = 0
while i < len(numero_str):
    cifra = int(numero_str[i])    # convertimos cada caracter a entero
    array_cifras.append(cifra)
    i = i + 1

print(f"Array de cifras: {array_cifras}")


# ------------------------------------------------------------
# EJERCICIO 10
# Pedir un numero entero positivo de hasta 10 cifras y comprobar
# si es capicua (se lee igual de izquierda a derecha que al reves).
# Ejemplo: 12321 es capicua. 12345 no lo es.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 10 -- Numero capicua")
print("=" * 50)

numero_str = input("Introduce un numero entero positivo (hasta 10 cifras): ")

# Guardamos cada cifra en un array
cifras = []
i      = 0
while i < len(numero_str):
    cifras.append(int(numero_str[i]))
    i = i + 1

# Comparamos la primera con la ultima, la segunda con la penultima...
es_capicua = True
izquierda  = 0
derecha    = len(cifras) - 1

while izquierda < derecha:
    if cifras[izquierda] != cifras[derecha]:
        es_capicua = False
        break
    izquierda = izquierda + 1
    derecha   = derecha - 1

if es_capicua:
    print(f"{numero_str} ES capicua")
else:
    print(f"{numero_str} NO es capicua")
