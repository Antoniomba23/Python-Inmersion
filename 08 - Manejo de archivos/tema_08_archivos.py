# ============================================================
#  TEMA 8 — MANEJO DE ARCHIVOS
# ============================================================

# ------------------------------------------------------------
# 1. ABRIR ARCHIVOS — dos formas
# ------------------------------------------------------------

#  Forma antigua → hay que cerrar manualmente
# archivo = open("notas.txt", "r")
# contenido = archivo.read()
# archivo.close()    # si se te olvida → pérdida de datos

#  Forma moderna con with → se cierra SIEMPRE automáticamente
# with open("notas.txt", "r") as archivo:
#     contenido = archivo.read()
# aquí el archivo ya está cerrado 

# ------------------------------------------------------------
# 2. MODOS DE APERTURA
# ------------------------------------------------------------

# "r"   → leer         (error si no existe)
# "w"   → escribir     (crea o SOBREESCRIBE ️)
# "a"   → añadir       (añade al final, crea si no existe)
# "x"   → crear nuevo  (error si ya existe)
# "r+"  → leer y escribir a la vez

# ------------------------------------------------------------
# 3. ESCRIBIR ARCHIVOS
# ------------------------------------------------------------

alumnos = ["Lucas", "Ana", "Pedro"]

# write() → escribe un string
with open("salida.txt", "w") as f:
    f.write("Lista de alumnos:\n")
    for alumno in alumnos:
        f.write(f"{alumno}\n")       # \n = salto de línea

# writelines() → escribe una lista
lineas = []
for a in alumnos:
    lineas.append(f"{a}\n")
with open("salida.txt", "w") as f:
    f.writelines(lineas)

# append → añadir sin borrar lo anterior
with open("salida.txt", "a") as f:
    f.write("Marta\n")              # se añade al final 

# ------------------------------------------------------------
# 4. LEER ARCHIVOS — todas las formas
# ------------------------------------------------------------

# read() → todo el contenido como un string
with open("salida.txt", "r") as f:
    contenido = f.read()
    print(contenido)

# readline() → una línea cada vez
with open("salida.txt", "r") as f:
    primera = f.readline()    # "Lucas\n"
    segunda = f.readline()    # "Ana\n"

# readlines() → lista con todas las líneas
with open("salida.txt", "r") as f:
    lineas = f.readlines()    # ["Lucas\n", "Ana\n", ...]

# Iterar línea a línea (más eficiente) 
with open("salida.txt", "r") as f:
    for linea in f:
        linea = linea.strip()    # elimina \n y espacios
        print(linea)

# ------------------------------------------------------------
# 5. PROCESAR DATOS DE UN ARCHIVO
# ------------------------------------------------------------

# Crear archivo de notas
datos = ["Lucas,7.8", "Ana,9.2", "Pedro,4.5", "Marta,6.0", "Carlos,3.8"]

with open("alumnos.txt", "w") as f:
    for d in datos:
        f.write(f"{d}\n")

# Leer y construir diccionario {nombre: nota}
clase = {}
with open("alumnos.txt", "r") as f:
    for linea in f:
        nombre, nota = linea.strip().split(",")   # patrón estrella 
        clase[nombre] = float(nota)

print(clase)

# Guardar solo aprobados
with open("aprobados.txt", "w") as f:
    for nombre, nota in clase.items():
        if nota >= 5:
            f.write(f"{nombre},{nota}\n")

# ------------------------------------------------------------
# 6. EXCEPCIONES CON ARCHIVOS
# ------------------------------------------------------------

def leer_archivo_seguro(ruta):
    try:
        with open(ruta, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f" El archivo '{ruta}' no existe")
        return None
    except PermissionError:
        print(f" Sin permisos para leer '{ruta}'")
        return None

contenido = leer_archivo_seguro("alumnos.txt")
if contenido:
    print(contenido)

# ------------------------------------------------------------
# 7. TRABAJAR CON CSV
# ------------------------------------------------------------

import csv

# Escribir CSV
alumnos_csv = [
    {"nombre": "Lucas", "nota": 7.8},
    {"nombre": "Ana",   "nota": 9.2}
]
with open("clase.csv", "w", newline="") as f:
    campos   = ["nombre", "nota"]
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()           # escribe la cabecera
    escritor.writerows(alumnos_csv)  # escribe todas las filas

# Leer CSV
with open("clase.csv", "r") as f:
    lector = csv.DictReader(f)       # cada fila → diccionario 
    for fila in lector:
        print(f"{fila['nombre']}: {fila['nota']}")

# ============================================================
#  HOJA DE TRUCOS — TEMA 8
# ============================================================
"""
ABRIR (siempre con with)
    with open("archivo.txt", modo) as f:

MODOS
    "r"  leer        "w"  escribir (sobreescribe ️)
    "a"  añadir      "x"  crear nuevo

LEER
    f.read()           → todo como string
    f.readline()       → una línea
    f.readlines()      → lista de líneas
    for linea in f:    → iterar línea a línea 

LIMPIAR LÍNEAS
    linea.strip()      → elimina \n y espacios

ESCRIBIR
    f.write("texto\n")
    f.writelines(lista_de_strings)

PATRÓN CSV MANUAL
    nombre, nota = linea.strip().split(",")   

ERRORES
    FileNotFoundError  → archivo no existe con modo "r"
    PermissionError    → sin permisos

CSV
    import csv
    csv.DictReader(f)                → leer como dicts
    csv.DictWriter(f, fieldnames)    → escribir desde dicts
"""
