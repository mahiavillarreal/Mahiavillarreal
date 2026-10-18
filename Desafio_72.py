# Desafío 72: Búsqueda de códigos de productos


print("DESAFÍO 72: SISTEMA DE INVENTARIO")
print()


# Lista de códigos de productos disponibles
codigos_productos = [101, 205, 310, 420, 535, 640, 750]


print("Códigos disponibles:", codigos_productos)
print()


try:
    # Solicitar el código al usuario
    codigo = int(input("Ingrese el código del producto que desea buscar: "))


    # Verificar si el código está en la lista
    if codigo in codigos_productos:


        # Obtener la posición del código
        posicion = codigos_productos.index(codigo)


        print(f"El código {codigo} fue encontrado.")
        print(f"Se encuentra en la posición {posicion} de la lista.")


    else:
        print(f"El código {codigo} no se ha encontrado en el inventario.")


except ValueError:
    print("Error: Debe ingresar un código numérico válido.")


