# ============================================================
#  PRACTICA 1 -- BUCLES BASICOS
#  (traducida a Python desde enunciado Java)
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 1 -- Potencias de 2 del 0 al 9 usando while
# ------------------------------------------------------------
print("=" * 40)
print("EJERCICIO 1 -- Potencias de 2 (0 a 9)")
print("=" * 40)

exponente = 0
while exponente <= 9:
    resultado = 2 ** exponente
    print(f"2 elevado a {exponente} = {resultado}")
    exponente = exponente + 1

# Salida:
# 2 elevado a 0 = 1
# 2 elevado a 1 = 2
# 2 elevado a 2 = 4
# ...
# 2 elevado a 9 = 512


# ------------------------------------------------------------
# EJERCICIO 2 -- Suma N primeros terminos de progresion geometrica
# Primer termino A y razon R dados por teclado
# SIN usar la formula, calculando termino a termino
# ------------------------------------------------------------
print("\n" + "=" * 40)
print("EJERCICIO 2 -- Progresion geometrica")
print("=" * 40)

A = float(input("Introduce el primer termino (A): "))
R = float(input("Introduce la razon (R): "))
N = int(input("Cuantos terminos quieres sumar (N): "))

suma        = 0
termino     = A
contador    = 1

while contador <= N:
    print(f"  Termino {contador}: {termino}")
    suma     = suma + termino
    termino  = termino * R      # cada termino = anterior * razon
    contador = contador + 1

print(f"Suma de los {N} primeros terminos: {suma}")


# ------------------------------------------------------------
# EJERCICIO 3 -- Sumar N numeros introducidos por teclado
# N se lee primero
# ------------------------------------------------------------
print("\n" + "=" * 40)
print("EJERCICIO 3 -- Suma de N numeros")
print("=" * 40)

N    = int(input("Cuantos numeros vas a introducir: "))
suma = 0
i    = 1

while i <= N:
    numero = float(input(f"Introduce el numero {i}: "))
    suma   = suma + numero
    i      = i + 1

print(f"La suma de los {N} numeros es: {suma}")


# ------------------------------------------------------------
# EJERCICIO 4 -- Suma N primeros impares / pares / multiples de 3
# ------------------------------------------------------------
print("\n" + "=" * 40)
print("EJERCICIO 4 -- Sumas especiales")
print("=" * 40)

N = int(input("Cuantos terminos quieres sumar: "))

# -- Suma de los N primeros impares --
suma_impares = 0
contador     = 0     # cuantos impares hemos sumado ya
numero       = 1     # primer impar

while contador < N:
    suma_impares = suma_impares + numero
    numero       = numero + 2    # siguiente impar
    contador     = contador + 1

print(f"Suma de los {N} primeros impares: {suma_impares}")

# -- Suma de los N primeros pares --
suma_pares = 0
contador   = 0
numero     = 2       # primer par

while contador < N:
    suma_pares = suma_pares + numero
    numero     = numero + 2      # siguiente par
    contador   = contador + 1

print(f"Suma de los {N} primeros pares: {suma_pares}")

# -- Suma de los N primeros multiplos de 3 --
suma_mult3 = 0
contador   = 0
numero     = 3       # primer multiplo de 3

while contador < N:
    suma_mult3 = suma_mult3 + numero
    numero     = numero + 3      # siguiente multiplo de 3
    contador   = contador + 1

print(f"Suma de los {N} primeros multiplos de 3: {suma_mult3}")


# ------------------------------------------------------------
# EJERCICIO 5 -- Sucesion de Fibonacci hasta el N-esimo termino
# a1=1, a2=1, an = an-1 + an-2
# ------------------------------------------------------------
print("\n" + "=" * 40)
print("EJERCICIO 5 -- Sucesion de Fibonacci")
print("=" * 40)

N = int(input("Hasta que termino quieres ver la sucesion: "))

if N <= 0:
    print("N debe ser mayor que 0")
elif N == 1:
    print("Termino 1: 1")
else:
    anterior     = 1     # primer termino
    actual       = 1     # segundo termino
    contador     = 1

    print(f"Termino {contador}: {anterior}")
    contador = contador + 1

    while contador <= N:
        print(f"Termino {contador}: {actual}")
        siguiente    = anterior + actual    # calculamos el siguiente
        anterior     = actual               # desplazamos
        actual       = siguiente
        contador     = contador + 1

# Primeros terminos: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...


# ------------------------------------------------------------
# EJERCICIO 6 -- Factura con IVA y descuentos
# ------------------------------------------------------------
print("\n" + "=" * 40)
print("EJERCICIO 6 -- Calculo de factura")
print("=" * 40)

suma_importes = 0.0
suma_ivas     = 0.0

# Bucle de entrada de datos, termina cuando importe = 0
while True:

    # Leer importe
    importe = float(input("\nIntroduce el importe (0 para terminar): "))

    if importe == 0:
        break    # salimos del bucle

    # Leer y validar el IVA -- solo acepta 4, 7 o 16
    iva_valido = False
    while not iva_valido:
        iva = int(input("Introduce el IVA (4, 7 o 16): "))
        if iva == 4 or iva == 7 or iva == 16:
            iva_valido = True
        else:
            print("IVA no valido. Debes introducir 4, 7 o 16.")

    # Acumular importes e ivas
    importe_iva   = importe * iva / 100
    suma_importes = suma_importes + importe
    suma_ivas     = suma_ivas + importe_iva

    print(f"  Linea anadida: {importe} EUR + {iva}% IVA = {importe_iva:.2f} EUR")

# Calcular descuento sobre la suma de importes
if suma_importes < 1000:
    porcentaje_descuento = 0
elif suma_importes < 10000:
    porcentaje_descuento = 5
else:
    porcentaje_descuento = 10

descuento_importe = suma_importes * porcentaje_descuento / 100
descuento_iva     = suma_ivas * porcentaje_descuento / 100

total_importe = suma_importes - descuento_importe
total_iva     = suma_ivas - descuento_iva
total_factura = total_importe + total_iva

# Mostrar resultado final
print("\n--- RESUMEN DE FACTURA ---")
print(f"Suma importes bruta : {suma_importes:.2f} EUR")
print(f"Suma IVAs bruta     : {suma_ivas:.2f} EUR")
print(f"Descuento aplicado  : {porcentaje_descuento}%")
print(f"Importe tras descto : {total_importe:.2f} EUR")
print(f"IVA tras descuento  : {total_iva:.2f} EUR")
print(f"TOTAL FACTURA       : {total_factura:.2f} EUR")
