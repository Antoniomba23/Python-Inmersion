# ============================================================
#  TEMA 2 — CONDICIONALES: Inmersión Completa
# ============================================================

# ------------------------------------------------------------
# 1. ESTRUCTURA BÁSICA
# ------------------------------------------------------------

nota = 7.8

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")        # ← esta se ejecuta
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")

# ️ Python evalúa los elif EN ORDEN y ejecuta solo el primero True
# El else es opcional, pero si está, siempre va al final

# ------------------------------------------------------------
# 2. OPERADORES DE COMPARACIÓN
# ------------------------------------------------------------

x = 10

print(x == 10)    # True   → igual que
print(x != 5)     # True   → distinto de
print(x > 5)      # True   → mayor que
print(x >= 10)    # True   → mayor o igual
print(x < 20)     # True   → menor que
print(x <= 10)    # True   → menor o igual

# is vs == (importante para examen)
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
print(lista1 == lista2)   # True  → mismo CONTENIDO
print(lista1 is lista2)   # False → distinto OBJETO en memoria

# Para None SIEMPRE usar is/is not
valor = None
print(valor is None)       #  correcto
print(valor is not None)   #  correcto
print(valor == None)       # ️ funciona pero no es pythónico

# ------------------------------------------------------------
# 3. OPERADORES LÓGICOS: and / or / not
# ------------------------------------------------------------

edad      = 20
tiene_dni = True
saldo     = 150

# and → ambas condiciones deben ser True
if edad >= 18 and tiene_dni:
    print("Puede votar")

# or → basta con que una sea True
if saldo >= 100 or tiene_dni:
    print("Puede continuar")

# not → invierte el valor booleano
if not tiene_dni:
    print("Necesitas DNI")

# Combinados con paréntesis para mayor claridad
hora = 14
if (hora >= 9 and hora <= 14) or (hora >= 16 and hora <= 20):
    print("Horario de atención")

# ️ TRAMPA CLÁSICA — siempre repetir la variable
#  if hora >= 9 and <= 14:    → SyntaxError
#  if hora >= 9 and hora <= 14:

# ------------------------------------------------------------
# 4. COMPARACIÓN ENCADENADA (exclusiva de Python) 
# ------------------------------------------------------------

nota = 7.8

# Forma normal
if nota >= 7 and nota < 9:
    print("Notable")

# Forma pythónica → más legible
if 7 <= nota < 9:
    print("Notable")

# Clasificación de notas con encadenado
if 9 <= nota <= 10:
    print("Sobresaliente")
elif 7 <= nota < 9:
    print("Notable")
elif 5 <= nota < 7:
    print("Aprobado")
elif 0 <= nota < 5:
    print("Suspenso")

# ------------------------------------------------------------
# 5. VALORES TRUTHY Y FALSY EN CONDICIONALES
# ------------------------------------------------------------

# No siempre necesitas == True o == False
notas = [7.8, 5.0, 4.5]
nombre = "Lucas"
valor = None

# FALSY → evalúan como False (no necesitas == False)
if not notas:        print("Lista vacía")      # lista vacía
if not nombre:       print("Sin nombre")        # string vacío
if valor is None:    print("Sin valor")         # None

# TRUTHY → evalúan como True (no necesitas == True)
if notas:            print("Hay notas")         # lista con elementos
if nombre:           print("Hay nombre")        # string no vacío

# Comparación compacta
aprobado = nota >= 5
if aprobado:                    #  más limpio
    print("Aprobado")
if aprobado == True:            # ️ redundante pero funciona
    print("Aprobado")

# ------------------------------------------------------------
# 6. OPERADOR TERNARIO (condicional en una línea)
# ------------------------------------------------------------

nota = 7.8

# Forma básica
resultado = "Aprobado" if nota >= 5 else "Suspenso"
print(resultado)   # "Aprobado"

# Con f-string
print(f"Estado: {'' if nota >= 5 else ''}")

# Ternario anidado (usar con moderacion)
nivel = "Alto" if nota >= 9 else ("Medio" if nota >= 5 else "Bajo")

# Ternario dentro de un bucle normal
notas = [4.5, 7.8, 9.2, 3.0]
estados = []
for n in notas:
    estados.append("Aprobado" if n >= 5 else "Suspenso")
print(estados)   # ['Suspenso', 'Aprobado', 'Aprobado', 'Suspenso']

