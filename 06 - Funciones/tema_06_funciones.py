# ============================================================
#  TEMA 6 — FUNCIONES
# ============================================================

# ------------------------------------------------------------
# 1. ANATOMÍA DE UNA FUNCIÓN
# ------------------------------------------------------------

def calcular_media(notas, redondear=2):   # redondear tiene valor por defecto
    """
    Calcula la media de una lista de notas.   ← docstring
    """
    if len(notas) == 0:
        return 0                   # return sale de la función inmediatamente
    media = sum(notas) / len(notas)
    return round(media, redondear)

# Llamadas
notas = [7.8, 9.2, 5.0]
print(calcular_media(notas))       # 7.33  (redondear=2 por defecto)
print(calcular_media(notas, 0))    # 7.0

# ------------------------------------------------------------
# 2. TIPOS DE PARÁMETROS
# ------------------------------------------------------------

# Parámetros obligatorios
def saludar(nombre, edad):
    print(f"Hola {nombre}, tienes {edad} años")

saludar("Lucas", 20)    # 
# saludar("Lucas")      #  TypeError: falta "edad"

# Parámetros con valor por defecto
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

saludar("Lucas")                # "Hola, Lucas!"
saludar("Lucas", "Buenos días") # "Buenos días, Lucas!"

# Argumentos por nombre (el orden no importa) 
def registrar(nombre, edad, ciudad):
    print(f"{nombre}, {edad} años, {ciudad}")

registrar(edad=20, ciudad="Madrid", nombre="Lucas")

# *args → número variable de argumentos (llegan como tupla)
def sumar(*numeros):
    return sum(numeros)

print(sumar(1, 2, 3))        # 6
print(sumar(1, 2, 3, 4, 5))  # 15

# **kwargs → argumentos nombrados variables (llegan como diccionario)
def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_datos(nombre="Lucas", edad=20, ciudad="Madrid")

# ------------------------------------------------------------
# 3. RETURN — TODO LO QUE NECESITAS
# ------------------------------------------------------------

# Devolver múltiples valores (devuelve una tupla)
def minmax(lista):
    return min(lista), max(lista)

minimo, maximo = minmax([3, 1, 9, 4])   # unpacking directo 
print(minimo)   # 1
print(maximo)   # 9

# Sin return → devuelve None implícitamente
def imprimir(texto):
    print(texto)

resultado = imprimir("Hola")
print(resultado)   # None

# Return como salida anticipada
def dividir(a, b):
    if b == 0:
        return None     # sale antes si hay error
    return a / b

# ------------------------------------------------------------
# 4. SCOPE — DÓNDE VIVEN LAS VARIABLES
# ------------------------------------------------------------

total = 100             # variable GLOBAL

def mostrar():
    print(total)        #  puede LEER variables globales

def modificar():
    global total        # ️ necesitas declararlo para MODIFICARLO
    total = 200

# Variable LOCAL → solo existe dentro de la función
def calcular():
    resultado = 42
    return resultado

# print(resultado)    #  NameError — no existe fuera

#  Regla de oro: evita global, mejor pasar datos como parámetros

# ------------------------------------------------------------
# 5. FUNCIONES LAMBDA (anónimas)
# ------------------------------------------------------------

cuadrado = lambda n: n ** 2
print(cuadrado(5))    # 25

# Uso típico: como argumento de sorted() 
alumnos = [("Lucas", 7.8), ("Ana", 9.2), ("Pedro", 4.5)]
alumnos.sort(key=lambda alumno: alumno[1])
# [("Pedro", 4.5), ("Lucas", 7.8), ("Ana", 9.2)]

ranking = sorted(alumnos, key=lambda a: a[1], reverse=True)

# ------------------------------------------------------------
# 6. FUNCIONES QUE LLAMAN A OTRAS
# ------------------------------------------------------------

def es_aprobado(nota):
    return nota >= 5

def evaluar_clase(notas):
    aprobados = []
    suspensos = []
    for n in notas:
        if es_aprobado(n):
            aprobados.append(n)
        else:
            suspensos.append(n)
    return {
        "media"    : round(sum(notas) / len(notas), 2),
        "aprobados": len(aprobados),
        "suspensos": len(suspensos),
        "max"      : max(notas),
        "min"      : min(notas)
    }

notas   = [4.5, 7.8, 9.2, 3.0, 5.5, 8.1]
informe = evaluar_clase(notas)

for clave, valor in informe.items():
    print(f"{clave}: {valor}")

# ============================================================
#  HOJA DE TRUCOS — TEMA 6
# ============================================================
"""
DEFINIR
    def nombre(param1, param2="default"):
        return resultado

TIPOS DE PARÁMETROS
    def f(obligatorio, opcional=0, *args, **kwargs)

LLAMAR
    f(1, 2)                     → posicional
    f(param2=2, param1=1)       → por nombre (orden libre) 

RETURN
    return valor                → devuelve y sale
    return a, b                 → devuelve tupla → a, b = f()
    (sin return)                → devuelve None

SCOPE
    global variable             → para modificar global ️

LAMBDA
    lambda x: x ** 2            → función anónima
    lista.sort(key=lambda x: x[1])  → uso típico

BUENAS PRÁCTICAS
     Una función → una tarea
     Nombres descriptivos: calcular_media() no cm()
     Parámetros en vez de variables globales
"""
