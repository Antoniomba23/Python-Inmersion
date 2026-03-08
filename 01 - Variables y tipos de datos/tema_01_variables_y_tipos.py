# ============================================================
#  TEMA 1 — VARIABLES Y TIPOS DE DATOS: Inmersión Completa
# ============================================================

# ------------------------------------------------------------
# 1. TIPOS FUNDAMENTALES
# ------------------------------------------------------------

nombre    = "Lucas"      # str       → texto
edad      = 20           # int       → entero
nota      = 7.8          # float     → decimal
aprobado  = True         # bool      → True / False
sin_valor = None         # NoneType  → ausencia de valor

# Ver el tipo de cualquier variable
print(type(nombre))      # <class 'str'>
print(type(edad))        # <class 'int'>
print(type(nota))        # <class 'float'>
print(type(aprobado))    # <class 'bool'>
print(type(sin_valor))   # <class 'NoneType'>

# ------------------------------------------------------------
# 2. STRINGS — Todo lo que necesitas saber
# ------------------------------------------------------------

texto = "Hola, mundo"

# LONGITUD
print(len(texto))           # 11

# INDEXING Y SLICING (igual que listas)
print(texto[0])             # "H"
print(texto[-1])            # "o"
print(texto[0:4])           # "Hola"
print(texto[::-1])          # "odnum ,aloH"  ← invertir string

# MÉTODOS DE STRING más usados en examen
nombre = "  lucas garcía  "

print(nombre.strip())            # "lucas garcía"     → quita espacios extremos
print(nombre.lstrip())           # "lucas garcía  "   → solo izquierda
print(nombre.rstrip())           # "  lucas garcía"   → solo derecha

print(nombre.strip().upper())    # "LUCAS GARCÍA"     → todo mayúsculas
print(nombre.strip().lower())    # "lucas garcía"     → todo minúsculas
print(nombre.strip().title())    # "Lucas García"     → capitaliza cada palabra
print(nombre.strip().capitalize()) # "Lucas garcía"   → solo primera letra

frase = "Python es genial"
print(frase.replace("genial", "increíble"))  # "Python es increíble"
print(frase.split(" "))    # ["Python", "es", "genial"] → divide en lista
print(frase.split("e"))    # ["Python ", "s g", "nial"] → divide por "e"
print(frase.startswith("Python"))   # True
print(frase.endswith("genial"))     # True
print(frase.count("e"))             # 2  → cuántas veces aparece
print(frase.find("es"))             # 7  → posición (o -1 si no existe)
print(frase.index("es"))            # 7  → posición (ValueError si no existe)
print("es" in frase)                # True → ¿está la subcadena?

# UNIR listas en string
palabras = ["Python", "es", "genial"]
print(" ".join(palabras))    # "Python es genial"  
print("-".join(palabras))    # "Python-es-genial"

# STRIP de caracteres concretos
codigo = "###error###"
print(codigo.strip("#"))     # "error"

# COMPROBAR CONTENIDO
print("123".isdigit())       # True  → ¿solo dígitos?
print("abc".isalpha())       # True  → ¿solo letras?
print("abc123".isalnum())    # True  → ¿letras y números?
print("  ".isspace())        # True  → ¿solo espacios?

# ------------------------------------------------------------
# 3. TIPOS NUMÉRICOS — int y float en detalle
# ------------------------------------------------------------

