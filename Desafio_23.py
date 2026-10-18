# Desafío 23: Traza de la matriz inversa
# Este programa crea una matriz utilizando NumPy,
# calcula su matriz inversa y luego obtiene la traza,
# sumando los elementos de la diagonal principal.


print("Desafío 23: Traza de la matriz inversa")


# Importar NumPy para trabajar con matrices
import numpy as np


# Crear la matriz A
A = np.array([
    [1, 0, 1],
    [4, -1, 4],
    [5, 6, 7]
], dtype=float)


# Mostrar la matriz original
print("Matriz A:")
print(A)

print()

# Calcular la matriz inversa de A
matriz_inversa = np.linalg.inv(A)

# Mostrar la matriz inversa
print("Matriz inversa de A:")
print(matriz_inversa)

print()

# Calcular la traza de la matriz inversa
# La traza es la suma de los elementos de la diagonal principal
traza_inversa = np.trace(matriz_inversa)


# Mostrar el resultado final
print("La traza de la matriz inversa de A es:", round(traza_inversa))