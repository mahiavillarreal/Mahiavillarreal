print("Desafío 21: Control de Notas de Estudiantes")

from collections import Counter
import matplotlib.pyplot as plt

entrada = input("Ingrese las notas separadas por comas: ")

notas = []

try:
    for nota in entrada.split(","):
        notas.append(float(nota.strip()))
except ValueError:
    print("Error: ingrese solo números separados por comas.")
    exit()

# Pregunta 1
promedio = sum(notas) / len(notas)
print()
print("Pregunta 1:")
print("El promedio de la clase es:", round(promedio, 2))

# Pregunta 2
print()
print("Pregunta 2:")
print("La nota más baja es:", min(notas))
print("La nota más alta es:", max(notas))

# Pregunta 3
contador = Counter(notas)
nota_mas_repetida = contador.most_common(1)

print()
print("Pregunta 3:")
print("La nota que más se repite es:", nota_mas_repetida[0][0])
print("Cantidad de veces:", nota_mas_repetida[0][1])

# Pregunta 4
etiquetas = [f"Est. {i + 1}" for i in range(len(notas))]

plt.figure(figsize=(8, 5))
plt.bar(etiquetas, notas)
plt.title("Notas de los estudiantes")
plt.xlabel("Estudiantes")
plt.ylabel("Notas")
plt.show()