# OPERADORES ARITMÉTICOS
print(10 + 3)    # 13    suma
print(10 - 3)    # 7     resta
print(10 * 3)    # 30    multiplicación
print(10 / 3)    # 3.33  división (SIEMPRE devuelve float)
print(10 // 3)   # 3     división entera (trunca)
print(10 % 3)    # 1     módulo (resto de la división)
print(10 ** 3)   # 1000  potencia

# REDONDEO
print(round(3.14159, 2))   # 3.14  → redondea a 2 decimales
print(round(7.8456, 1))    # 7.8

# NÚMEROS GRANDES (Python no tiene límite de tamaño)
grande = 1_000_000_000     # puedes usar _ como separador visual
print(grande)              # 1000000000

# FLOATS — precaución con decimales ️
print(0.1 + 0.2)           # 0.30000000000000004  ← imprecisión float
print(round(0.1 + 0.2, 1)) # 0.3   redondear para comparar

# ------------------------------------------------------------
# 4. BOOLEANOS — más de lo que parece
# ------------------------------------------------------------

print(True + True)    # 2  → bool hereda de int, True=1, False=0
print(True * 5)       # 5
print(False + 1)      # 1

# Valores "FALSY" → se evalúan como False en condicionales ️
print(bool(0))        # False
print(bool(0.0))      # False
print(bool(""))       # False  → string vacío
print(bool([]  ))     # False  → lista vacía
print(bool({} ))      # False  → dict vacío
print(bool(None))     # False

# Valores "TRUTHY" → todo lo demás es True
print(bool(1))        # True
print(bool(-1))       # True   ← cualquier número no cero
print(bool("hola"))   # True
print(bool([0]))      # True   ← lista con elementos (aunque sean 0)

# Uso práctico: comprobar si una lista está vacía
notas = []
if not notas:                    # más pythónico que: if len(notas) == 0
    print("No hay notas")

# Comparación con None
valor = None
if valor is None:    #  forma correcta
    print("Sin valor")
if valor == None:    # ️ funciona pero no es pythónico

# ------------------------------------------------------------
# 5. CASTING — conversión entre tipos
# ------------------------------------------------------------

# str → otros tipos
print(int("42"))         # 42
print(float("3.14"))     # 3.14
print(bool("hola"))      # True   (cualquier string no vacío)
print(bool(""))          # False

# int → otros tipos
print(str(42))           # "42"
print(float(42))         # 42.0
print(bool(0))           # False
print(bool(1))           # True

# float → otros tipos
print(int(7.9))          # 7    ️ TRUNCA, no redondea
print(int(-3.9))         # -3   ️ trunca hacia cero
print(str(3.14))         # "3.14"

# TRAMPAS de examen 
# int("3.9")           → ValueError  
# int(float("3.9"))    → 3            primero float, luego int
# int("hola")          → ValueError  
# float("hola")        → ValueError  
# int(True)            → 1           
# int(False)           → 0           
# int(None)            → TypeError   

# ------------------------------------------------------------
# 6. F-STRINGS — todas las formas
# ------------------------------------------------------------

nombre = "Lucas"
nota   = 7.8456
pi     = 3.14159265

# Básico
print(f"Hola, {nombre}")                  # "Hola, Lucas"

# Expresiones dentro
print(f"El doble de la nota: {nota * 2}") # "El doble de la nota: 15.6912"

# Formato numérico
print(f"{nota:.2f}")          # "7.85"      → 2 decimales (redondea)
print(f"{nota:.0f}")          # "8"         → sin decimales
print(f"{pi:.4f}")            # "3.1416"    → 4 decimales
print(f"{1000000:,}")         # "1,000,000" → separador de miles
print(f"{0.456:.1%}")         # "45.6%"     → porcentaje

# Alineación y relleno
print(f"{'izquierda':<20}")   # "izquierda           "  → izquierda
print(f"{'derecha':>20}")     # "           derecha"    → derecha
print(f"{'centro':^20}")      # "       centro       "  → centrar
print(f"{'texto':*^20}")      # "*******texto********"  → rellenar con *

# Números con relleno de ceros
print(f"{42:05d}")            # "00042"  → rellena con ceros

# Condicional dentro del f-string
print(f"Estado: {' Aprobado' if nota >= 5 else ' Suspenso'}")

# ------------------------------------------------------------
# 7. MÚLTIPLES ASIGNACIONES
# ------------------------------------------------------------

# Asignación múltiple al mismo valor
a = b = c = 0
print(a, b, c)   # 0 0 0

# Asignación desempaquetada
x, y, z = 1, 2, 3
print(x, y, z)   # 1 2 3

# Swap sin variable temporal 
a, b = 10, 20
a, b = b, a
print(a, b)      # 20 10

# Ignorar valores con _
primero, _, ultimo = (1, 2, 3)
print(primero, ultimo)   # 1 3

# ------------------------------------------------------------
# 8. OPERADORES DE COMPARACIÓN
# ------------------------------------------------------------

nota = 7.8

print(nota == 7.8)    # True   → igual
print(nota != 5)      # True   → distinto
print(nota > 5)       # True   → mayor que
print(nota >= 5)      # True   → mayor o igual
print(nota < 10)      # True   → menor que
print(nota <= 9)      # True   → menor o igual

# Comparación encadenada (exclusiva de Python) 
print(5 <= nota <= 10)   # True → más limpio que: nota >= 5 and nota <= 10

# Operadores lógicos
print(True and False)    # False
print(True or False)     # True
print(not True)          # False

# Comparación de tipos: is vs ==
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)    # True  → mismo contenido
print(a is b)    # False → distinto objeto en memoria
print(a is None) # False

# ============================================================
#  HOJA DE TRUCOS — TEMA 1
# ============================================================
"""
TIPOS
    str / int / float / bool / None
    type(x)                  → ver el tipo

STRINGS MÁS USADOS
    s.strip()                → quita espacios/\n
    s.upper() / s.lower()    → mayúsculas/minúsculas
    s.title() / s.capitalize()
    s.split(",")             → dividir en lista
    ",".join(lista)          → unir lista en string 
    s.replace(viejo, nuevo)
    s.startswith(x) / s.endswith(x)
    s.count(x)               → cuántas veces aparece
    s.find(x)                → posición o -1
    x in s                   → True/False

NÚMEROS
    /    → float siempre
    //   → división entera
    %    → módulo (resto)
    **   → potencia
    round(x, n)              → n decimales

️ FLOATS
    0.1 + 0.2 ≠ 0.3  → usar round() para comparar

CASTING
    int("42")   float("3.14")   str(x)
    ️ int("3.9")           → ValueError 
     int(float("3.9"))    → 3

FALSY (evalúan como False)
    0  0.0  ""  []  {}  None

F-STRING
    f"{x}"          → básico
    f"{x:.2f}"      → 2 decimales
    f"{x:,}"        → separador miles
    f"{x:.1%}"      → porcentaje
    f"{'txt':>10}"  → alineación derecha

ASIGNACIÓN
    a, b = b, a     → swap sin variable temporal 
    x, _, z = tupla → ignorar valores con _

COMPARACIÓN ENCADENADA
    5 <= nota <= 10     solo Python

is vs ==
    == compara CONTENIDO
    is compara IDENTIDAD (mismo objeto)
    → usar siempre is None, nunca == None
"""
