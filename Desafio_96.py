# Desafío 96: Inventario de productos con diccionarios
#
# La clave es el código del producto.
# El valor es otro diccionario con nombre, precio y stock.


def agregar_producto(inventario, codigo, nombre, precio, stock):
    """Agrega un producto nuevo. Devuelve True si se agregó."""
    if codigo in inventario:
        print(f"Error: el código {codigo} ya existe.")
        return False

    inventario[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
    }
    print(f"Producto '{nombre}' agregado correctamente.")
    return True


def actualizar_stock(inventario, codigo, nuevo_stock):
    """Actualiza el stock de un producto existente."""
    if codigo not in inventario:
        print(f"Error: no existe un producto con el código {codigo}.")
        return False

    if nuevo_stock < 0:
        print("Error: el stock no puede ser negativo.")
        return False

    inventario[codigo]["stock"] = nuevo_stock
    nombre = inventario[codigo]["nombre"]
    print(f"Stock de '{nombre}' actualizado a {nuevo_stock}.")
    return True


def buscar_producto(inventario, codigo):
    """Busca un producto por código y muestra sus detalles."""
    producto = inventario.get(codigo)

    if producto is None:
        print(f"No se encontró ningún producto con el código {codigo}.")
        return None

    print(f"\nCódigo: {codigo}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: ${producto['precio']:.2f}")
    print(f"Stock:  {producto['stock']} unidades")
    return producto


def mostrar_inventario(inventario):
    """Muestra todos los productos del inventario."""
    print("\n--- Inventario completo ---")
    if not inventario:
        print("El inventario está vacío.")
        return

    for codigo, producto in inventario.items():
        nombre = producto["nombre"]
        precio = producto["precio"]
        stock = producto["stock"]
        print(f"{codigo} | {nombre} | ${precio:.2f} | Stock: {stock}")


def main():
    print("Desafío 96: Inventario de productos con diccionarios")
    print()

    inventario = {}

    # 1. Agregar productos
    agregar_producto(inventario, "P001", "Cuaderno", 150.00, 40)
    agregar_producto(inventario, "P002", "Lapicera", 45.50, 120)
    agregar_producto(inventario, "P003", "Mochila", 1800.00, 15)

    # Intento de agregar un código repetido
    agregar_producto(inventario, "P001", "Regla", 30.00, 10)

    mostrar_inventario(inventario)

    # 2. Actualizar stock
    print()
    actualizar_stock(inventario, "P002", 95)
    actualizar_stock(inventario, "P999", 10)  # no existe
    actualizar_stock(inventario, "P003", -5)  # valor inválido

    # 3. Buscar productos
    buscar_producto(inventario, "P002")
    buscar_producto(inventario, "P888")  # no existe

    mostrar_inventario(inventario)


if __name__ == "__main__":
    main()