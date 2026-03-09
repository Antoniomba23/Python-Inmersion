# ============================================================
#  PRACTICA 1.1 -- ALGORITMOS CON INSTRUCCIONES ALTERNATIVAS
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 1
# Crear un algoritmo que pida al usuario un numero y le diga
# si es positivo, negativo o cero.
# ------------------------------------------------------------
print("=" * 50)
print("EJERCICIO 1 -- Positivo, negativo o cero")
print("=" * 50)

numero = float(input("Introduce un numero: "))

if numero > 0:
    print("El numero es POSITIVO")
elif numero < 0:
    print("El numero es NEGATIVO")
else:
    print("El numero es CERO")


# ------------------------------------------------------------
# EJERCICIO 2
# Programa que capture un numero por teclado e indique
# si es par o impar.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 2 -- Par o impar")
print("=" * 50)

numero = int(input("Introduce un numero entero: "))

if numero % 2 == 0:
    print(f"{numero} es PAR")
else:
    print(f"{numero} es IMPAR")


# ------------------------------------------------------------
# EJERCICIO 3
# Crea un programa que pida al usuario dos numeros y muestre
# su division si el segundo no es cero, o un mensaje de aviso
# en caso contrario.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 3 -- Division segura")
print("=" * 50)

a = float(input("Introduce el primer numero: "))
b = float(input("Introduce el segundo numero: "))

if b == 0:
    print("Error: no se puede dividir entre cero")
else:
    resultado = a / b
    print(f"{a} / {b} = {resultado}")


# ------------------------------------------------------------
# EJERCICIO 4
# Calcular la potencia pidiendo base y exponente por teclado.
# - Exponente positivo: imprimir la potencia
# - Exponente 0: el resultado es 1
# - Exponente negativo: el resultado es 1 / (base ^ exponente positivo)
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 4 -- Calculo de potencia")
print("=" * 50)

base      = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

if exponente == 0:
    resultado = 1
    print(f"{base} elevado a {exponente} = {resultado}")

elif exponente > 0:
    resultado = 1
    i = 0
    while i < exponente:
        resultado = resultado * base
        i = i + 1
    print(f"{base} elevado a {exponente} = {resultado}")

else:
    # Exponente negativo: calculamos la potencia con el exponente positivo
    exp_positivo = exponente * -1    # convertimos a positivo
    potencia = 1
    i = 0
    while i < exp_positivo:
        potencia = potencia * base
        i = i + 1
    resultado = 1 / potencia
    print(f"{base} elevado a {exponente} = {resultado}")


# ------------------------------------------------------------
# EJERCICIO 5
# Pide nota, edad y genero.
# Muestra ACEPTADA si nota >= 5, edad >= 18 y genero == F
# Muestra ACEPTADO si nota >= 5, edad >= 18 y genero == M
# Si no se cumplen las condiciones: NO ACEPTADO/A
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 5 -- Aceptado o no")
print("=" * 50)

nota   = float(input("Introduce la nota: "))
edad   = int(input("Introduce la edad: "))
genero = input("Introduce el genero (M/F): ")

if nota >= 5 and edad >= 18 and genero == "F":
    print("ACEPTADA")
elif nota >= 5 and edad >= 18 and genero == "M":
    print("ACEPTADO")
else:
    print("NO ACEPTADO/A")


# ------------------------------------------------------------
# EJERCICIO 6
# Lee los 3 lados de un triangulo A, B, C y determina el tipo:
# - Rectangulo: cumple el teorema de Pitagoras
# - Equilatero: los 3 lados son iguales
# - Isosceles: solo 2 lados son iguales
# - Escaleno: ninguna de las anteriores
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 6 -- Tipo de triangulo")
print("=" * 50)

a = float(input("Introduce el lado A: "))
b = float(input("Introduce el lado B: "))
c = float(input("Introduce el lado C: "))

# Para comprobar Pitagoras necesitamos saber cual es la hipotenusa (el lado mayor)
# Ordenamos manualmente los tres lados
if a >= b and a >= c:
    hip = a
    cat1 = b
    cat2 = c
elif b >= a and b >= c:
    hip = b
    cat1 = a
    cat2 = c
else:
    hip = c
    cat1 = a
    cat2 = b

# Comprobamos Pitagoras: hip^2 == cat1^2 + cat2^2
# Usamos round para evitar problemas de precision con decimales
if round(hip ** 2, 5) == round(cat1 ** 2 + cat2 ** 2, 5):
    print("El triangulo es RECTANGULO")
elif a == b and b == c:
    print("El triangulo es EQUILATERO")
elif a == b or b == c or a == c:
    print("El triangulo es ISOSCELES")
else:
    print("El triangulo es ESCALENO")


