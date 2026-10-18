# Desafío 11: Formateo de Factura
# Este programa solicita los datos de un producto,
# calcula el importe total de la compra
# y muestra una factura con la información ingresada.

print("Desafío 3: Formateo de Factura")

# Solicitar el nombre del producto
nombre_producto = input("Ingrese el nombre del producto: ")

# Solicitar la cantidad de productos
cantidad = int(input("Ingrese la cantidad: "))

# Solicitar el precio unitario del producto
precio_unitario = float(input("Ingrese el precio unitario: "))

# Calcular el importe total
total = cantidad * precio_unitario

# Dejar una línea en blanco para mejorar la presentación
print()

# Mostrar la factura
print("========== FACTURA ==========")
print("Producto: ", nombre_producto)
print("Cantidad: ", cantidad)
print("Precio unitario: $", precio_unitario)
print("Total a pagar: $", total)
print("=============================")
