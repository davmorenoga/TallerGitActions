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