# ------------------------------------------------------------
# 7. MATCH-CASE (Python 3.10+, equivalente a switch)
# ------------------------------------------------------------

dia = "lunes"

match dia:
    case "lunes" | "martes" | "miércoles" | "jueves" | "viernes":
        print("Día laborable")
    case "sábado" | "domingo":
        print("Fin de semana")
    case _:                        # _ → caso por defecto (como else)
        print("Día no reconocido")

# Con valores numéricos
codigo = 404
match codigo:
    case 200:
        print("OK")
    case 404:
        print("No encontrado")   # ← esta se ejecuta
    case 500:
        print("Error del servidor")
    case _:
        print("Código desconocido")

# ------------------------------------------------------------
# 8. CONDICIONALES CON IN Y NOT IN
# ------------------------------------------------------------

frutas       = ["manzana", "pera", "uva"]
vocales      = "aeiou"
codigos_validos = {100, 200, 300}

# in → comprobar si un elemento está en una colección
fruta = "pera"
if fruta in frutas:
    print(f"{fruta} está en la lista")

letra = "a"
if letra in vocales:
    print(f"{letra} es vocal")

codigo = 200
if codigo in codigos_validos:
    print("Código válido")

# not in → comprobar que NO está
if "kiwi" not in frutas:
    print("No tenemos kiwi")

# ------------------------------------------------------------
# 9. CONDICIONALES ANIDADOS
# ------------------------------------------------------------

edad   = 20
saldo  = 50
es_vip = True

# Anidado simple
if edad >= 18:
    if saldo >= 100:
        print("Puede comprar")
    else:
        print("Saldo insuficiente")
else:
    print("Menor de edad")

# Mejor con and (más limpio)
if edad >= 18 and saldo >= 100:
    print("Puede comprar")
elif edad >= 18:
    print("Saldo insuficiente")
else:
    print("Menor de edad")

# Con prioridades combinadas
if edad >= 18 and (saldo >= 100 or es_vip):
    print("Acceso concedido")

# ------------------------------------------------------------
# 10. CASOS PRÁCTICOS TÍPICOS DE EXAMEN
# ------------------------------------------------------------

# Clasificador de temperatura
temp = 25
if temp < 0:
    clima = "Bajo cero"
elif temp < 10:
    clima = "Frío"
elif temp < 20:
    clima = "Fresco"
elif temp < 30:
    clima = "Agradable"    # ← esta se ejecuta
else:
    clima = "Caluroso"
print(clima)

# Calculadora con condicionales
def calcular(a, operador, b):
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        if b == 0:
            return "Error: división por cero"
        return a / b
    else:
        return "Operador no reconocido"

print(calcular(10, "+", 5))   # 15
print(calcular(10, "/", 0))   # "Error: división por cero"
print(calcular(10, "?", 5))   # "Operador no reconocido"

# IMC (Índice de Masa Corporal) — ejercicio tipo examen
def clasificar_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 25:
        categoria = "Normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"
    return round(imc, 2), categoria

imc, cat = clasificar_imc(70, 1.75)
print(f"IMC: {imc} → {cat}")   # IMC: 22.86 → Normal

# ============================================================
#  HOJA DE TRUCOS — TEMA 2
# ============================================================
"""
ESTRUCTURA
    if condicion:
        ...
    elif otra_condicion:
        ...
    else:
        ...

OPERADORES
    ==  !=  >  <  >=  <=
    and  or  not
    in   not in

️ SIEMPRE repetir la variable en cada comparación
    hora >= 6 and hora <= 11    
    hora >= 6 and <= 11          SyntaxError

ENCADENADO (solo Python)
    6 <= hora <= 11              muy limpio

is vs ==
    ==   compara contenido
    is   compara identidad (mismo objeto)
    → siempre: valor is None   (nunca: valor == None)

FALSY (evalúan False en condicionales)
    0  0.0  ""  []  {}  None
    → if not lista: ...   ← más pythónico que if len(lista) == 0

TERNARIO
    resultado = "Si" if condicion else "No"

in / not in
    "a" in "hola"       → True
    3 in [1, 2, 3]      → True
    "x" not in "hola"   → True

MATCH-CASE (Python 3.10+)
    match variable:
        case valor1 | valor2:
            ...
        case _:            → como else
            ...

BUENAS PRÁCTICAS
     if lista:           (no: if len(lista) > 0)
     if valor is None:   (no: if valor == None)
     if aprobado:        (no: if aprobado == True)
"""
