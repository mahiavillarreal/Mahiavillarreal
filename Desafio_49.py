# Desafío 49: Estructuras de datos para una biblioteca


# Utilizaría clases para representar autores, libros y la biblioteca.
# También utilizaría listas para almacenar múltiples autores y libros.




class Autor:
    def __init__(self, nombre):
        self.nombre = nombre




class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor




class Biblioteca:
    def __init__(self):
        self.autores = []
        self.libros = []


    def agregar_autor(self, autor):
        self.autores.append(autor)


    def agregar_libro(self, libro):
        self.libros.append(libro)


    def mostrar_libros(self):
        print("Libros de la biblioteca:")
        for libro in self.libros:
            print(f"{libro.titulo} - Autor: {libro.autor.nombre}")




# Crear autores
autor1 = Autor("Gabriel García Márquez")
autor2 = Autor("Mario Benedetti")


# Crear libros
libro1 = Libro("Cien años de soledad", autor1)
libro2 = Libro("La tregua", autor2)


# Crear biblioteca
biblioteca = Biblioteca()


# Agregar autores y libros
biblioteca.agregar_autor(autor1)
biblioteca.agregar_autor(autor2)
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)


# Mostrar los libros
biblioteca.mostrar_libros()




# Reflexión:
# Las clases permiten organizar la información de autores y libros.
# Las listas permiten almacenar varios objetos y recorrerlos.
# De esta manera, es posible agregar, buscar o eliminar elementos
# y mantener organizada la información de la biblioteca.


