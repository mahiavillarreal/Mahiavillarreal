# Desafío 48: Relación entre las clases Libro y Autor
#
# Este programa crea las clases Autor y Libro.
# Cada libro tiene un título, género, ISBN y un autor.
# Al crear un libro, se agrega automáticamente
# a la lista de libros de su autor.


class Autor:
    """Representa a un autor y los libros que ha escrito."""

    def __init__(self, nombre):
        """Inicializa el nombre del autor y su lista de libros."""
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        """Agrega un libro a la lista del autor si no está ya."""
        if libro not in self.libros:
            self.libros.append(libro)

    def eliminar_libro(self, libro):
        """Elimina un libro de la lista del autor si existe."""
        if libro in self.libros:
            self.libros.remove(libro)

    def mostrar_libros(self):
        """Muestra los libros escritos por el autor."""
        print(f"\nLibros de {self.nombre}:")

        if not self.libros:
            print("No hay libros registrados.")
        else:
            for libro in self.libros:
                print(f"- {libro.titulo}")

    def __str__(self):
        return self.nombre


class Libro:
    """Representa un libro y sus datos principales."""

    def __init__(self, titulo, genero, isbn, autor):
        """Inicializa los datos del libro y lo relaciona con su autor."""
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.autor = autor

        # Relacionar automáticamente el libro con su autor
        self.autor.agregar_libro(self)

    def mostrar_informacion(self):
        """Muestra la información del libro."""
        print(f"\nTítulo: {self.titulo}")