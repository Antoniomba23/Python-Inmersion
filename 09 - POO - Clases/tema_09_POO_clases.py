# ============================================================
#  TEMA 9 — PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# ============================================================

# ------------------------------------------------------------
# 1. CLASE BÁSICA — anatomía completa
# ------------------------------------------------------------

class Alumno:
    centro = "IES Python"        # atributo de CLASE → compartido por todos

    def __init__(self, nombre, edad, nota):
        """Constructor → se ejecuta al crear el objeto"""
        self.nombre = nombre     # atributo de INSTANCIA → único por objeto
        self.edad   = edad
        self.nota   = nota

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

    def evaluar(self):
        estado = "Aprobado" if self.nota >= 5 else "Suspenso"
        return f"{self.nombre}: {self.nota} → {estado}"

    def __str__(self):
        """Qué se muestra al hacer print(objeto)"""
        return f"Alumno({self.nombre}, {self.nota})"

    def __repr__(self):
        """Representación técnica para debugging"""
        return f"Alumno(nombre='{self.nombre}', nota={self.nota})"


# Crear instancias
lucas = Alumno("Lucas", 20, 7.8)
ana   = Alumno("Ana",   22, 9.2)

lucas.saludar()           # "Hola, soy Lucas y tengo 20 años"
print(ana.evaluar())      # "Ana: 9.2 → Aprobado"
print(lucas)              # "Alumno(Lucas, 7.8)"  ← usa __str__
print(lucas.nombre)       # "Lucas"

# Atributo de clase
print(lucas.centro)       # "IES Python"
Alumno.centro = "IES Django"
print(lucas.centro)       # "IES Django" → cambia para todos

# ------------------------------------------------------------
# 2. MÉTODOS DUNDER MÁS DE EXAMEN
# ------------------------------------------------------------

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre   = nombre
        self.precio   = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} → {self.precio}€ (x{self.cantidad})"

    def __len__(self):
        return self.cantidad       # len(producto) → cantidad

    def __eq__(self, otro):
        return self.precio == otro.precio   # p1 == p2

    def __lt__(self, otro):
        return self.precio < otro.precio    # p1 < p2 (para ordenar)


p1 = Producto("Manzana", 1.5, 10)
p2 = Producto("Pera",    1.5,  6)

print(p1)           # Manzana → 1.5€ (x10)
print(len(p1))      # 10
print(p1 == p2)     # True  (mismo precio)

# ------------------------------------------------------------
# 3. HERENCIA
# ------------------------------------------------------------

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad   = edad

    def presentarse(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años")


class Alumno(Persona):          # Alumno hereda de Persona
    def __init__(self, nombre, edad, nota):
        super().__init__(nombre, edad)   # llama al __init__ del padre 
        self.nota = nota

    def evaluar(self):           # método propio del hijo
        return "Aprobado" if self.nota >= 5 else "Suspenso"


class Profesor(Persona):        # Profesor también hereda de Persona
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def presentarse(self):       # sobreescribe el método del padre
        print(f"Soy el profesor {self.nombre}, imparto {self.asignatura}")


lucas = Alumno("Lucas", 20, 7.8)
prof  = Profesor("García", 45, "Python")

lucas.presentarse()     # hereda del padre
prof.presentarse()      # sobreescrito
print(lucas.evaluar())  # "Aprobado"

print(isinstance(lucas, Alumno))    # True
print(isinstance(lucas, Persona))   # True ← también es Persona 

# ------------------------------------------------------------
# 4. ENCAPSULACIÓN
# ------------------------------------------------------------

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular  = titular
        self.__saldo  = saldo    # __ → atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            print(" Saldo insuficiente")
        else:
            self.__saldo -= cantidad

    def get_saldo(self):         # getter → forma controlada de leer
        return self.__saldo

    def __str__(self):
        return f"Cuenta de {self.titular}: {self.__saldo}€"


cuenta = CuentaBancaria("Lucas", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
print(cuenta.get_saldo())    # 1300
print(cuenta)                # Cuenta de Lucas: 1300€
# cuenta.__saldo             #  AttributeError

# ------------------------------------------------------------
# 5. EJEMPLO COMPLETO — Biblioteca
# ------------------------------------------------------------

class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor  = autor
        self.año    = año

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.año})"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo, autor, año):
        self.libros.append(Libro(titulo, autor, año))

    def mostrar_libros(self):
        for i in range(len(self.libros)):
            print(f"{i + 1}. {self.libros[i]}")

    def buscar_autor(self, autor):
        for libro in self.libros:
            if libro.autor == autor:
                return libro.titulo
        return f"No hay libros de {autor}"

    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                return

    def __len__(self):
        return len(self.libros)

    def __str__(self):
        return f"Biblioteca con {len(self)} libros"


bib = Biblioteca()
bib.agregar_libro("El Quijote", "Cervantes", 1605)
bib.agregar_libro("1984", "Orwell", 1949)
bib.mostrar_libros()
print(len(bib))         # 2

# ============================================================
#  HOJA DE TRUCOS — TEMA 9
# ============================================================
"""
DEFINIR CLASE
    class Nombre:
        atributo_clase = valor         → compartido

        def __init__(self, param):
            self.atributo = param      → único por objeto

        def metodo(self):
            return self.atributo

CREAR OBJETO
    obj = Nombre(valor)

ACCEDER
    obj.atributo
    obj.metodo()

HERENCIA
    class Hijo(Padre):
        def __init__(self, ...):
            super().__init__(...)      → llama al padre 

DUNDER MÁS USADOS
    __init__    → constructor
    __str__     → print(objeto)
    __len__     → len(objeto)
    __eq__      → objeto == otro

ENCAPSULACIÓN
    self.__privado    → doble __ → privado
    self._protegido   → simple _ → convención "no tocar"

COMPROBAR TIPO
    isinstance(obj, Clase)    → True / False
"""
