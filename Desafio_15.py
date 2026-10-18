# Desafío 1: Calificaciones Aprobatorias y Desaprobatorias
# Este programa solicita las calificaciones de varios estudiantes,
# determina cuántos aprobaron y cuántos desaprobaron
# utilizando un bucle y estructuras condicionales.


print("Desafío 1: Calificaciones Aprobatorias y Desaprobatorias")


# Solicitar la cantidad de estudiantes
cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))


# Crear contadores para aprobados y desaprobados
aprobados = 0
desaprobados = 0


# Recorrer la cantidad de estudiantes ingresada
for estudiante in range(1, cantidad_estudiantes + 1):


    # Solicitar la calificación del estudiante
    calificacion = float(input("Ingrese la calificación del estudiante " + str(estudiante) + ": "))


    # Verificar si la calificación es aprobatoria
    if calificacion >= 7:


        # Aumentar el contador de aprobados
        aprobados = aprobados + 1


    else:


        # Aumentar el contador de desaprobados
        desaprobados = desaprobados + 1


# Dejar una línea en blanco para ordenar la salida
print()


# Mostrar los resultados finales
print("Cantidad de estudiantes aprobados:", aprobados)
print("Cantidad de estudiantes desaprobados:", desaprobados)