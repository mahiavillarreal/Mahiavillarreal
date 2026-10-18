# Desafío 2: Mejora del Cálculo del Promedio
# Este programa solicita al usuario todas las calificaciones
# en una sola línea separadas por comas,
# calcula el promedio y muestra el resultado final.


print("Desafío 2: Mejora del Cálculo del Promedio")


# Solicitar al usuario todas las calificaciones separadas por comas
entrada = input("Ingrese las calificaciones separadas por comas: ")


# Separar las calificaciones utilizando la coma como separador
calificaciones = entrada.split(",")


# Crear una variable para acumular la suma de las calificaciones
suma_calificaciones = 0


# Recorrer la lista de calificaciones
for calificacion in calificaciones:


    # Convertir cada calificación a número decimal
    nota = float(calificacion)


    # Sumar la calificación al acumulador
    suma_calificaciones = suma_calificaciones + nota


# Calcular el promedio
promedio = suma_calificaciones / len(calificaciones)


# Dejar una línea en blanco para mejorar la presentación
print()


# Mostrar el resultado final
print("El promedio de las calificaciones es:", promedio)