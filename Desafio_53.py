# Desafío 53: Clase Autor con lista de libros


class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []  # Lista para guardar los libros del autor


    # Método para agregar libros
    def agregar_libro(self, titulo):
        self.libros.append(titulo)


    # Método para mostrar la información del autor
    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Nacionalidad:", self.nacionalidad)
        print("Libros escritos:")


        if self.libros:
            for libro in self.libros:
                print("-", libro)
        else:
            print("No tiene libros registrados.")




# Crear un autor
autor1 = Autor("Mario Benedetti", "Uruguaya")


# Agregar libros a su lista
autor1.agregar_libro("La tregua")
autor1.agregar_libro("Gracias por el fuego")
autor1.agregar_libro("Primavera con una esquina rota")


# Mostrar los datos del autor y sus libros
autor1.mostrar_informacion()




# Reflexión:
# La clase Autor tiene una lista para almacenar sus libros.
# El método agregar_libro() permite incorporar nuevos títulos
# utilizando append(), sin modificar los anteriores
