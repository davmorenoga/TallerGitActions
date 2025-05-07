import csv
from collections import namedtuple

Estudiante = namedtuple('Estudiante', ['nombre', 'nota'])

def cargar_estudiantes(path):
    estudiantes = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            try:
                nota = float(fila['nota'])
            except ValueError:
                continue
            if 0.0 <= nota <= 5.0:
                estudiantes.append(Estudiante(fila['nombre'], nota))
    return estudiantes

def imprimir_tabla(estudiantes):
    lista=sorted(estudiantes, key=lambda e: e.nombre)
    ancho_nombre = max(len(e.nombre) for e in lista)
    ancho_nota=len('NOTA')
    print (f"{'NOMBRE' .ljust(ancho_nombre)}|{'NOTA'.rjust(ancho_nota)}")
    print('-' * (ancho_nombre + 3 +  ancho_nota ))
    for e in lista:
        print(f"{e.nombre.ljust(ancho_nombre)}|{e.nota:>{ancho_nota}.1f}")
        
def calcular_promedio(estudiantes):
    if not estudiantes:
        return 0.0
    total = sum(e.nota for e in estudiantes)
    return total / len(estudiantes)

