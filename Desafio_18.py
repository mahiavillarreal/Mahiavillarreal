# Desafío 18: Gestión del Stock de la Verdulería
# Este programa permite gestionar el inventario de una verdulería
# utilizando una lista. Se realizan diferentes operaciones como
# consultar, eliminar, agregar, verificar, ordenar y copiar productos.

print("Desafío 18: Gestión del Stock de la Verdulería")

# Crear el inventario inicial
inventario = ["manzanas", "bananas", "zanahorias", "espinacas", "brocoli", "cebolla", "kiwis"]

# Mostrar el inventario inicial
print("Inventario inicial:")
print(inventario)

print()

# -------------------------
# Pregunta 1
# -------------------------

# Contar la cantidad de productos del inventario
print("Pregunta 1:")
print("Cantidad de productos en el inventario:", len(inventario))

print()

# -------------------------
# Pregunta 2
# -------------------------

# Mostrar el producto que ocupa la tercera posición
print("Pregunta 2:")
print("El producto en la tercera posición es:", inventario[2])

print()

# -------------------------
# Pregunta 3
# -------------------------

# Eliminar las bananas del inventario
inventario.remove("bananas")


print("Pregunta 3:")
print("Inventario después de vender las bananas:")
print(inventario)


print()


# -------------------------
# Pregunta 4
# -------------------------


# Agregar los nuevos productos al inventario
inventario.extend(["frutillas", "apio", "papas"])


print("Pregunta 4:")
print("Inventario después de agregar los nuevos productos:")
print(inventario)


print()


# -------------------------
# Pregunta 5
# -------------------------


# Verificar si las papas están en el inventario
print("Pregunta 5:")


if "papas" in inventario:
    print("Las papas están en el inventario.")


else:
    print("Las papas no están en el inventario.")


print()


# -------------------------
# Pregunta 6
# -------------------------


# Como solo hay espacio para 7 productos,
# se elimina el último producto para hacer lugar al nuevo.
inventario.pop()


# Agregar el nuevo producto
inventario.append("dragonfruit")


print("Pregunta 6:")
print("Inventario después de agregar dragonfruit:")
print(inventario)


print()


# -------------------------
# Pregunta 7
# -------------------------


# Ordenar alfabéticamente el inventario
inventario.sort()


print("Pregunta 7:")
print("Inventario ordenado alfabéticamente:")
print(inventario)


print()


# -------------------------
# Pregunta 8
# -------------------------


# Crear una copia independiente del inventario
copia_inventario = inventario.copy()


print("Pregunta 8:")
print("Copia del inventario:")
print(copia_inventario)
