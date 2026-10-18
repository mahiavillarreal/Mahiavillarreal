# Desafío 56: Autor con mayor cantidad de libros


class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.__libros = []  # Lista privada


    # Método para agregar libros
    def agregar_libro(self, titulo):
        self.__libros.append(titulo)


    # Método para consultar la cantidad de libros
    def cantidad_libros(self):
        return len(self.__libros)


    # Método para mostrar los libros
    def obtener_libros(self):
        return self.__libros.copy()




# Función que recibe una lista de autores
# y devuelve el autor con más libros
def autor_con_mas_libros(autores):
    if not autores:
        return None


    autor_mayor = autores[0]


    for autor in autores:
        if autor.cantidad_libros() > autor_mayor.cantidad_libros():
            autor_mayor = autor


    return autor_mayor




# Crear autores
autor1 = Autor("Mario Benedetti", "Uruguaya")
autor2 = Autor("Gabriel García Márquez", "Colombiana")
autor3 = Autor("Isabel Allende", "Chilena")


# Agregar libros a cada autor
autor1.agregar_libro("La tregua")
autor1.agregar_libro("Gracias por el fuego")
autor1.agregar_libro("Primavera con una esquina rota")


autor2.agregar_libro("Cien años de soledad")
autor2.agregar_libro("El amor en los tiempos del cólera")


autor3.agregar_libro("La casa de los espíritus")


# Crear lista de autores
autores = [autor1, autor2, autor3]


# Mostrar cantidad de libros de cada autor
print("CANTIDAD DE LIBROS POR AUTOR")


for autor in autores:
    print(autor.nombre, ":", autor.cantidad_libros(), "libros")


# Buscar el autor con más libros
resultado = autor_con_mas_libros(autores)


print("\nAUTOR CON MAYOR CANTIDAD DE LIBROS")


if resultado:
    print("Nombre:", resultado.nombre)
    print("Nacionalidad:", resultado.nacionalidad)
    print("Cantidad de libros:", resultado.cantidad_libros())
    print("Libros registrados:")


    for titulo in resultado.obtener_libros():
        print("-", titulo)
else:
    print("No hay autores registrados.")




# Reflexión:
# El encapsulamiento permite proteger la lista de libros.
# La función compara la cantidad mediante un método público,
# sin acceder directamente al atributo privado __libros.
