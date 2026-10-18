# Desafío 55: Acceso a los libros de un autor


class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.__libros = []  # Lista privada de libros


    # Método para agregar libros
    def agregar_libro(self, titulo):
        self.__libros.append(titulo)


    # Método para consultar los títulos
    def obtener_libros(self):
        return self.__libros.copy()




# Función que recibe un objeto Autor
# y devuelve los títulos de sus libros
def obtener_titulos_autor(autor):
    return autor.obtener_libros()




# Crear un autor
autor1 = Autor("Mario Benedetti", "Uruguaya")


# Agregar libros
autor1.agregar_libro("La tregua")
autor1.agregar_libro("Gracias por el fuego")
autor1.agregar_libro("Primavera con una esquina rota")


# Obtener los títulos mediante la función
titulos = obtener_titulos_autor(autor1)


# Mostrar resultados
print("Autor:", autor1.nombre)
print("Nacionalidad:", autor1.nacionalidad)
print("Libros escritos:")


for titulo in titulos:
    print("-", titulo)




# Comprobar que modificar la lista devuelta
# no afecta la lista privada del autor
titulos.append("Libro de prueba")


print("\nLibros originales después de modificar la copia:")
print(obtener_titulos_autor(autor1))




# Reflexión:
# La lista __libros es privada y no se accede directamente.
# Los métodos permiten agregar y consultar sus elementos.
# obtener_libros() devuelve una copia para proteger
# la lista original de modificaciones externas.
