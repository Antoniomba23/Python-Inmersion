# ============================================================
#  PRACTICA 2.2 -- ALGORITMOS SECUENCIALES
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 1
# Capturar el nombre de un alumno y las calificaciones de tres
# evaluaciones. Calcular y mostrar su nota media final del
# siguiente modo: "La nota media de <nombre> es <nota>"
# ------------------------------------------------------------
print("=" * 50)
print("EJERCICIO 1 -- Nota media de un alumno")
print("=" * 50)

nombre = input("Introduce el nombre del alumno: ")
nota1  = float(input("Nota de la primera evaluacion: "))
nota2  = float(input("Nota de la segunda evaluacion: "))
nota3  = float(input("Nota de la tercera evaluacion: "))

media = (nota1 + nota2 + nota3) / 3

print(f"La nota media de {nombre} es {media:.2f}")


# ------------------------------------------------------------
# EJERCICIO 2
# Capturar el nombre de una persona y su sueldo bruto.
# Calcular el sueldo neto descontando:
#   - IRPF: 12%
#   - Seguridad Social: 5.20%
# Mostrar: "El sueldo neto de XXXX es XXXX euros"
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 2 -- Calculo del sueldo neto")
print("=" * 50)

nombre      = input("Introduce el nombre de la persona: ")
sueldo_bruto = float(input("Introduce el sueldo bruto: "))

descuento_irpf = sueldo_bruto * 12 / 100
descuento_ss   = sueldo_bruto * 5.20 / 100
sueldo_neto    = sueldo_bruto - descuento_irpf - descuento_ss

print(f"\nSueldo bruto      : {sueldo_bruto:.2f} euros")
print(f"Descuento IRPF    : {descuento_irpf:.2f} euros (12%)")
print(f"Descuento SS      : {descuento_ss:.2f} euros (5.20%)")
print(f"El sueldo neto de {nombre} es {sueldo_neto:.2f} euros")


# ------------------------------------------------------------
# EJERCICIO 3
# Crear un algoritmo que escriba "Hola" cinco veces.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 3 -- Hola cinco veces")
print("=" * 50)

contador = 1
while contador <= 5:
    print("Hola")
    contador = contador + 1


# ------------------------------------------------------------
# EJERCICIO 4
# Crear un algoritmo que pida al usuario 5 datos y muestre
# su suma.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 4 -- Suma de 5 datos")
print("=" * 50)

suma = 0
i    = 1
while i <= 5:
    dato = float(input(f"Introduce el dato {i}: "))
    suma = suma + dato
    i    = i + 1

print(f"La suma de los 5 datos es: {suma}")


# ------------------------------------------------------------
# EJERCICIO 5
# Calcular la raiz cuadrada del numero que introduzca el usuario.
# Comprobar que pasa si introduce un numero negativo.
# (En la 2.2 solo mostramos lo que pasa, sin bucle de repeticion.
#  El bucle se anade en la practica 3.2)
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 5 -- Raiz cuadrada")
print("=" * 50)

import math

numero = float(input("Introduce un numero: "))

if numero < 0:
    print("Error: no se puede calcular la raiz cuadrada de un numero negativo")
else:
    raiz = math.sqrt(numero)
    print(f"La raiz cuadrada de {numero} es {raiz:.4f}")


# ------------------------------------------------------------
# EJERCICIO 6
# Emitir la factura de una compra:
#   - Se pide nombre del articulo, precio unitario y nº de unidades
#   - IVA del 19%
#   - Mostrar: precio venta, IVA, precio bruto y precio final
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 6 -- Factura de compra")
print("=" * 50)

articulo      = input("Nombre del articulo: ")
precio_unit   = float(input("Precio unitario (EUR): "))
unidades      = int(input("Numero de unidades: "))

precio_venta  = precio_unit * unidades
iva_importe   = precio_venta * 19 / 100
precio_bruto  = precio_venta           # precio antes de IVA
precio_final  = precio_venta + iva_importe

print(f"\n--- FACTURA: {articulo} ---")
print(f"Precio unitario   : {precio_unit:.2f} EUR")
print(f"Unidades          : {unidades}")
print(f"Precio de venta   : {precio_venta:.2f} EUR")
print(f"IVA (19%)         : {iva_importe:.2f} EUR")
print(f"Precio bruto      : {precio_bruto:.2f} EUR")
print(f"PRECIO FINAL      : {precio_final:.2f} EUR")


# ------------------------------------------------------------
# EJERCICIO 7
# Resolver una ecuacion de segundo grado: ax^2 + bx + c = 0
# A partir de sus coeficientes a, b, c.
# Discriminante D = b^2 - 4ac
#   D > 0 --> dos soluciones reales
#   D = 0 --> una solucion real (doble)
#   D < 0 --> no hay soluciones reales
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 7 -- Ecuacion de segundo grado")
print("=" * 50)

