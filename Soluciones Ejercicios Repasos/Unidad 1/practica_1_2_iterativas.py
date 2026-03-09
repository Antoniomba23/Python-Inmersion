# ============================================================
#  PRACTICA 1.2 -- ALGORITMOS CON ESTRUCTURAS ITERATIVAS
#  (Basada en el documento 1_2_ALGORITMOS_CON_ESTRUCTURAS_ITERATIVAS)
# ============================================================

import math
import random
import time


# ------------------------------------------------------------
# EJERCICIO 1
# Muestra en pantalla 15 numeros obtenidos de forma aleatoria.
# Entre un numero y otro el ordenador espera 2 segundos.
# ------------------------------------------------------------
print("=" * 50)
print("EJERCICIO 1 -- 15 numeros aleatorios con pausa")
print("=" * 50)

contador = 1
while contador <= 15:
    numero = random.randint(1, 100)
    print(f"Numero {contador:2d}: {numero}")
    if contador < 15:
        time.sleep(2)    # espera 2 segundos entre numeros
    contador = contador + 1


# ------------------------------------------------------------
# EJERCICIO 2
# Modifica el ejercicio 1 de la PRACTICA 2.2 (nota media alumno)
# para que el proceso se repita 5 veces (5 alumnos).
# Mostrar al final la NOTA MEDIA DEL GRUPO. Usar numeros reales.
# (Ej. 1 P2.2: capturar nombre y 3 notas, mostrar media del alumno)
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 2 -- Nota media de 5 alumnos y del grupo")
print("=" * 50)

suma_medias_grupo = 0.0
alumno_num        = 1

while alumno_num <= 5:
    print(f"\n-- Alumno {alumno_num} --")
    nombre = input("Nombre del alumno: ")
    nota1  = float(input("Nota evaluacion 1: "))
    nota2  = float(input("Nota evaluacion 2: "))
    nota3  = float(input("Nota evaluacion 3: "))

    media_alumno    = (nota1 + nota2 + nota3) / 3
    suma_medias_grupo = suma_medias_grupo + media_alumno

    print(f"La nota media de {nombre} es {media_alumno:.2f}")
    alumno_num = alumno_num + 1

media_grupo = suma_medias_grupo / 5
print(f"\nNOTA MEDIA DEL GRUPO: {media_grupo:.2f}")


# ------------------------------------------------------------
# EJERCICIO 3
# Captura por teclado un numero y pregunta la tabla de multiplicar
# de dicho numero. El usuario responde y el programa indica si
# es correcto o incorrecto.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 3 -- Tabla de multiplicar")
print("=" * 50)

numero = int(input("Introduce un numero para repasar su tabla: "))

multiplicador = 1
while multiplicador <= 10:
    respuesta = int(input(f"{numero} x {multiplicador} = "))
    resultado_correcto = numero * multiplicador

    if respuesta == resultado_correcto:
        print("Correcto!")
    else:
        print(f"Incorrecto. La respuesta correcta es {resultado_correcto}")

    multiplicador = multiplicador + 1


# ------------------------------------------------------------
# EJERCICIO 4
# Calcular la raiz cuadrada del numero que introduzca el usuario.
# Si introduce un numero negativo, mostrar error y volver a
# pedirlo (tantas veces como sea necesario).
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 4 -- Raiz cuadrada con validacion")
print("=" * 50)

numero = -1    # valor inicial para entrar al bucle

while numero < 0:
    numero = float(input("Introduce un numero (positivo): "))
    if numero < 0:
        print("Error: el numero debe ser positivo. Intentalo de nuevo.")

raiz = math.sqrt(numero)
print(f"La raiz cuadrada de {numero} es {raiz:.4f}")


# ------------------------------------------------------------
# EJERCICIO 5
# Modifica el ejercicio 2 de la P2.2 (calculo de sueldo neto)
# para que el proceso se repita mientras el sueldo sea positivo.
# Al final indicar:
#   - Total recaudado por el Estado (IRPF + SS)
#   - Total pagado por la empresa (suma de sueldos brutos)
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 5 -- Sueldos netos hasta sueldo = 0")
print("=" * 50)

total_irpf          = 0.0
total_ss            = 0.0
total_bruto_empresa = 0.0

sueldo_bruto = float(input("Introduce el sueldo bruto (0 para terminar): "))

while sueldo_bruto > 0:
    nombre = input("Nombre de la persona: ")

    descuento_irpf = sueldo_bruto * 12 / 100
    descuento_ss   = sueldo_bruto * 5.20 / 100
    sueldo_neto    = sueldo_bruto - descuento_irpf - descuento_ss

    total_irpf          = total_irpf + descuento_irpf
    total_ss            = total_ss + descuento_ss
    total_bruto_empresa = total_bruto_empresa + sueldo_bruto

    print(f"El sueldo neto de {nombre} es {sueldo_neto:.2f} euros")

    sueldo_bruto = float(input("\nIntroduce el sueldo bruto (0 para terminar): "))

