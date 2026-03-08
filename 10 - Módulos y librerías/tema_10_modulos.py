# ============================================================
#  TEMA 10 — MÓDULOS Y LIBRERÍAS
# ============================================================

# ------------------------------------------------------------
# 1. TIPOS DE MÓDULOS
# ------------------------------------------------------------

# 1. Biblioteca estándar → vienen con Python
import math
import random
import os
import datetime

# 2. Módulos de terceros → se instalan con pip
# import requests       # pip install requests
# import pandas         # pip install pandas

# 3. Módulos propios → archivos .py que tú creas
# import mi_modulo      # mi_modulo.py en la misma carpeta

# ------------------------------------------------------------
# 2. FORMAS DE IMPORTAR
# ------------------------------------------------------------

# import completo → accedes con nombre.funcion
import math
print(math.sqrt(25))    # 5.0
print(math.pi)          # 3.14159...

# from ... import → importas solo lo que necesitas
from math import sqrt, pi
print(sqrt(25))         # 5.0  (sin "math.")
print(pi)               # 3.14159...

# alias con as → nombre más corto
import datetime as dt
import math as m
print(m.sqrt(25))       # 5.0

# importar todo (️ evitar en producción)
# from math import *    # puede causar conflictos de nombres

# ------------------------------------------------------------
# 3. MÓDULO math
# ------------------------------------------------------------

import math

print(math.sqrt(16))       # 4.0      → raíz cuadrada
print(math.pow(2, 10))     # 1024.0   → potencia (devuelve float)
print(2 ** 10)             # 1024     → potencia con operador (devuelve int)
print(math.pi)             # 3.14159  → constante π
print(math.e)              # 2.71828  → constante e
print(math.ceil(4.2))      # 5        → redondear arriba
print(math.floor(4.9))     # 4        → redondear abajo
print(math.factorial(5))   # 120
print(math.log(100, 10))   # 2.0      → logaritmo base 10
print(abs(-5))             # 5        → ️ abs() es builtin, NO math.abs()

# ------------------------------------------------------------
# 4. MÓDULO random
# ------------------------------------------------------------

import random

print(random.random())              # float entre 0.0 y 1.0
print(random.randint(1, 10))        # entero entre 1 y 10 (ambos incluidos) 
print(random.uniform(0, 10))        # float entre 0.0 y 10.0
print(random.choice([1,2,3,4,5]))   # elemento aleatorio de una lista

lista = [1, 2, 3, 4, 5]
random.shuffle(lista)               # mezcla la lista in-place ️ modifica original
print(lista)

print(random.sample([1,2,3,4,5], 3))  # 3 elementos sin repetición → nueva lista

# Semilla → resultados reproducibles
random.seed(42)
print(random.randint(1, 100))       # siempre el mismo con seed 42

# Generar lista de notas aleatorias con 1 decimal
notas = []
for _ in range(10):
    nota = round(random.uniform(0, 10), 1)
    notas.append(nota)
print(notas)

# ------------------------------------------------------------
# 5. MÓDULO datetime
# ------------------------------------------------------------

from datetime import datetime, date, timedelta

# Fecha y hora actual
ahora = datetime.now()
print(ahora)                              # 2026-03-08 10:30:45.123456

# Solo fecha actual
hoy = date.today()
print(hoy)                                # 2026-03-08

# Crear fecha concreta
cumple = date(1995, 6, 20)

# Formatear fechas 
print(ahora.strftime("%d/%m/%Y"))         # "08/03/2026"
print(ahora.strftime("%d/%m/%Y %H:%M"))   # "08/03/2026 10:30"
print(ahora.strftime("%A, %d de %B"))     # "Sunday, 08 de March"

# Operaciones con fechas
manana = hoy + timedelta(days=1)
semana = hoy + timedelta(weeks=1)

# Diferencia entre fechas
nacimiento = date(2004, 3, 15)
edad_dias  = (hoy - nacimiento).days
print(f"Llevas {edad_dias} días vivo")

