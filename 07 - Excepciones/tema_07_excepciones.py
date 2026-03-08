# ============================================================
#  TEMA 7 — EXCEPCIONES try / except
# ============================================================

# ------------------------------------------------------------
# 1. ESTRUCTURA COMPLETA
# ------------------------------------------------------------

try:
    resultado = 10 / 0

except ZeroDivisionError:
    print("No se puede dividir entre cero")

except ValueError:
    print("Valor incorrecto")

except Exception as e:           # captura CUALQUIER otro error
    print(f"Error inesperado: {e}")

else:
    # se ejecuta SOLO si NO hubo ningún error 
    print(f"Todo fue bien: {resultado}")

finally:
    # se ejecuta SIEMPRE, haya error o no
    print("Esto siempre se imprime")

# ------------------------------------------------------------
# 2. ERRORES MÁS COMUNES
# ------------------------------------------------------------

# ValueError → tipo correcto pero valor inválido
# int("hola")               
# int("42")                 

# TypeError → operación entre tipos incompatibles
# "edad: " + 20             
# "edad: " + str(20)        

# ZeroDivisionError → división entre cero
# 10 / 0                    

# IndexError → índice fuera de rango
# lista = [1, 2, 3]
# lista[10]                 

# KeyError → clave que no existe en diccionario
# d = {"nombre": "Lucas"}
# d["edad"]                 
# d.get("edad", "N/A")       forma segura

# FileNotFoundError → archivo que no existe
# open("archivo_inexistente.txt")   

# NameError → variable que no existe
# print(variable_no_declarada)      

# ------------------------------------------------------------
# 3. PATRÓN CLÁSICO — validar entrada del usuario
# ------------------------------------------------------------

def pedir_numero(mensaje):
    while True:                      # repite hasta que el usuario acierte
        try:
            numero = float(input(mensaje))
            return numero            # si llega aquí, todo fue bien
        except ValueError:
            print("️ Introduce un número válido, por favor")

# edad = pedir_numero("¿Cuántos años tienes? ")
# Patrón: while True + try/except + return → muy de examen 

# ------------------------------------------------------------
# 4. LANZAR TUS PROPIAS EXCEPCIONES
# ------------------------------------------------------------

def calcular_media(notas):
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacia")
    for n in notas:
        if n < 0 or n > 10:
            raise ValueError("Las notas deben estar entre 0 y 10")
    return sum(notas) / len(notas)

try:
    media = calcular_media([])
except ValueError as e:
    print(f"Error: {e}")    # "Error: La lista de notas no puede estar vacía"

# ------------------------------------------------------------
# 5. EXCEPCIONES EN FUNCIONES
# ------------------------------------------------------------

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None             # devuelve None en vez de explotar


def procesar_operaciones(operaciones):
    resultados = []
    for a, b in operaciones:
        resultado = dividir(a, b)
        if resultado is None:
            print(f"️ {a}/{b} → división por cero, se ignora")
        else:
            resultados.append(resultado)
    return resultados


ops = [(10, 2), (8, 0), (15, 3), (7, 0)]
print(procesar_operaciones(ops))
# ️ 8/0 → división por cero, se ignora
# ️ 7/0 → división por cero, se ignora
# [5.0, 5.0]

# ------------------------------------------------------------
# 6. CONVERTIR VALORES DE FORMA SEGURA
# ------------------------------------------------------------

def convertir_a_entero(valor):
    try:
        return int(valor)
    except ValueError:
        print(f"Error: '{valor}' no es un número entero válido")
        return None
    except TypeError:
        print("Error: tipo de dato no compatible")
        return None

valores = [42, "15", "3.14", "hola", None, "99"]
for v in valores:
    resultado = convertir_a_entero(v)
    if resultado is not None:
        print(f"{str(v):>6} → {resultado}")

# ============================================================
#  HOJA DE TRUCOS — TEMA 7
# ============================================================
"""
ESTRUCTURA COMPLETA
    try:
        ...                    → código que puede fallar
    except TipoError:
        ...                    → gestión del error concreto
    except Exception as e:
        print(e)               → cualquier otro error
    else:
        ...                    → solo si NO hubo error
    finally:
        ...                    → SIEMPRE se ejecuta

ERRORES FRECUENTES
    ValueError        → valor inválido      int("hola")
    TypeError         → tipo incorrecto     "a" + 1
    ZeroDivisionError → /0                  10/0
    IndexError        → índice fuera        lista[99]
    KeyError          → clave inexistente   dict["x"]
    FileNotFoundError → archivo ausente     open("x.txt")

LANZAR ERROR PROPIO
    raise ValueError("mensaje descriptivo")

PATRÓN CLÁSICO (muy de examen)
    while True:
        try:
            x = int(input("..."))
            break                  → sale si todo fue bien
        except ValueError:
            print("Inténtalo de nuevo")
"""
