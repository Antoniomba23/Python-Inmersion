# ============================================================
#   REPASO PYTHON — ÍNDICE GENERAL
#  Preparación de examen — Lucas
# ============================================================
#
#   ESTRUCTURA DE ARCHIVOS
#  ├── tema_01_variables_y_tipos.py
#  ├── tema_02_condicionales.py
#  ├── tema_03_bucles.py
#  ├── tema_04_listas_y_tuplas.py
#  ├── tema_05_diccionarios_y_sets.py
#  ├── tema_06_funciones.py
#  ├── tema_07_excepciones.py
#  ├── tema_08_archivos.py
#  ├── tema_09_POO_clases.py
#  ├── tema_10_modulos.py
#  └── simulacro_final.py
#
# ============================================================

# ============================================================
#   RESUMEN ULTRA-RÁPIDO — Lo más importante de cada tema
# ============================================================

# TEMA 1 — Variables
# ─────────────────
# str / int / float / bool / None
# casting: str() int() float()     ️ int("3.9") → ERROR
# f-string: f"Hola {variable}"
# comparación devuelve bool: aprobado = nota >= 5  (no pongas = True)

# TEMA 2 — Condicionales
# ──────────────────────
# if / elif / else
# ️ hora >= 6 and hora <= 11  (no: and <= 11)
# forma pythónica: 6 <= hora <= 11
# ternario: resultado = "Sí" if condicion else "No"

# TEMA 3 — Bucles
# ───────────────
# for i in range(inicio, fin, paso):   fin EXCLUIDO
# enumerate(lista) → índice + valor
# zip(l1, l2)      → dos listas a la vez
# while True + break → patrón clásico
# break / continue / pass
# FizzBuzz: el caso combinado SIEMPRE va primero
# comprehension: [expr for x in lista if condicion]

# TEMA 4 — Listas y Tuplas
# ────────────────────────
# lista[-1] → último   lista[::-1] → invertir
# append / insert / extend / remove / pop / clear
# sort() modifica original   sorted() devuelve nueva ️
# ️ no machaques: num = len(lista), no lista = len(lista)
# tupla → inmutable, unpacking: a, b = (1, 2)
# swap: a, b = b, a

# TEMA 5 — Diccionarios y Sets
# ────────────────────────────
# d["clave"] → KeyError si no existe
# d.get("clave", default) → seguro 
# for k, v in d.items() → recorrer ambos 
# max(d, key=d.get) → clave con valor máximo
# set → sin duplicados: list(set(lista))
# a | b  a & b  a - b → operaciones de conjuntos

# TEMA 6 — Funciones
# ──────────────────
# def f(oblig, opcional=0, *args, **kwargs)
# return a, b → tupla → a, b = f()
# sin return → None
# lambda x: x**2 → función anónima
# lista.sort(key=lambda x: x[1]) → uso típico
# evitar global, mejor pasar parámetros

# TEMA 7 — Excepciones
# ────────────────────
# try / except / else / finally
# ValueError / TypeError / ZeroDivisionError / IndexError / KeyError
# FileNotFoundError
# raise ValueError("mensaje") → lanzar propia
# while True + try/except + break → validar input 

# TEMA 8 — Archivos
# ─────────────────
# with open("f.txt", modo) as f:   → siempre with 
# "r" leer  "w" escribir  "a" añadir
# f.read() / for linea in f: / f.write()
# linea.strip().split(",") → patrón CSV 
# import csv + DictReader/DictWriter

# TEMA 9 — POO
# ────────────
# class / __init__ / self
# __str__ → print(obj)  __len__ → len(obj)  __eq__ → ==
# herencia: class Hijo(Padre): + super().__init__()
# isinstance(obj, Clase) → True/False
# self.__privado → atributo privado

# TEMA 10 — Módulos
# ─────────────────
# import math / random / datetime / os
# math.sqrt() ceil() floor() pi
# random.randint(a,b) choice() shuffle() sample()
# datetime.now().strftime("%d/%m/%Y %H:%M")
# os.path.exists() getcwd() listdir()
# if __name__ == "__main__": → solo ejecuta directamente 

# ============================================================
#  ️  ERRORES CLÁSICOS DE EXAMEN
# ============================================================
"""
1.  int("3.9")              → ERROR, usar int(float("3.9"))
2.  hora >= 6 and <= 11     → ERROR, repetir variable
3.  numero %3 = 0           → ERROR, usar == no =
4.  for i range(lista):     → ERROR, falta "in"
5.  FizzBuzz sin orden      → el caso combinado SIEMPRE primero
6.  aprobados = len(lista)  → machacas la lista, usar num_aprobados
7.  lista.sort() en vez de sorted() cuando no quieres modificar original
8.  dict["clave"] sin .get()→ KeyError si no existe
9.  __init__ sin self        → TypeError
10. open() sin with          → posible pérdida de datos
"""
