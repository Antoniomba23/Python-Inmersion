# ============================================================
#  PRACTICA 8.2 -- EJERCICIOS CON VECTORES (LISTAS) II
# ============================================================

import random


# ------------------------------------------------------------
# EJERCICIO 1
# Rellenar 4 boletos de la bonoloto.
# Cada boleto tiene 6 numeros entre 1 y 49.
# No se pueden repetir los numeros en una misma apuesta.
# Visualizar las cuatro apuestas.
# ------------------------------------------------------------
print("=" * 50)
print("EJERCICIO 1 -- 4 boletos de bonoloto")
print("=" * 50)

NUM_BOLETOS  = 4
NUMS_BOLETO  = 6
MIN_NUM      = 1
MAX_NUM      = 49

boletos = []    # lista de boletos (cada boleto es una lista de 6 numeros)

boleto_num = 0
while boleto_num < NUM_BOLETOS:
    print(f"\n--- Boleto {boleto_num + 1} ---")
    boleto = []

    while len(boleto) < NUMS_BOLETO:
        numero = int(input(f"  Numero {len(boleto) + 1} (1-49): "))

        # Validar rango
        if numero < MIN_NUM or numero > MAX_NUM:
            print(f"  Error: el numero debe estar entre {MIN_NUM} y {MAX_NUM}")
            continue

        # Comprobar que no se repite en este boleto
        repetido = False
        i        = 0
        while i < len(boleto):
            if boleto[i] == numero:
                repetido = True
                break
            i = i + 1

        if repetido:
            print(f"  Error: el {numero} ya esta en este boleto")
        else:
            boleto.append(numero)

    boletos.append(boleto)
    boleto_num = boleto_num + 1

# Mostrar las cuatro apuestas
print("\n--- TUS APUESTAS ---")
i = 0
while i < len(boletos):
    print(f"Boleto {i + 1}: {boletos[i]}")
    i = i + 1


# ------------------------------------------------------------
# EJERCICIO 2
# Maquina automatica de venta de bebidas.
# Productos:
#   1. Agua    --> 0.50 EUR
#   2. Refresco --> 0.75 EUR
#   3. Zumo    --> 0.95 EUR
#   4. Salir
#
# Monedas aceptadas (en centimos): 5, 10, 20, 50, 100, 200
# (NO acepta 1 ni 2 centimos)
# Al inicio la maquina tiene 20 monedas de cada tipo.
# Dar el cambio con el minimo numero de monedas posible.
# Si quedan menos de 2 tipos de moneda (o menos de 1 si es la de 5),
# mostrar "INTRODUZCA IMPORTE EXACTO" y solo aceptar el precio exacto.
# Al salir, mostrar el total de dinero por tipo de moneda.
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 2 -- Maquina de venta de bebidas")
print("=" * 50)

# Precios en centimos para evitar errores con decimales
PRECIO_AGUA      = 50    # 0.50 EUR
PRECIO_REFRESCO  = 75    # 0.75 EUR
PRECIO_ZUMO      = 95    # 0.95 EUR

# Monedas disponibles: [5cts, 10cts, 20cts, 50cts, 1eur, 2eur]
# En centimos:         [5,    10,    20,    50,    100,  200 ]
TIPOS_MONEDAS    = [5, 10, 20, 50, 100, 200]
NOMBRES_MONEDAS  = ["5cts", "10cts", "20cts", "50cts", "1EUR", "2EUR"]

# La maquina empieza con 20 monedas de cada tipo
monedas_maquina = [20, 20, 20, 20, 20, 20]

def tipos_disponibles(monedas):
    """Cuenta cuantos tipos de moneda quedan en la maquina."""
    tipos = 0
    i     = 0
    while i < len(monedas):
        if monedas[i] > 0:
            tipos = tipos + 1
        i = i + 1
    return tipos

def tiene_moneda_5(monedas):
    """Comprueba si quedan monedas de 5 centimos."""
    return monedas[0] > 0

