# Desafío 19: Ordenar el Inventario de Libros
# Este programa organiza una lista de códigos de libros
# en orden decreciente utilizando la función sorted(),
# sin modificar la lista original.


print("Desafío 19: Ordenar el Inventario de Libros")


# Crear una lista con los códigos de identificación de los libros
inventario_libros = [105, 302, 150, 420, 215, 98, 501]


# Mostrar la lista original
print("Inventario original:")
print(inventario_libros)


print()


# Crear una nueva lista ordenada en forma decreciente
inventario_ordenado = sorted(inventario_libros, reverse=True)


# Mostrar la nueva lista ordenada
print("Inventario ordenado en forma decreciente:")
print(inventario_ordenado)


print()


# Mostrar nuevamente la lista original para comprobar
# que no fue modificada
print("Inventario original después de ordenar:")
print(inventario_libros)


print()


# Explicar por qué se utiliza sorted()
print("Explicación:")
print("Se utiliza la función sorted() porque crea una nueva lista ordenada")
print("sin modificar la lista original.")
print("El método sort() no se utiliza porque cambia directamente")
print("el contenido de la lista original.")

