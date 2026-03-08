# ============================================================
#  TEMA 4 — LISTAS Y TUPLAS
# ============================================================

# ------------------------------------------------------------
# 1. LISTAS vs TUPLAS
# ------------------------------------------------------------

# LISTA  → mutable (puedes cambiarla después de crearla)
notas = [7.8, 9.2, 5.0, 6.5]

# TUPLA  → inmutable (una vez creada, no se puede modificar)
coordenadas = (40.7128, -74.0060)   # latitud, longitud NYC

# ¿Cuándo usar cada una?
# Lista  → datos que van a cambiar  (carrito de compra, alumnos)
# Tupla  → datos fijos              (días de la semana, colores RGB)

# ------------------------------------------------------------
# 2. CREAR LISTAS
# ------------------------------------------------------------

vacia       = []
numeros     = [1, 2, 3, 4, 5]
mixta       = [42, "hola", True, 3.14]    # pueden mezclar tipos
anidada     = [[1, 2], [3, 4], [5, 6]]   # lista de listas
desde_rango = list(range(1, 6))           # [1, 2, 3, 4, 5]

print(anidada[1][0])    # → 3  (fila 1, columna 0)

# ------------------------------------------------------------
# 3. INDEXING Y SLICING
# ------------------------------------------------------------

frutas = ["manzana", "pera", "uva", "kiwi", "mango"]
#           0         1       2      3        4
#          -5        -4      -3     -2       -1

# INDEXING
print(frutas[0])     # "manzana"   (primero)
print(frutas[-1])    # "mango"     (último)
print(frutas[-2])    # "kiwi"      (penúltimo)

# SLICING → [inicio : fin : paso]  (fin excluido)
print(frutas[1:3])   # ["pera", "uva"]
print(frutas[:2])    # ["manzana", "pera"]
print(frutas[2:])    # ["uva", "kiwi", "mango"]
print(frutas[::2])   # ["manzana", "uva", "mango"]
print(frutas[::-1])  # ["mango", "kiwi", "uva", "pera", "manzana"] ← invertir 

# ------------------------------------------------------------
# 4. MÉTODOS ESENCIALES
# ------------------------------------------------------------

notas = [6.0, 8.5, 4.0]

# AÑADIR
notas.append(9.0)           # añade al final
notas.insert(1, 7.5)        # inserta en posición 1
notas.extend([5.0, 6.5])    # fusiona con otra lista

# ELIMINAR
notas.remove(4.0)    # elimina la primera ocurrencia del valor
notas.pop()          # elimina y devuelve el último
notas.pop(0)         # elimina y devuelve el de posición 0
notas.clear()        # vacía la lista → []

# BUSCAR / CONSULTAR
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(numeros))         # 8    → cuántos elementos
print(numeros.count(1))     # 2    → cuántas veces aparece el 1
print(numeros.index(5))     # 4    → posición del valor 5
print(5 in numeros)         # True → ¿está el 5?
print(max(numeros))         # 9
print(min(numeros))         # 1
print(sum(numeros))         # 31

# ORDENAR
numeros.sort()                   # modifica la lista original
numeros.sort(reverse=True)       # orden descendente
ordenada = sorted(numeros)       # ️ devuelve lista NUEVA, no modifica
numeros.reverse()                # invierte el orden in-place

# ------------------------------------------------------------
# 5. RECORRER LISTAS
# ------------------------------------------------------------

alumnos = ["Lucas", "Ana", "Pedro"]
notas   = [7.8, 9.2, 5.0]

# Con indice
for i in range(len(alumnos)):
    print(f"{i + 1}. {alumnos[i]}")

# Dos listas a la vez usando el mismo indice
for i in range(len(alumnos)):
    if notas[i] >= 5:
        estado = "Aprobado"
    else:
        estado = "Suspenso"
    print(f"{alumnos[i]}: {notas[i]} - {estado}")

# ------------------------------------------------------------
# 6. LIST COMPREHENSIONS
# ------------------------------------------------------------

numeros = list(range(1, 11))

cuadrados  = [n**2 for n in numeros]
pares      = [n for n in numeros if n % 2 == 0]
mayusculas = [n.upper() for n in ["lucas", "ana"]]
resultado  = ["par" if n % 2 == 0 else "impar" for n in numeros]

# ------------------------------------------------------------
# 7. TUPLAS
# ------------------------------------------------------------

punto     = (3, 7)
singleton = (42,)          # ️ una coma obligatoria para tupla de 1 elemento
sin_paren = 1, 2, 3        # también es tupla

# Acceso igual que listas
colores = ("rojo", "verde", "azul")
print(colores[0])    # "rojo"
print(colores[-1])   # "azul"
print(colores[1:])   # ("verde", "azul")

# ️ NO puedes modificarlas
# colores[0] = "amarillo"   → TypeError

# UNPACKING 
x, y = (3, 7)
nombre, edad, ciudad = ("Lucas", 20, "Madrid")

# Swap sin variable temporal
a, b = 10, 20
a, b = b, a
print(a, b)   # 20 10

# Convertir entre lista y tupla
lista = [1, 2, 3]
tupla = tuple(lista)   # (1, 2, 3)
lista2 = list(tupla)   # [1, 2, 3]

# ============================================================
#  HOJA DE TRUCOS — TEMA 4
# ============================================================
"""
CREAR
    lista = []  /  lista = [1, 2, 3]  /  list(range(n))

ACCESO
    lista[0]   lista[-1]   lista[1:3]   lista[::-1]

AÑADIR
    lista.append(x)      # al final
    lista.insert(i, x)   # en posición i
    lista.extend(otra)   # fusionar listas

ELIMINAR
    lista.remove(x)      # por valor
    lista.pop(i)         # por índice (devuelve el elemento)
    lista.clear()        # vaciar

CONSULTAR
    len()   sum()   max()   min()
    x in lista             → True / False
    lista.count(x)         → cuántas veces aparece
    lista.index(x)         → posición de x

ORDENAR
    lista.sort()           → modifica original
    sorted(lista)          → devuelve nueva ️

️ NO machaques la lista con len()
    aprobados = len(aprobados)     pierdes la lista
    num_aprobados = len(aprobados) 

COMPREHENSION
    [expr for x in lista if condicion]

TUPLA
    t = (1, 2, 3)    → inmutable
    a, b, c = t      → unpacking
    (42,)            → ️ coma obligatoria para tupla de 1 elemento
"""
