# ============================================================
#  TEMA 3 — BUCLES for / while
# ============================================================

# ------------------------------------------------------------
# 1. BUCLE for — cuando sabes cuántas veces iterar
# ------------------------------------------------------------

# Iterar una lista
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)

# range(inicio, fin, paso) — fin es EXCLUIDO
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)

for i in range(10, 0, -1):  # 10, 9, 8... 1 (cuenta atrás)
    print(i)

# enumerate() → índice + valor
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")  # 0: manzana / 1: pera / 2: uva

# zip() → dos listas a la vez
nombres = ["Lucas", "Ana"]
notas   = [7.8, 9.2]
for nombre, nota in zip(nombres, notas):
    print(f"{nombre} → {nota}")

# Iterar un string letra a letra
for letra in "Python":
    print(letra)   # P, y, t, h, o, n

# ------------------------------------------------------------
# 2. BUCLE while — mientras se cumpla una condición
# ------------------------------------------------------------

contador = 0
while contador < 5:
    print(contador)
    contador += 1       # ️ sin esto → bucle infinito

# Patrón clásico: bucle hasta que el usuario diga stop
while True:
    entrada = input("Escribe algo (q para salir): ")
    if entrada == "q":
        break
    print(f"Dijiste: {entrada}")

# while con else (poco conocido, sale en examen)
intentos = 0
while intentos < 3:
    print(f"Intento {intentos}")
    intentos += 1
else:
    print("Bucle terminado sin break")  # se ejecuta si no hubo break

# ------------------------------------------------------------
# 3. break / continue / pass
# ------------------------------------------------------------

# break → sale del bucle completamente
for i in range(10):
    if i == 5:
        break
    print(i)     # 0, 1, 2, 3, 4

# continue → salta esta iteración, sigue el bucle
for i in range(6):
    if i == 3:
        continue
    print(i)     # 0, 1, 2, 4, 5  (el 3 se salta)

# pass → no hace nada, marcador de sitio
for i in range(5):
    if i == 2:
        pass     # aquí pondremos algo luego
    print(i)     # imprime todo normal

# ------------------------------------------------------------
# 4. BUCLES ANIDADOS
# ------------------------------------------------------------

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")

# ------------------------------------------------------------
# 5. FIZZBUZZ (ejercicio clásico de examen)
# ------------------------------------------------------------

# ️ El caso combinado (FizzBuzz) SIEMPRE va primero
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:   # primero el más restrictivo
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# ------------------------------------------------------------
# 6. LIST COMPREHENSION (forma pythónica)
# ------------------------------------------------------------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cuadrados = [n**2 for n in numeros]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

pares = [n for n in numeros if n % 2 == 0]
# [2, 4, 6, 8, 10]

resultado = ["par" if n % 2 == 0 else "impar" for n in numeros]

# ============================================================
#  HOJA DE TRUCOS — TEMA 3
# ============================================================
"""
FOR
    for i in range(inicio, fin, paso):   # fin excluido
    for i, v in enumerate(lista):        # índice + valor
    for a, b in zip(lista1, lista2):     # dos listas

WHILE
    while condicion:    # ️ actualiza la variable o bucle infinito
    while True: ... break               # patrón clásico

CONTROL
    break      → sale del bucle
    continue   → salta a la siguiente iteración
    pass       → no hace nada

COMPREHENSION
    [expresion for x in iterable if condicion]

% MÓDULO
    x % 2 == 0  → par
    x % 3 == 0  → divisible por 3
"""
