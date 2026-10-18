
# Desafío 22: Operaciones con matrices
# Este programa crea dos matrices utilizando NumPy,
# multiplica la matriz A por 2, calcula la transpuesta de la matriz B
# y suma ambas matrices para obtener el resultado de 2A + Bᵀ.


print("Desafío 22: Operaciones con matrices")


# Importar NumPy para crear y realizar operaciones con matrices
import numpy as np


# Crear la matriz A
A = np.array([
    [1, 2],
    [3, 4]
])


# Crear la matriz B
B = np.array([
    [5, 6],
    [7, 8]
])


# Mostrar las matrices originales
print("Matriz A:")
print(A)


print()


print("Matriz B:")
print(B)


print()


# Multiplicar todos los elementos de la matriz A por 2
dos_por_A = 2 * A


# Calcular la transpuesta de la matriz B
# La transposición intercambia las filas por las columnas
B_transpuesta = B.T


# Sumar la matriz 2A con la matriz transpuesta de B
matriz_resultante = dos_por_A + B_transpuesta


# Mostrar los resultados de cada operación
print("Matriz 2A:")
print(dos_por_A)


print()


print("Matriz transpuesta de B:")
print(B_transpuesta)


print()


# Mostrar la matriz resultante
print("Resultado de la operación 2A + Bᵀ:")
print(matriz_resultante)