# ------------------------------------------------------------
# 6. MÓDULO os
# ------------------------------------------------------------

import os

print(os.getcwd())                       # directorio actual
print(os.listdir("."))                   # lista archivos del directorio
print(os.path.exists("alumnos.txt"))     # True/False → ¿existe? 
ruta = os.path.join("carpeta", "archivo.txt")  # une rutas correctamente

# os.mkdir("nueva_carpeta")             # crear carpeta
# os.remove("archivo.txt")             # eliminar archivo

# ------------------------------------------------------------
# 7. CREAR TU PROPIO MÓDULO
# ------------------------------------------------------------

# ── archivo: calculadora.py ──────────────────────
# def sumar(a, b):
#     return a + b
#
# def restar(a, b):
#     return a - b
#
# PI = 3.14159
#
# if __name__ == "__main__":
#     print("Probando calculadora...")
#     print(sumar(3, 5))       # solo al ejecutar directamente

# ── archivo: main.py ─────────────────────────────
# import calculadora
# print(calculadora.sumar(3, 5))    # 8
# print(calculadora.PI)             # 3.14159

# ------------------------------------------------------------
# 8. if __name__ == "__main__" (MUY DE EXAMEN)
# ------------------------------------------------------------

def saludar(nombre):
    return f"Hola, {nombre}!"

# Este bloque SOLO se ejecuta si corres este archivo directamente
# NO se ejecuta si lo importas desde otro archivo 
if __name__ == "__main__":
    print(saludar("Lucas"))

# Cuando haces "import modulo" desde otro archivo,
# el bloque if __name__ == "__main__" NO se ejecuta 

# ------------------------------------------------------------
# 9. EJEMPLO COMPLETO — Informe con 3 módulos
# ------------------------------------------------------------

import random
import math
from datetime import datetime

notas = []
for _ in range(10):
    nota = round(random.uniform(0, 10), 1)
    notas.append(nota)

media    = sum(notas) / len(notas)

# Calcular varianza con bucle explicito
suma_diferencias = 0
for x in notas:
    suma_diferencias += (x - media) ** 2
varianza = suma_diferencias / len(notas)

desv_std = math.sqrt(varianza)
fecha    = datetime.now().strftime("%d/%m/%Y a las %H:%M:%S")

print("=" * 40)
print(f"  INFORME DE NOTAS")
print(f"  Generado el {fecha}")
print("=" * 40)
print(f"  Notas    : {notas}")
print(f"  Media    : {media:.2f}")
print(f"  Máxima   : {max(notas)}")
print(f"  Mínima   : {min(notas)}")
print(f"  Desv. std: {desv_std:.2f}")
print("=" * 40)

# ============================================================
#  HOJA DE TRUCOS — TEMA 10
# ============================================================
"""
IMPORTAR
    import modulo
    import modulo as alias
    from modulo import funcion, CONSTANTE
    from modulo import *               → ️ evitar

MATH
    math.sqrt(x)   math.pi    math.ceil(x)   math.floor(x)
    math.pow(x,y)  math.factorial(x)
    abs(-5)        → ️ builtin, no math.abs()

RANDOM
    random.randint(a, b)         → entero aleatorio [a, b]
    random.uniform(a, b)         → float aleatorio [a, b]
    random.choice(lista)         → elemento aleatorio
    random.shuffle(lista)        → mezcla in-place ️
    random.sample(lista, n)      → n elementos sin repetir

DATETIME
    datetime.now()               → fecha y hora actual
    date.today()                 → solo fecha
    timedelta(days=n)            → sumar/restar días
    fecha.strftime("%d/%m/%Y")   → formatear

OS
    os.path.exists("ruta")       → comprobar si existe 
    os.getcwd()                  → directorio actual
    os.listdir(".")              → listar archivos

MÓDULO PROPIO
    if __name__ == "__main__":   → solo se ejecuta directamente 
"""