a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el coeficiente c: "))

if a == 0:
    print("El coeficiente 'a' no puede ser 0 (no seria de segundo grado)")
else:
    discriminante = b ** 2 - 4 * a * c

    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        print(f"Dos soluciones reales: x1 = {x1:.4f}  x2 = {x2:.4f}")
    elif discriminante == 0:
        x = -b / (2 * a)
        print(f"Una solucion real doble: x = {x:.4f}")
    else:
        print("No hay soluciones reales (discriminante negativo)")


# ------------------------------------------------------------
# EJERCICIO 8
# Dada una cantidad en pies, convertirla a:
#   pulgadas, yardas, metros y millas.
# Equivalencias:
#   1 milla   = 1609 metros
#   1 pulgada = 0.0254 metros
#   1 yarda   = 3 pies
#   1 pie     = 12 pulgadas
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 8 -- Conversion de unidades desde pies")
print("=" * 50)

pies = float(input("Introduce la cantidad en pies: "))

pulgadas = pies * 12
yardas   = pies / 3
metros   = pulgadas * 0.0254
millas   = metros / 1609

print(f"\n{pies} pies equivalen a:")
print(f"  {pulgadas:.4f} pulgadas")
print(f"  {yardas:.4f} yardas")
print(f"  {metros:.4f} metros")
print(f"  {millas:.6f} millas")


# ------------------------------------------------------------
# EJERCICIO 9
# Pide al usuario 2 numeros y muestra la "distancia entre ellos"
# (el valor absoluto de su diferencia).
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 9 -- Distancia entre dos numeros")
print("=" * 50)

a = float(input("Introduce el primer numero: "))
b = float(input("Introduce el segundo numero: "))

diferencia = a - b
if diferencia < 0:
    diferencia = diferencia * -1    # valor absoluto manual

print(f"La distancia entre {a} y {b} es {diferencia}")


# ------------------------------------------------------------
# EJERCICIO 10
# Capturar un numero de dos cifras y mostrar el numero invertido.
# Para invertirlo hay que obtener las decenas y las unidades
# por separado.
# Ejemplo: 47 --> invertido es 74
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 10 -- Numero de dos cifras invertido")
print("=" * 50)

numero = int(input("Introduce un numero de dos cifras: "))

decenas  = numero // 10    # parte entera de la division entre 10
unidades = numero % 10     # resto de la division entre 10

invertido = unidades * 10 + decenas

print(f"Numero original : {numero}")
print(f"Numero invertido: {invertido}")


# ------------------------------------------------------------
# EJERCICIO 11
# Capturar dos numeros A y B e intercambiar sus valores.
# Mostrar al final el valor de cada variable.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 11 -- Intercambio de variables")
print("=" * 50)

a = float(input("Introduce el valor de A: "))
b = float(input("Introduce el valor de B: "))

print(f"\nAntes del intercambio: A = {a}  B = {b}")

# Intercambio usando una variable temporal
temporal = a
a        = b
b        = temporal

print(f"Despues del intercambio: A = {a}  B = {b}")


# ------------------------------------------------------------
# EJERCICIO 12
# Recibe una cantidad de minutos y muestra cuantas horas
# y minutos son.
# Ejemplo: 130 minutos --> 2 horas y 10 minutos
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 12 -- Minutos a horas y minutos")
print("=" * 50)

total_minutos = int(input("Introduce la cantidad de minutos: "))

horas   = total_minutos // 60    # division entera: cuantas horas completas
minutos = total_minutos % 60     # resto: minutos que sobran

print(f"{total_minutos} minutos son {horas} horas y {minutos} minutos")


# ------------------------------------------------------------
# EJERCICIO 13
# Un ciclista parte de ciudad A a las HH:MM:SS.
# El viaje dura T segundos. Calcular la hora de llegada a ciudad B.
# Sugerencia: convertir la hora de salida a segundos, sumar T,
# y volver a convertir a HH:MM:SS.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 13 -- Hora de llegada del ciclista")
print("=" * 50)

hh = int(input("Hora de salida - horas: "))
mm = int(input("Hora de salida - minutos: "))
ss = int(input("Hora de salida - segundos: "))
t  = int(input("Duracion del viaje en segundos: "))

# Convertir hora de salida a segundos totales del dia
salida_segundos = hh * 3600 + mm * 60 + ss

# Sumar el tiempo de viaje
llegada_segundos = salida_segundos + t