print(f"\n--- RESUMEN FINAL ---")
print(f"Total IRPF recaudado    : {total_irpf:.2f} euros")
print(f"Total SS recaudada      : {total_ss:.2f} euros")
print(f"Total recaudado Estado  : {total_irpf + total_ss:.2f} euros")
print(f"Total pagado empresa    : {total_bruto_empresa:.2f} euros")


# ------------------------------------------------------------
# EJERCICIO 6
# Repetir el ejercicio 1 de la practica 1.1 (positivo/negativo/cero)
# Contar cuantos numeros de cada grupo tenemos.
# Antes de introducir el siguiente numero, preguntar si continuar.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 6 -- Contar positivos, negativos y ceros")
print("=" * 50)

positivos = 0
negativos = 0
ceros     = 0

while True:
    numero = float(input("Introduce un numero: "))

    if numero > 0:
        positivos = positivos + 1
        print("El numero es POSITIVO")
    elif numero < 0:
        negativos = negativos + 1
        print("El numero es NEGATIVO")
    else:
        ceros = ceros + 1
        print("El numero es CERO")

    respuesta = input("Deseas continuar? (S/N): ")
    if respuesta.upper() == "N":
        break

print(f"\nPositivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Ceros    : {ceros}")


# ------------------------------------------------------------
# EJERCICIO 7
# Modificar el ejercicio 3 para repasar tablas continuamente
# hasta que el usuario lo indique.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 7 -- Repaso continuo de tablas")
print("=" * 50)

while True:
    numero = int(input("Introduce un numero para repasar su tabla: "))

    multiplicador = 1
    while multiplicador <= 10:
        respuesta = int(input(f"{numero} x {multiplicador} = "))
        resultado_correcto = numero * multiplicador

        if respuesta == resultado_correcto:
            print("Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es {resultado_correcto}")

        multiplicador = multiplicador + 1

    respuesta = input("Quieres repasar otra tabla? (S/N): ")
    if respuesta.upper() == "N":
        break


# ------------------------------------------------------------
# EJERCICIO 8
# Modificar el ejercicio 7 para contar el numero de fallos
# al repasar una tabla de multiplicar.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 8 -- Repaso de tablas contando fallos")
print("=" * 50)

while True:
    numero = int(input("Introduce un numero para repasar su tabla: "))
    fallos = 0

    multiplicador = 1
    while multiplicador <= 10:
        respuesta = int(input(f"{numero} x {multiplicador} = "))
        resultado_correcto = numero * multiplicador

        if respuesta == resultado_correcto:
            print("Correcto!")
        else:
            fallos = fallos + 1
            print(f"Incorrecto. La respuesta correcta es {resultado_correcto}")

        multiplicador = multiplicador + 1

    print(f"Has tenido {fallos} fallos en la tabla del {numero}")

    respuesta = input("Quieres repasar otra tabla? (S/N): ")
    if respuesta.upper() == "N":
        break


# ------------------------------------------------------------
# EJERCICIO 9
# Modificar el ejercicio 8: si tenemos mas de 2 fallos,
# hay que repetir la tabla de multiplicar.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 9 -- Repetir tabla si mas de 2 fallos")
print("=" * 50)

while True:
    numero = int(input("Introduce un numero para repasar su tabla: "))

    while True:    # bucle interno: repite la tabla si hay mas de 2 fallos
        fallos = 0

        multiplicador = 1
        while multiplicador <= 10:
            respuesta = int(input(f"{numero} x {multiplicador} = "))
            resultado_correcto = numero * multiplicador

            if respuesta == resultado_correcto:
                print("Correcto!")
            else:
                fallos = fallos + 1
                print(f"Incorrecto. La respuesta correcta es {resultado_correcto}")

            multiplicador = multiplicador + 1

        print(f"Has tenido {fallos} fallos")

        if fallos > 2:
            print("Mas de 2 fallos. Debes repetir la tabla.")
        else:
            print("Tabla superada!")
            break    # salimos del bucle interno

    respuesta = input("Quieres repasar otra tabla? (S/N): ")
    if respuesta.upper() == "N":
        break


# ------------------------------------------------------------
# EJERCICIO 10
# El ordenador obtiene un numero aleatorio entre 1 y 100.
# El usuario tiene que adivinarlo.
# El ordenador indica si el numero es mayor, menor o correcto.
# Repetir hasta que acierte.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 10 -- Adivina el numero")
print("=" * 50)

numero_secreto = random.randint(1, 100)
intentos       = 0

print("He pensado un numero entre 1 y 100. Adivina cual es!")

while True:
    intento  = int(input("Tu numero: "))
    intentos = intentos + 1

    if intento == numero_secreto:
        print(f"CORRECTO! Lo has adivinado en {intentos} intentos.")
        break
    elif intento < numero_secreto:
        print("El numero a adivinar es MAYOR")
    else:
        print("El numero a adivinar es MENOR")


# ------------------------------------------------------------
# EJERCICIO 11
# Pasar un numero decimal positivo a su representacion en binario.
# Algoritmo: dividir entre 2 sucesivamente y recoger los restos
# en orden inverso.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 11 -- Decimal a binario")
print("=" * 50)