def dar_cambio(cambio_centimos, monedas):
    """
    Da el cambio usando el minimo numero de monedas posible.
    Devuelve True si pudo dar el cambio, False si no pudo.
    Modifica la lista monedas si tiene exito.
    """
    cambio_restante = cambio_centimos
    monedas_usadas  = [0, 0, 0, 0, 0, 0]

    # Recorremos desde la moneda mayor a la menor (indice 5 a 0)
    i = len(TIPOS_MONEDAS) - 1
    while i >= 0 and cambio_restante > 0:
        valor = TIPOS_MONEDAS[i]
        while cambio_restante >= valor and monedas[i] > 0:
            monedas_usadas[i] = monedas_usadas[i] + 1
            cambio_restante   = cambio_restante - valor
        i = i - 1

    if cambio_restante > 0:
        return False    # No se pudo dar el cambio exacto

    # Aplicar el cambio a las monedas de la maquina
    i = 0
    while i < len(monedas):
        monedas[i] = monedas[i] - monedas_usadas[i]
        i = i + 1

    # Mostrar el desglose del cambio
    print("  Cambio entregado:")
    i = len(TIPOS_MONEDAS) - 1
    while i >= 0:
        if monedas_usadas[i] > 0:
            print(f"    {monedas_usadas[i]} moneda(s) de {NOMBRES_MONEDAS[i]}")
        i = i - 1

    return True


# Bucle principal de la maquina
while True:
    print("\n--- MENU ---")
    print(f"1. Agua       {PRECIO_AGUA / 100:.2f} EUR")
    print(f"2. Refresco   {PRECIO_REFRESCO / 100:.2f} EUR")
    print(f"3. Zumo       {PRECIO_ZUMO / 100:.2f} EUR")
    print("4. Salir")

    opcion = int(input("Elige una opcion: "))

    if opcion == 4:
        break

    if opcion == 1:
        precio      = PRECIO_AGUA
        nombre_prod = "Agua"
    elif opcion == 2:
        precio      = PRECIO_REFRESCO
        nombre_prod = "Refresco"
    elif opcion == 3:
        precio      = PRECIO_ZUMO
        nombre_prod = "Zumo"
    else:
        print("Opcion no valida")
        continue

    # Comprobar si hay suficientes monedas para dar cambio
    tipos   = tipos_disponibles(monedas_maquina)
    hay_5   = tiene_moneda_5(monedas_maquina)

    if tipos < 2 or (tipos == 1 and not hay_5):
        solo_exacto = True
        print("INTRODUZCA IMPORTE EXACTO")
    else:
        solo_exacto = False

    # Pedir el dinero introducido
    print(f"Precio: {precio / 100:.2f} EUR")

    while True:
        print("Introduce monedas (5, 10, 20, 50, 100, 200 centimos; 0 para cancelar):")
        total_introducido = 0

        while total_introducido < precio:
            moneda = int(input(f"  Moneda (faltan {(precio - total_introducido) / 100:.2f} EUR): "))

            if moneda == 0:
                print("Compra cancelada")
                break

            if moneda not in TIPOS_MONEDAS:
                print("  Moneda no aceptada")
                continue

            total_introducido = total_introducido + moneda

        if moneda == 0:
            break

        cambio = total_introducido - precio

        if solo_exacto and cambio != 0:
            print("Solo se acepta importe exacto. Devolviendo monedas...")
            continue

        # Intentar dar el cambio
        if cambio == 0:
            print(f"Gracias! Disfruta tu {nombre_prod}. Sin cambio.")
            # Guardar las monedas introducidas en la maquina
            i = 0
            while i < len(TIPOS_MONEDAS):
                if TIPOS_MONEDAS[i] == moneda:
                    monedas_maquina[i] = monedas_maquina[i] + 1
                i = i + 1
            break
        else:
            print(f"Cambio a devolver: {cambio / 100:.2f} EUR")
            exito = dar_cambio(cambio, monedas_maquina)
            if exito:
                print(f"Gracias! Disfruta tu {nombre_prod}.")
                break
            else:
                print("No tenemos cambio exacto. Por favor introduzca importe mas exacto.")

# Resumen final de dinero en la maquina
print("\n--- DINERO EN LA MAQUINA AL CIERRE ---")
i = 0
while i < len(TIPOS_MONEDAS):
    total_tipo = TIPOS_MONEDAS[i] * monedas_maquina[i]
    print(f"  {NOMBRES_MONEDAS[i]:6s}: {monedas_maquina[i]:3d} monedas = {total_tipo / 100:.2f} EUR")
    i = i + 1
