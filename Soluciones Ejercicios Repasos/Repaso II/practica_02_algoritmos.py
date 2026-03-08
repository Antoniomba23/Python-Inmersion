# ============================================================
#  PRACTICA 2 -- ALGORITMOS CLASICOS
#  (traducida a Python desde enunciado Java)
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 1 -- Maximo Comun Divisor (algoritmo de Euclides)
# 1. Divide N entre M, sea R el resto
# 2. Si R=0, el MCD es M y se acaba
# 3. N = M, M = R, volver al paso 1
# ------------------------------------------------------------
print("=" * 40)
print("EJERCICIO 1 -- Maximo Comun Divisor")
print("=" * 40)

N = int(input("Introduce el primer numero (N): "))
M = int(input("Introduce el segundo numero (M): "))

# Guardamos los originales para mostrarlos al final
n_original = N
m_original = M

while True:
    R = N % M       # calculamos el resto

    if R == 0:
        # El MCD es M cuando el resto es 0
        break

    # Desplazamos: N pasa a ser M, M pasa a ser el resto R
    N = M
    M = R

mcd = M
print(f"El MCD de {n_original} y {m_original} es: {mcd}")

# Ejemplo: MCD(48, 18)
# 48 % 18 = 12  --> N=18, M=12
# 18 % 12 =  6  --> N=12, M=6
# 12 %  6 =  0  --> MCD = 6


# ------------------------------------------------------------
# EJERCICIO 2 -- Numero perfecto
# Un numero N es perfecto si la suma de sus divisores
# (sin incluir el propio N) es igual a N
# Ejemplo: 28 --> divisores: 1,2,4,7,14 --> suma = 28
# ------------------------------------------------------------
print("\n" + "=" * 40)
print("EJERCICIO 2 -- Numero perfecto")
print("=" * 40)

N = int(input("Introduce un numero para comprobar si es perfecto: "))

suma_divisores = 0
divisor        = 1

while divisor < N:        # probamos todos los divisores desde 1 hasta N-1
    if N % divisor == 0:  # si el resto es 0, es divisor
        suma_divisores = suma_divisores + divisor
    divisor = divisor + 1

if suma_divisores == N:
    print(f"{N} ES un numero perfecto (suma divisores = {suma_divisores})")
else:
    print(f"{N} NO es un numero perfecto (suma divisores = {suma_divisores})")

# Numeros perfectos conocidos: 6, 28, 496, 8128


# ------------------------------------------------------------
# EJERCICIO 3 -- Dia siguiente
# Dados un dia D, mes M y anio A, calcular el dia siguiente
# Tener en cuenta anios bisiestos (febrero 28 o 29 dias)
# ------------------------------------------------------------
print("\n" + "=" * 40)
print("EJERCICIO 3 -- Dia siguiente")
print("=" * 40)

D = int(input("Introduce el dia: "))
M = int(input("Introduce el mes (1-12): "))
A = int(input("Introduce el anio: "))

# Determinar si el anio es bisiesto
# Un anio es bisiesto si es divisible por 4,
# EXCEPTO los multiplos de 100, que solo son bisiestos si son multiplos de 400
if (A % 4 == 0 and A % 100 != 0) or (A % 400 == 0):
    bisiesto = True
else:
    bisiesto = False

# Determinar cuantos dias tiene el mes actual
if M == 2:
    if bisiesto:
        dias_del_mes = 29
    else:
        dias_del_mes = 28
elif M == 4 or M == 6 or M == 9 or M == 11:
    dias_del_mes = 30
else:
    dias_del_mes = 31

# Calcular el dia siguiente
if D < dias_del_mes:
    # Caso normal: avanzamos un dia dentro del mismo mes
    D_siguiente = D + 1
    M_siguiente = M
    A_siguiente = A

elif M == 12:
    # Ultimo dia de diciembre: cambiamos de anio
    D_siguiente = 1
    M_siguiente = 1
    A_siguiente = A + 1

else:
    # Ultimo dia del mes pero no es diciembre: cambiamos de mes
    D_siguiente = 1
    M_siguiente = M + 1
    A_siguiente = A

print(f"Fecha introducida : {D:02d}/{M:02d}/{A}")
print(f"Dia siguiente     : {D_siguiente:02d}/{M_siguiente:02d}/{A_siguiente}")
if bisiesto:
    print(f"(El anio {A} es bisiesto)")


# ------------------------------------------------------------
# EJERCICIO 4 -- Salario semanal de operarios
# Hasta 40h -> precio normal P por hora
# Horas extras (> 40h) -> 1.5 * P por hora
# El programa repite hasta que horas = 0
# ------------------------------------------------------------
print("\n" + "=" * 40)
print("EJERCICIO 4 -- Calculo de salario")
print("=" * 40)

while True:
    horas = float(input("\nHoras trabajadas esta semana (0 para salir): "))

    if horas == 0:
        print("Fin del programa.")
        break

    P = float(input("Precio por hora (P): "))

    if horas <= 40:
        # Sin horas extras
        salario      = horas * P
        horas_extra  = 0
        horas_normal = horas
    else:
        # Con horas extras
        horas_normal = 40
        horas_extra  = horas - 40
        salario      = (horas_normal * P) + (horas_extra * 1.5 * P)

    print(f"\n--- RESUMEN SALARIAL ---")
    print(f"Horas normales : {horas_normal}h x {P} EUR = {horas_normal * P:.2f} EUR")
    if horas_extra > 0:
        print(f"Horas extras   : {horas_extra}h x {1.5 * P} EUR = {horas_extra * 1.5 * P:.2f} EUR")
    print(f"SALARIO TOTAL  : {salario:.2f} EUR")