numero = int(input("Introduce un numero decimal positivo: "))

if numero == 0:
    print("El numero en binario es: 0")
else:
    restos = []
    n      = numero

    while n > 0:
        resto = n % 2
        restos.append(str(resto))
        n     = n // 2

    # Los restos se leen en orden inverso
    binario = ""
    i = len(restos) - 1
    while i >= 0:
        binario = binario + restos[i]
        i = i - 1

    print(f"{numero} en binario es: {binario}")


# ------------------------------------------------------------
# EJERCICIO 12
# Pide limite inferior y superior de un intervalo.
# Si el inferior es mayor que el superior, volver a pedir.
# Introduce numeros hasta que se introduzca el 0. Al final:
#   - Suma de numeros dentro del intervalo (intervalo abierto)
#   - Cuantos numeros estan fuera del intervalo
#   - Si algun numero coincide con los limites
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 12 -- Numeros en un intervalo")
print("=" * 50)

# Pedir el intervalo hasta que sea valido
while True:
    limite_inf = float(input("Introduce el limite inferior del intervalo: "))
    limite_sup = float(input("Introduce el limite superior del intervalo: "))

    if limite_inf < limite_sup:
        break
    else:
        print("Error: el limite inferior debe ser menor que el superior.")

suma_dentro     = 0.0
fuera_contador  = 0
toco_limite     = False

print(f"Intervalo: ({limite_inf}, {limite_sup}) -- introduce numeros, 0 para terminar")

while True:
    numero = float(input("Numero: "))

    if numero == 0:
        break

    if numero == limite_inf or numero == limite_sup:
        toco_limite = True
        print("Ese numero coincide con un limite del intervalo")
    elif numero > limite_inf and numero < limite_sup:
        suma_dentro = suma_dentro + numero
        print("Numero dentro del intervalo")
    else:
        fuera_contador = fuera_contador + 1
        print("Numero fuera del intervalo")

print(f"\nSuma de numeros dentro del intervalo : {suma_dentro}")
print(f"Numeros fuera del intervalo          : {fuera_contador}")
if toco_limite:
    print("Se ha introducido algun numero igual a los limites del intervalo")
else:
    print("Ningun numero coincidio con los limites del intervalo")


# ------------------------------------------------------------
# EJERCICIO 13
# Dados un numero real (base) y un entero positivo (exponente),
# calcular la potencia SIN usar el operador de potencia.
# Algoritmo: multiplicar la base por si misma "exponente" veces.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 13 -- Potencia sin operador **")
print("=" * 50)

base      = float(input("Introduce la base (numero real): "))
exponente = int(input("Introduce el exponente (entero positivo): "))

if exponente < 0:
    print("El exponente debe ser un entero positivo")
else:
    resultado = 1.0
    i         = 0
    while i < exponente:
        resultado = resultado * base
        i         = i + 1

    print(f"{base} elevado a {exponente} = {resultado}")


# ------------------------------------------------------------
# EJERCICIO 14
# Menu de opciones. El usuario elige hasta que selecciona Salir.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 14 -- Menu de opciones")
print("=" * 50)

while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1. Opcion A")
    print("2. Opcion B")
    print("3. Opcion C")
    print("4. Salir")

    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        print("Has elegido la Opcion A")
    elif opcion == 2:
        print("Has elegido la Opcion B")
    elif opcion == 3:
        print("Has elegido la Opcion C")
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida. Elige entre 1 y 4.")


# ------------------------------------------------------------
# EJERCICIO 15
# Introducir un numero y mostrar si es primo o no.
# Un numero es primo si solo es divisible por 1 y por si mismo.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 15 -- Numero primo")
print("=" * 50)

numero = int(input("Introduce un numero entero: "))

if numero < 2:
    print(f"{numero} NO es primo")
else:
    es_primo  = True
    divisor   = 2

    while divisor <= numero - 1:
        if numero % divisor == 0:
            es_primo = False
            break        # ya sabemos que no es primo, no hace falta seguir
        divisor = divisor + 1

    if es_primo:
        print(f"{numero} ES primo")
    else:
        print(f"{numero} NO es primo (es divisible entre {divisor})")


# ------------------------------------------------------------
# EJERCICIO 16
# Mostrar en pantalla los N primeros numeros primos.
# N lo pide el usuario por teclado.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 16 -- N primeros numeros primos")
print("=" * 50)

N             = int(input("Cuantos numeros primos quieres mostrar: "))
primos_encontrados = 0
candidato     = 2     # empezamos buscando desde el 2

while primos_encontrados < N:

    # Comprobar si candidato es primo
    es_primo = True
    divisor  = 2

    while divisor <= candidato - 1:
        if candidato % divisor == 0:
            es_primo = False
            break
        divisor = divisor + 1

    if es_primo:
        primos_encontrados = primos_encontrados + 1
        print(f"Primo {primos_encontrados}: {candidato}")

    candidato = candidato + 1
