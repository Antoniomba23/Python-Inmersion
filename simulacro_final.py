# ============================================================
#  SIMULACRO FINAL — 3 Ejercicios de nivel intermedio
#  Mezcla de todos los temas
# ============================================================

# ============================================================
#  EJERCICIO 1 — Funciones + Listas + Excepciones
# ============================================================

def pedir_notas():
    notas = []
    print("Introduce notas (escribe 'fin' para terminar):")
    while True:
        entrada = input("Nota: ")
        if entrada.lower() == "fin":
            break
        try:
            nota = float(entrada)
            if not 0 <= nota <= 10:
                print("️ La nota debe estar entre 0 y 10")
            else:
                notas.append(nota)
                print(f" Nota {nota} añadida")
        except ValueError:
            print("️ Eso no es un número válido, inténtalo de nuevo")
    return notas


def analizar_notas(notas):
    if not notas:
        return None
    aprobados = []
    for n in notas:
        if n >= 5:
            aprobados.append(n)
    return {
        "media"    : round(sum(notas) / len(notas), 2),
        "maxima"   : max(notas),
        "minima"   : min(notas),
        "aprobados": len(aprobados),
        "suspensos": len(notas) - len(aprobados)
    }


def mostrar_informe(informe):
    if not informe:
        print(" No hay notas que mostrar")
        return
    print("\n" + "=" * 35)
    print("        INFORME DE NOTAS")
    print("=" * 35)
    print(f"  Media        : {informe['media']}")
    print(f"  Nota máxima  : {informe['maxima']}")
    print(f"  Nota mínima  : {informe['minima']}")
    print(f"  Aprobados    : {informe['aprobados']}")
    print(f"  Suspensos    : {informe['suspensos']}")
    print("=" * 35)


# notas   = pedir_notas()        # descomentar para ejecutar con input real
# informe = analizar_notas(notas)
# mostrar_informe(informe)

# ============================================================
#  EJERCICIO 2 — POO + Archivos
# ============================================================

class Tarea:
    def __init__(self, titulo, prioridad, completada=False):
        self.titulo     = titulo
        self.prioridad  = prioridad
        self.completada = completada

    def __str__(self):
        estado = "" if self.completada else "⬜"
        return f"{estado} [{self.prioridad.upper()}] {self.titulo}"


class GestorTareas:
    PRIORIDADES = ["alta", "media", "baja"]

    def __init__(self):
        self.tareas = []

    def agregar(self, titulo, prioridad):
        if prioridad not in self.PRIORIDADES:
            print(f"️ Prioridad inválida. Usa: {self.PRIORIDADES}")
            return
        self.tareas.append(Tarea(titulo, prioridad))
        print(f" Tarea '{titulo}' añadida con prioridad {prioridad}")

    def completar(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                tarea.completada = True
                print(f" '{titulo}' marcada como completada")
                return
        print(f" Tarea '{titulo}' no encontrada")

    def mostrar(self):
        if not self.tareas:
            print("No hay tareas")
            return
        print("\nLISTA DE TAREAS:")
        print("-" * 35)

        # Mostrar primero las de alta, luego media, luego baja
        for prioridad in ["alta", "media", "baja"]:
            for tarea in self.tareas:
                if tarea.prioridad == prioridad:
                    print(f"  {tarea}")

        print("-" * 35)

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for t in self.tareas:
                f.write(f"{t.titulo},{t.prioridad},{t.completada}\n")
        print(f" Tareas guardadas en '{ruta}'")

    def cargar(self, ruta):
        try:
            with open(ruta, "r") as f:
                self.tareas = []
                for linea in f:
                    titulo, prioridad, completada = linea.strip().split(",")
                    self.tareas.append(
                        Tarea(titulo, prioridad, completada == "True")
                    )
            print(f" Tareas cargadas desde '{ruta}'")
        except FileNotFoundError:
            print(f" Archivo '{ruta}' no encontrado")

    def __len__(self):
        return len(self.tareas)


# Prueba Ejercicio 2
g = GestorTareas()
g.agregar("Estudiar Python",    "alta")
g.agregar("Hacer ejercicio",    "media")
g.agregar("Leer documentación", "baja")
g.agregar("Repasar POO",        "alta")
g.completar("Estudiar Python")
g.mostrar()
g.guardar("tareas.txt")
g.cargar("tareas.txt")

# ============================================================
#  EJERCICIO 3 — Bucles + Diccionarios + Módulos
# ============================================================

import random
from datetime import datetime

jugadores = ["Lucas", "Ana", "Pedro", "Marta", "Carlos"]
partidos  = 10

# Generar goles aleatorios
equipo = {}
for jugador in jugadores:
    goles_jugador = []
    for _ in range(partidos):
        goles_jugador.append(random.randint(0, 3))
    equipo[jugador] = goles_jugador

# Calcular estadisticas
estadisticas = {}
for jugador, goles in equipo.items():
    total  = 0
    mejor  = 0
    for g in goles:
        total += g
        if g > mejor:
            mejor = g
    media = round(total / len(goles), 2)
    estadisticas[jugador] = {
        "total"   : total,
        "media"   : media,
        "mejor"   : mejor,
        "partidos": goles
    }

# Ordenar ranking de mayor a menor total (burbuja simple)
jugadores_lista = list(estadisticas.keys())
for i in range(len(jugadores_lista)):
    for j in range(i + 1, len(jugadores_lista)):
        if estadisticas[jugadores_lista[j]]["total"] > estadisticas[jugadores_lista[i]]["total"]:
            jugadores_lista[i], jugadores_lista[j] = jugadores_lista[j], jugadores_lista[i]

# Informe con fecha
fecha = datetime.now().strftime("%d/%m/%Y a las %H:%M")

print("\n" + "=" * 50)
print(f"   INFORME DE GOLEADORES")
print(f"   {fecha}")
print("=" * 50)

pos = 1
for jugador in jugadores_lista:
    stats = estadisticas[jugador]
    print(f"\n  {pos}. {jugador}")
    print(f"     Goles por partido : {stats['partidos']}")
    print(f"     Total goles       : {stats['total']}")
    print(f"     Media por partido : {stats['media']}")
    print(f"     Mejor partido     : {stats['mejor']} goles")
    pos += 1

print("\n" + "=" * 50)
print("   RANKING FINAL")
print("=" * 50)
pos = 1
for jugador in jugadores_lista:
    stats  = estadisticas[jugador]
    barra  = "*" * stats["total"]
    print(f"  {pos}. {jugador}: {barra} ({stats['total']} goles)")
    pos += 1
print("=" * 50)
