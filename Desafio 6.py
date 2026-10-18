
# Desafío 2: Calcular promedio
# Este programa solicita al usuario cinco calificaciones,
# calcula el promedio de ellas y muestra el resultado final.


print("Desafío 2: Calcular promedio")


# Solicitar al usuario que ingrese las cinco calificaciones
calificacion1 = float(input("Ingrese la primera calificación: "))
calificacion2 = float(input("Ingrese la segunda calificación: "))
calificacion3 = float(input("Ingrese la tercera calificación: "))
calificacion4 = float(input("Ingrese la cuarta calificación: "))
calificacion5 = float(input("Ingrese la quinta calificación: "))


# Calcular la suma de todas las calificaciones
suma_calificaciones = calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5


# Calcular el promedio dividiendo la suma entre la cantidad de calificaciones
promedio = suma_calificaciones / 5


# Dejar una línea en blanco para ordenar la salida
print()


# Mostrar el promedio obtenido
print("El promedio de las cinco calificaciones es:", promedio)
