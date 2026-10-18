# Desafío 83: Búsqueda binaria en una lista ordenada de estudiantes


def busqueda_binaria(estudiantes, nombre):
    """Busca un nombre en una lista ordenada alfabéticamente.

    Devuelve la posición si lo encuentra, o -1 si no está.
    """
    inicio = 0
    fin = len(estudiantes) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if estudiantes[medio] == nombre:
            return medio
        elif estudiantes[medio] < nombre:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1


def buscar_estudiante(estudiantes, nombre):
    """Busca un estudiante y muestra el resultado."""
    posicion = busqueda_binaria(estudiantes, nombre)

    if posicion == -1:
        print(f"El estudiante '{nombre}' no está en la lista.")
    else:

    