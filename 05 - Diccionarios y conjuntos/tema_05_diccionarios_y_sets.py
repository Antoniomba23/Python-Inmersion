# ============================================================
#  TEMA 5 — DICCIONARIOS Y CONJUNTOS
# ============================================================

# ------------------------------------------------------------
# 1. ¿QUÉ ES UN DICCIONARIO?
# ------------------------------------------------------------

# Lista  → acceso por índice
# Diccionario → acceso por clave (clave: valor)

alumno = {
    "nombre": "Lucas",
    "edad"  : 20,
    "nota"  : 7.8,
    "activo": True
}

# ------------------------------------------------------------
# 2. CREAR Y ACCEDER
# ------------------------------------------------------------

# Acceso directo → KeyError si no existe ️
print(alumno["nombre"])          # "Lucas"

# Acceso seguro con .get() 
print(alumno.get("ciudad"))            # None  (sin error)
print(alumno.get("ciudad", "N/A"))     # "N/A" (valor por defecto)

# ------------------------------------------------------------
# 3. MODIFICAR DICCIONARIOS
# ------------------------------------------------------------

alumno["ciudad"] = "Madrid"    # añadir clave nueva
alumno["edad"]   = 21          # modificar existente

del alumno["ciudad"]           # eliminar clave
edad = alumno.pop("edad")      # eliminar y devolver valor
alumno.clear()                 # vaciar el diccionario

# Fusionar diccionarios
alumno  = {"nombre": "Lucas", "nota": 7.8}
extras  = {"ciudad": "Madrid", "carrera": "Informática"}
alumno.update(extras)          # añade/sobreescribe con los de extras

# ------------------------------------------------------------
# 4. RECORRER DICCIONARIOS
# ------------------------------------------------------------

alumno = {"nombre": "Lucas", "edad": 20, "nota": 7.8}

# Solo claves
for clave in alumno:
    print(clave)

# Solo valores
for valor in alumno.values():
    print(valor)

# Claves Y valores a la vez 
for clave, valor in alumno.items():
    print(f"{clave}: {valor}")

# ------------------------------------------------------------
# 5. DICCIONARIOS ANIDADOS
# ------------------------------------------------------------

clase = {
    "Lucas": {"nota": 7.8, "edad": 20},
    "Ana"  : {"nota": 9.2, "edad": 22},
    "Pedro": {"nota": 4.5, "edad": 21}
}

# Acceder a datos anidados
print(clase["Ana"]["nota"])    # 9.2

# Recorrer clase completa
for nombre, datos in clase.items():
    estado = "" if datos["nota"] >= 5 else ""
    print(f"{nombre}: {datos['nota']} {estado}")

# ------------------------------------------------------------
# 6. CONSTRUIR DICCIONARIOS CON BUCLES
# ------------------------------------------------------------

notas = {"Lucas": 7.8, "Ana": 9.2, "Pedro": 4.5}

# Crear diccionario de resultados
resultados = {}
for nombre, nota in notas.items():
    if nota >= 5:
        resultados[nombre] = "Aprobado"
    else:
        resultados[nombre] = "Suspenso"

# Filtrar solo aprobados en un diccionario nuevo
aprobados = {}
for nombre, nota in notas.items():
    if nota >= 5:
        aprobados[nombre] = nota

# ------------------------------------------------------------
# 7. MÉTODOS ÚTILES
# ------------------------------------------------------------

alumno = {"nombre": "Lucas", "edad": 20, "nota": 7.8}

print("nombre" in alumno)        # True  → comprobar si existe clave
print(len(alumno))               # 3     → número de pares
print(list(alumno.keys()))       # ["nombre", "edad", "nota"]
print(list(alumno.values()))     # ["Lucas", 20, 7.8]

# Encontrar el alumno con la nota mas alta
clase = {"Lucas": 7.8, "Ana": 9.2, "Pedro": 4.5}

mejor_alumno = None
mejor_nota   = -1
for nombre, nota in clase.items():
    if nota > mejor_nota:
        mejor_nota   = nota
        mejor_alumno = nombre

print(f"Mejor: {mejor_alumno} con {mejor_nota}")   # Ana con 9.2

# ------------------------------------------------------------
# 8. CONJUNTOS (sets)
# ------------------------------------------------------------

# Set → colección SIN duplicados y SIN orden
numeros = {1, 2, 3, 3, 2, 1}
print(numeros)    # {1, 2, 3}  ← los duplicados desaparecen

# Uso más común: eliminar duplicados de una lista
notas = [7, 8, 7, 9, 8, 10, 7]
unicas = list(set(notas))    # [8, 9, 10, 7]  (orden no garantizado)

# Operaciones de conjuntos 
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)    # Unión         → {1, 2, 3, 4, 5, 6}
print(a & b)    # Intersección  → {3, 4}
print(a - b)    # Diferencia    → {1, 2}  (en a pero no en b)
print(a ^ b)    # Simétrica     → {1, 2, 5, 6} (en uno pero no en ambos)

# Métodos de set
s = {1, 2, 3}
s.add(4)         # añadir elemento
s.remove(2)      # eliminar (KeyError si no existe)
s.discard(99)    # eliminar (sin error si no existe) 

# ============================================================
#  HOJA DE TRUCOS — TEMA 5
# ============================================================
"""
CREAR
    d = {"clave": valor}
    d = dict(nombre="Lucas", edad=20)

ACCEDER
    d["clave"]               → KeyError si no existe ️
    d.get("clave", default)  → seguro, devuelve default 

MODIFICAR
    d["clave"] = valor       → añadir / modificar
    del d["clave"]           → eliminar
    d.pop("clave")           → eliminar y obtener valor
    d.update(otro_dict)      → fusionar

RECORRER
    for k in d:              → claves
    for v in d.values():     → valores
    for k, v in d.items():   → ambos 

CONSULTAR
    "clave" in d             → True / False
    len(d)                   → número de pares

CONSTRUIR DICT CON BUCLE
    d = {}
    for k, v in otro.items():
        if condicion:
            d[k] = v

SETS
    set()  /  {1, 2, 3}
    a | b    a & b    a - b  → union, interseccion, diferencia
    list(set(lista))         → eliminar duplicados
"""
