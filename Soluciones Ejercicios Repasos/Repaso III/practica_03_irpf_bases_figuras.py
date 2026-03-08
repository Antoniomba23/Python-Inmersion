# ============================================================
#  PRACTICA 3 -- IRPF, CONVERSION DE BASES Y FIGURAS
#  (traducida a Python desde enunciado Java)
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 1 -- Impuesto sobre la renta (IRPF)
#
# Deducciones por hijos PRIMERO:
#   0 hijos  --> 0% de deduccion
#   1 o 2    --> 5% de deduccion
#   mas de 2 --> 15% de deduccion
#
# Tipo impositivo sobre salario TRAS deduccion:
#   < 20.000       --> 15%
#   >= 20.000 y < 30.000 --> 18%
#   >= 30.000      --> 25%
#
# El programa pregunta S/N para continuar
# ------------------------------------------------------------
print("=" * 40)
print("EJERCICIO 1 -- Calculo del IRPF")
print("=" * 40)

while True:
    salario_bruto = float(input("\nIntroduce el salario anual bruto (EUR): "))
    num_hijos     = int(input("Numero de hijos: "))

    # Calcular porcentaje de deduccion por hijos
    if num_hijos == 0:
        porcentaje_deduccion = 0
    elif num_hijos == 1 or num_hijos == 2:
        porcentaje_deduccion = 5
    else:
        porcentaje_deduccion = 15

    # Aplicar deduccion al salario bruto
    deduccion       = salario_bruto * porcentaje_deduccion / 100
    salario_neto    = salario_bruto - deduccion

    # Calcular tipo impositivo sobre el salario ya deducido
    if salario_neto < 20000:
        tipo_impositivo = 15
    elif salario_neto < 30000:
        tipo_impositivo = 18
    else:
        tipo_impositivo = 25

    # Calcular el impuesto
    impuesto = salario_neto * tipo_impositivo / 100

    # Mostrar resultado
    print("\n--- CALCULO IRPF ---")
    print(f"Salario bruto          : {salario_bruto:.2f} EUR")
    print(f"Deduccion por hijos    : {porcentaje_deduccion}% = {deduccion:.2f} EUR")
    print(f"Salario tras deduccion : {salario_neto:.2f} EUR")
    print(f"Tipo impositivo        : {tipo_impositivo}%")
    print(f"IMPUESTO A PAGAR       : {impuesto:.2f} EUR")
    print(f"Salario final neto     : {salario_bruto - impuesto:.2f} EUR")

    # Preguntar si continuar
    respuesta = input("\nDesea continuar con otro caso? (S/N): ")
    if respuesta.upper() == "N":
        print("Fin del programa.")
        break


# ------------------------------------------------------------
# EJERCICIO 2 -- Conversion de base decimal a binario, octal o base 5
#
# El algoritmo de conversion: dividir sucesivamente entre la base
# y recoger los restos en orden inverso
# Ejemplo decimal 13 a binario:
#   13 / 2 = 6  resto 1
#    6 / 2 = 3  resto 0
#    3 / 2 = 1  resto 1
#    1 / 2 = 0  resto 1
#   Resultado (restos al reves): 1101
# ------------------------------------------------------------
print("\n" + "=" * 40)
print("EJERCICIO 2 -- Conversion de bases")
print("=" * 40)

def convertir_a_base(numero, base):
    """Convierte un numero decimal a la base indicada.
    Devuelve el resultado como string."""
    if numero == 0:
        return "0"

    digitos = []        # aqui guardamos los restos
    n = numero

    while n > 0:
        resto = n % base
        digitos.append(str(resto))
        n = n // base   # division entera, descartamos el resto

    # Los restos se recogen en orden inverso
    resultado = ""
    i = len(digitos) - 1
    while i >= 0:
        resultado = resultado + digitos[i]
        i = i - 1

    return resultado


while True:
    numero = int(input("\nIntroduce un numero en decimal: "))

    print("Elige la base de conversion:")
    print("  1 -- Binario (base 2)")
    print("  2 -- Octal (base 8)")
    print("  3 -- Base 5")

    opcion = int(input("Tu eleccion (1/2/3): "))

    if opcion == 1:
        base       = 2
        nombre     = "binario"
    elif opcion == 2:
        base       = 8
        nombre     = "octal"
    elif opcion == 3:
        base       = 5
        nombre     = "base 5"
    else:
        print("Opcion no valida.")
        continue

    resultado = convertir_a_base(numero, base)
    print(f"{numero} en {nombre} es: {resultado}")

    respuesta = input("Desea continuar? (S/N): ")
    if respuesta.upper() == "N":
        print("Fin del programa.")
        break


# ------------------------------------------------------------
# EJERCICIO 3 -- Cuadrado hueco en pantalla
#
# Ejemplo con lado = 5:
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
#
# Logica:
#   - Primera y ultima fila: imprimir el simbolo en todas las columnas
#   - Filas intermedias: solo imprimir en la primera y ultima columna
# ------------------------------------------------------------
print("\n" + "=" * 40)
print("EJERCICIO 3 -- Cuadrado hueco")
print("=" * 40)

lado   = int(input("Introduce la longitud del lado: "))
simbolo = "*"      # puedes cambiarlo por otro caracter ASCII

# Recorremos cada fila
fila = 1
while fila <= lado:

    # Recorremos cada columna de la fila
    linea    = ""
    columna  = 1

    while columna <= lado:

        # Primera fila o ultima fila --> todo simbolos
        if fila == 1 or fila == lado:
            linea = linea + simbolo + " "

        # Filas intermedias --> solo primera y ultima columna
        else:
            if columna == 1 or columna == lado:
                linea = linea + simbolo + " "
            else:
                linea = linea + "  "    # espacio hueco

        columna = columna + 1

    print(linea)
    fila = fila + 1

# Salida para lado = 5:
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
