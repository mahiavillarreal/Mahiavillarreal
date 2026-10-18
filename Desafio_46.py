# Desafío 46: Estructuras de datos anidadas
# Este programa representa una cadena de tiendas utilizando
# estructuras de datos anidadas para organizar productos,
# empleados y transacciones de cada tienda.


print("Desafío 46: Estructuras de datos anidadas")


# Crear una estructura que representa varias tiendas
tiendas = [
    {
        "nombre": "Tienda Centro",
        "productos": [
            {"nombre": "Arroz", "stock": 20},
            {"nombre": "Leche", "stock": 15},
        ],
        "empleados": [
            {"nombre": "Ana", "cargo": "Cajera"},
            {"nombre": "Luis", "cargo": "Encargado"},
        ],
        "transacciones": [
            {"producto": "Arroz", "cantidad": 2},
            {"producto": "Leche", "cantidad": 1},
        ],
    },
    {
        "nombre": "Tienda Norte",
        "productos": [
            {"nombre": "Pan", "stock": 30},
            {"nombre": "Azúcar", "stock": 10},
        ],
        "empleados": [
            {"nombre": "Carla", "cargo": "Cajera"},
            {"nombre": "Pedro", "cargo": "Encargado"},
        ],
        "transacciones": [
            {"producto": "Pan", "cantidad": 3},
        ],
    },
]


# Recorrer cada tienda
for tienda in tiendas:
    print()
    print("Tienda:", tienda["nombre"])


    print("Productos:")
    for producto in tienda["productos"]:
        print(
            "-",
            producto["nombre"],
            "| Stock:",
            producto["stock"]
        )


    print("Empleados:")
    for empleado in tienda["empleados"]:
        print(
            "-",
            empleado["nombre"],
            "| Cargo:",
            empleado["cargo"]
        )


    print("Transacciones:")
    for transaccion in tienda["transacciones"]:
        print(
            "- Producto:",
            transaccion["producto"],
            "| Cantidad:",
            transaccion["cantidad"]
        )
