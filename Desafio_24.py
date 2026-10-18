# Desafío 24: Rango de una matriz
# Este programa crea una matriz utilizando NumPy,
# calcula su transpuesta, suma ambas matrices
# y obtiene el rango de la matriz resultante.


print("Desafío 24: Rango de la matriz resultante")


# Importar NumPy para crear matrices
# y realizar operaciones de álgebra lineal
import numpy as np


# Crear la matriz A
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


# Mostrar la matriz original
print("Matriz A:")
print(A)


print()


# Calcular la transpuesta de la matriz A
# La transposición intercambia las filas por las columnas
A_transpuesta = A.T


# Mostrar la matriz transpuesta
print("Matriz transpuesta de A:")
print(A_transpuesta)


print()


# Sumar la matriz A y su transpuesta
matriz_resultante = A + A_transpuesta

# Mostrar la matriz obtenida
print("Matriz resultante de A + Aᵀ:")
print(matriz_resultante)

print()

# Calcular el rango de la matriz resultante
# El rango representa la cantidad de filas o columnas
# linealmente independientes que tiene la matriz
rango = np.linalg.matrix_rank(matriz_resultante)

# Mostrar el resultado final
print("El rango de la matriz resultante es:", rango)