# ------------------------------------------------------------
# EJERCICIO 7
# Leer un anio e indicar si es bisiesto.
# Un anio es bisiesto si es divisible por 4,
# pero NO si es divisible por 100,
# excepto que tambien sea divisible por 400.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 7 -- Anio bisiesto")
print("=" * 50)

anio = int(input("Introduce un anio: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"{anio} ES bisiesto")
else:
    print(f"{anio} NO es bisiesto")


# ------------------------------------------------------------
# EJERCICIO 8
# Calcular la raiz cuadrada del numero que introduzca el usuario.
# Si se introduce un numero negativo, mostrar un mensaje de error.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 8 -- Raiz cuadrada")
print("=" * 50)

import math

numero = float(input("Introduce un numero: "))

if numero < 0:
    print("Error: no se puede calcular la raiz cuadrada de un numero negativo")
else:
    raiz = math.sqrt(numero)
    print(f"La raiz cuadrada de {numero} es {raiz:.4f}")


# ------------------------------------------------------------
# EJERCICIO 9
# Determinar el menor valor de 5 numeros introducidos por teclado.
# El menor valor puede repetirse.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 9 -- Menor de 5 numeros")
print("=" * 50)

n1 = float(input("Introduce el numero 1: "))
n2 = float(input("Introduce el numero 2: "))
n3 = float(input("Introduce el numero 3: "))
n4 = float(input("Introduce el numero 4: "))
n5 = float(input("Introduce el numero 5: "))

# Comparamos manualmente uno a uno
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n4 < menor:
    menor = n4
if n5 < menor:
    menor = n5

print(f"El menor valor introducido es {menor}")


# ------------------------------------------------------------
# EJERCICIO 10
# Introducimos dos numeros por teclado y guardamos el mayor
# en la variable MAYOR y el menor en la variable MENOR.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 10 -- Mayor y menor")
print("=" * 50)

a = float(input("Introduce el primer numero: "))
b = float(input("Introduce el segundo numero: "))

if a >= b:
    mayor = a
    menor = b
else:
    mayor = b
    menor = a

print(f"MAYOR = {mayor}")
print(f"MENOR = {menor}")


# ------------------------------------------------------------
# EJERCICIO 11
# Capturamos tres numeros por teclado y los ordenamos de mayor a menor.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 11 -- Tres numeros de mayor a menor")
print("=" * 50)

a = float(input("Introduce el primer numero: "))
b = float(input("Introduce el segundo numero: "))
c = float(input("Introduce el tercer numero: "))

# Ordenar de mayor a menor intercambiando si hace falta
# Pasada 1: asegurar que el mayor esta en a
if b > a:
    a, b = b, a
if c > a:
    a, c = c, a

# Pasada 2: asegurar que el segundo mayor esta en b
if c > b:
    b, c = c, b

print(f"Ordenados de mayor a menor: {a}, {b}, {c}")


# ------------------------------------------------------------
# EJERCICIO 12
# Lee un numero entero (positivo o negativo) y determina
# si tiene 1, 2, 3, 4 o mas cifras.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 12 -- Numero de cifras")
print("=" * 50)

numero = int(input("Introduce un numero entero: "))

# Trabajamos con el valor absoluto para ignorar el signo negativo
valor = numero
if valor < 0:
    valor = valor * -1

if valor < 10:
    print(f"{numero} tiene 1 cifra")
elif valor < 100:
    print(f"{numero} tiene 2 cifras")
elif valor < 1000:
    print(f"{numero} tiene 3 cifras")
elif valor < 10000:
    print(f"{numero} tiene 4 cifras")
else:
    print(f"{numero} tiene mas de 4 cifras")


# ------------------------------------------------------------
# EJERCICIO 13
# Calculadora que pide dos valores numericos y la operacion:
# suma, resta, multiplicacion o division.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 13 -- Calculadora")
print("=" * 50)

a         = float(input("Introduce el primer numero: "))
b         = float(input("Introduce el segundo numero: "))
operacion = input("Operacion (suma / resta / multiplicacion / division): ")

if operacion == "suma":
    print(f"{a} + {b} = {a + b}")
elif operacion == "resta":
    print(f"{a} - {b} = {a - b}")
elif operacion == "multiplicacion":
    print(f"{a} * {b} = {a * b}")
elif operacion == "division":
    if b == 0:
        print("Error: no se puede dividir entre cero")
    else:
        print(f"{a} / {b} = {a / b}")
else:
    print("Operacion no reconocida")


# ------------------------------------------------------------
# EJERCICIO 14
# Pide el dia de la semana (del 1 al 7) y escribe el dia
# correspondiente. Si es otro numero, muestra un error.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 14 -- Dia de la semana")
print("=" * 50)

dia = int(input("Introduce el dia de la semana (1-7): "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
else:
    print("Error: introduce un numero entre 1 y 7")
