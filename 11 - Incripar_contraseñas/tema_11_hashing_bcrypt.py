# ============================================================
#  TEMA 11 -- HASHING DE CONTRASENAS CON bcrypt
# ============================================================
# Instalacion: pip install bcrypt

import bcrypt

# ------------------------------------------------------------
# 1. POR QUE NO GUARDAR CONTRASENAS EN TEXTO PLANO
# ------------------------------------------------------------

# MAL: guardar la contrasena directamente
usuario = {"nombre": "Lucas", "password": "seguridad123"}   # PELIGROSO

# BIEN: guardar solo el hash (huella irreversible)
# Si alguien roba la base de datos, no puede recuperar la contrasena original

# ------------------------------------------------------------
# 2. CONCEPTOS CLAVE
# ------------------------------------------------------------

# HASH     --> funcion que convierte texto en una cadena fija irreversible
# SALT     --> dato aleatorio que se mezcla con la contrasena antes de hashear
#              evita ataques de "tablas arcoiris" (listas de hashes precomputados)
# BCRYPT   --> algoritmo de hashing disenado especificamente para contrasenas
#              es lento a proposito para dificultar ataques de fuerza bruta

# ------------------------------------------------------------
# 3. HASHEAR UNA CONTRASENA (lo que se vio en clase)
# ------------------------------------------------------------

# La contrasena debe ser bytes (b"...") no string
secreto  = b"seguridad123"
salt     = bcrypt.gensalt()            # genera un salt aleatorio
hasheada = bcrypt.hashpw(secreto, salt)  # genera el hash

print(secreto)    # b'seguridad123'          --> contrasena original en bytes
print(salt)       # b'$2b$12$...'            --> salt aleatorio generado
print(hasheada)   # b'$2b$12$...'            --> hash resultante (60 caracteres)

# IMPORTANTE: cada vez que ejecutas el codigo, salt y hash son distintos
# aunque la contrasena sea la misma --> es el comportamiento correcto

# ------------------------------------------------------------
# 4. VERIFICAR UNA CONTRASENA
# ------------------------------------------------------------

# El codigo de clase tenia un ERROR en la verificacion:
# hasheada == input(...)  --> INCORRECTO, compara bytes con string directamente

# FORMA CORRECTA con bcrypt.checkpw()
secreto  = b"seguridad123"
salt     = bcrypt.gensalt()
hasheada = bcrypt.hashpw(secreto, salt)

# Simulamos que el usuario introduce su contrasena
intento = input("Dame tu contrasena: ")

# checkpw() convierte y compara correctamente
if bcrypt.checkpw(intento.encode(), hasheada):
    print("CORRECTO")
else:
    print("INCORRECTO")

# .encode() convierte string --> bytes  (equivalente a b"...")
# "hola".encode()  -->  b'hola'

# ------------------------------------------------------------
# 5. FLUJO COMPLETO -- Registro y Login
# ------------------------------------------------------------

# REGISTRO: cuando el usuario crea su cuenta
def registrar_usuario(nombre, password_plano):
    password_bytes = password_plano.encode()        # str --> bytes
    salt           = bcrypt.gensalt()
    hash_guardado  = bcrypt.hashpw(password_bytes, salt)
    # En un sistema real guardarias en base de datos:
    # {"nombre": nombre, "password_hash": hash_guardado}
    return {"nombre": nombre, "password_hash": hash_guardado}


# LOGIN: cuando el usuario intenta entrar
def verificar_login(usuario_db, password_intento):
    password_bytes = password_intento.encode()      # str --> bytes
    return bcrypt.checkpw(password_bytes, usuario_db["password_hash"])


# Prueba del flujo
usuario_db = registrar_usuario("Lucas", "miContrasena123")
print(usuario_db["nombre"])          # "Lucas"
print(usuario_db["password_hash"])   # hash (nunca la contrasena real)

# Intento correcto
resultado = verificar_login(usuario_db, "miContrasena123")
print(f"Login correcto: {resultado}")    # True

# Intento incorrecto
resultado = verificar_login(usuario_db, "contrasenaWrong")
print(f"Login correcto: {resultado}")    # False

# ------------------------------------------------------------
# 6. GENSALT -- COSTE DEL HASH (rounds)
# ------------------------------------------------------------

# gensalt() acepta un parametro "rounds" (por defecto 12)
# Cuantos mas rounds, mas lento --> mas seguro, pero mas tiempo de espera

salt_normal = bcrypt.gensalt()           # rounds=12 por defecto
salt_rapido = bcrypt.gensalt(rounds=10)  # menos seguro, mas rapido
salt_lento  = bcrypt.gensalt(rounds=14)  # mas seguro, mas lento

# Para produccion: entre 10 y 14 es lo habitual
# Para pruebas/tests: rounds=4 para que sea rapido

# ------------------------------------------------------------
# 7. CONVERTIR ENTRE str Y bytes
# ------------------------------------------------------------

# str --> bytes
texto  = "hola"
bytes_ = texto.encode()          # b'hola'
bytes_ = texto.encode("utf-8")   # equivalente, explicito

# bytes --> str
texto = bytes_.decode()          # "hola"
texto = bytes_.decode("utf-8")   # equivalente

# Contrasenas en bcrypt: siempre bytes
password_str   = "miPassword"
password_bytes = password_str.encode()    # necesario para bcrypt

# ------------------------------------------------------------
# 8. ERRORES COMUNES
# ------------------------------------------------------------

# ERROR 1: pasar string en vez de bytes a hashpw
# bcrypt.hashpw("texto", salt)          --> TypeError
# bcrypt.hashpw(b"texto", salt)         --> correcto
# bcrypt.hashpw("texto".encode(), salt) --> correcto

# ERROR 2: comparar hash con == en vez de checkpw
# hasheada == password                  --> INCORRECTO (siempre False)
# bcrypt.checkpw(password, hasheada)    --> CORRECTO

# ERROR 3: no encodear el intento en checkpw
# bcrypt.checkpw(intento, hasheada)     --> TypeError si intento es str
# bcrypt.checkpw(intento.encode(), hasheada) --> correcto

# ERROR 4 (el del codigo de clase): comparar hash con input() directamente
# if hasheada == input("Contrasena: "):  --> siempre False, tipos distintos

# ============================================================
#  HOJA DE TRUCOS -- TEMA 11
# ============================================================
"""
INSTALACION
    pip install bcrypt

IMPORTAR
    import bcrypt

HASHEAR
    secreto  = password.encode()           # str --> bytes OBLIGATORIO
    salt     = bcrypt.gensalt()            # salt aleatorio
    hasheada = bcrypt.hashpw(secreto, salt)

VERIFICAR (siempre con checkpw, nunca con ==)
    if bcrypt.checkpw(intento.encode(), hash_guardado):
        print("Correcto")

CONVERTIR
    "texto".encode()   --> b'texto'  (str --> bytes)
    b"texto".decode()  --> 'texto'   (bytes --> str)

ROUNDS (coste)
    bcrypt.gensalt(rounds=12)   # por defecto, bueno para produccion
    bcrypt.gensalt(rounds=4)    # solo para tests

FLUJO TIPICO
    # Registro:
    hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    # guardar hash en base de datos (nunca la password original)

    # Login:
    if bcrypt.checkpw(intento.encode(), hash_de_bd):
        acceso concedido

ERRORES FRECUENTES
    TypeError   --> pasas str en vez de bytes
    Siempre False --> usas == en vez de checkpw()
"""