# Manejar el caso de que se pase de medianoche (86400 segundos en un dia)
llegada_segundos = llegada_segundos % 86400

# Convertir de vuelta a HH:MM:SS
hh_llegada = llegada_segundos // 3600
resto      = llegada_segundos % 3600
mm_llegada = resto // 60
ss_llegada = resto % 60

print(f"Hora de salida  : {hh:02d}:{mm:02d}:{ss:02d}")
print(f"Duracion viaje  : {t} segundos")
print(f"Hora de llegada : {hh_llegada:02d}:{mm_llegada:02d}:{ss_llegada:02d}")


# ------------------------------------------------------------
# EJERCICIO 14
# Pedir nombre y dos apellidos de una persona y mostrar
# sus iniciales separadas por puntos.
# Ejemplo: Lucas Garcia Lopez --> L.G.L.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 14 -- Iniciales de una persona")
print("=" * 50)

nombre    = input("Introduce el nombre: ")
apellido1 = input("Introduce el primer apellido: ")
apellido2 = input("Introduce el segundo apellido: ")

inicial_nombre    = nombre[0].upper()
inicial_apellido1 = apellido1[0].upper()
inicial_apellido2 = apellido2[0].upper()

iniciales = inicial_nombre + "." + inicial_apellido1 + "." + inicial_apellido2 + "."

print(f"Iniciales: {iniciales}")


# ------------------------------------------------------------
# EJERCICIO 15
# Calcular la nota final de un estudiante en un test:
#   - Cada respuesta correcta vale 1 punto
#   - Cada respuesta incorrecta resta 0.25 puntos
#   - Las respuestas en blanco valen 0
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 15 -- Nota de un test")
print("=" * 50)

correctas   = int(input("Numero de respuestas correctas: "))
incorrectas = int(input("Numero de respuestas incorrectas: "))
en_blanco   = int(input("Numero de respuestas en blanco: "))

nota = correctas * 1 + incorrectas * (-0.25) + en_blanco * 0

print(f"\nCorrectas   : {correctas} x  1.00 = {correctas:.2f}")
print(f"Incorrectas : {incorrectas} x -0.25 = {incorrectas * -0.25:.2f}")
print(f"En blanco   : {en_blanco} x  0.00 = 0.00")
print(f"NOTA FINAL  : {nota:.2f}")


# ------------------------------------------------------------
# EJERCICIO 16
# Calcular el dinero total en euros y centimos a partir de
# cuantas monedas tiene el usuario de cada tipo:
#   2 euros, 1 euro, 50 cts, 20 cts, 10 cts
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 16 -- Total de monedas")
print("=" * 50)

monedas_2eur  = int(input("Monedas de 2 euros: "))
monedas_1eur  = int(input("Monedas de 1 euro: "))
monedas_50cts = int(input("Monedas de 50 centimos: "))
monedas_20cts = int(input("Monedas de 20 centimos: "))
monedas_10cts = int(input("Monedas de 10 centimos: "))

# Calculamos el total en centimos para evitar errores con decimales
total_centimos  = (monedas_2eur  * 200
                 + monedas_1eur  * 100
                 + monedas_50cts * 50
                 + monedas_20cts * 20
                 + monedas_10cts * 10)

euros    = total_centimos // 100
centimos = total_centimos % 100

print(f"\nTotal: {euros} euros y {centimos} centimos")
print(f"       ({total_centimos} centimos en total)")


# ------------------------------------------------------------
# EJERCICIO 17
# Calculo de la calificacion final de un alumno en Algoritmos:
#   55% del promedio de tres calificaciones parciales
#   30% de la calificacion del examen final
#   15% de la calificacion del trabajo final
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 17 -- Calificacion final en Algoritmos")
print("=" * 50)

parcial1       = float(input("Nota del primer parcial: "))
parcial2       = float(input("Nota del segundo parcial: "))
parcial3       = float(input("Nota del tercer parcial: "))
examen_final   = float(input("Nota del examen final: "))
trabajo_final  = float(input("Nota del trabajo final: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

aportacion_parciales = promedio_parciales * 55 / 100
aportacion_examen    = examen_final       * 30 / 100
aportacion_trabajo   = trabajo_final      * 15 / 100

nota_final = aportacion_parciales + aportacion_examen + aportacion_trabajo

print(f"\nPromedio parciales : {promedio_parciales:.2f}  x 55% = {aportacion_parciales:.2f}")
print(f"Examen final       : {examen_final:.2f}          x 30% = {aportacion_examen:.2f}")
print(f"Trabajo final      : {trabajo_final:.2f}          x 15% = {aportacion_trabajo:.2f}")
print(f"CALIFICACION FINAL : {nota_final:.2f}")
