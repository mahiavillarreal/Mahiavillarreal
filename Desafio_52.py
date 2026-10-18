# Desafío 52: Encapsulamiento en la clase Libro


class Libro:
    def __init__(self, titulo, autor, isbn):
        # Atributos privados
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn


    # Getter y setter del título
    def get_titulo(self):
        return self.__titulo


    def set_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo


    # Getter y setter del autor
    def get_autor(self):
        return self.__autor


    def set_autor(self, nuevo_autor):
        self.__autor = nuevo_autor


    # Getter y setter del ISBN
    def get_isbn(self):
        return self.__isbn


    def set_isbn(self, nuevo_isbn):
        self.__isbn = nuevo_isbn




# Crear un objeto Libro
libro1 = Libro("La tregua", "Mario Benedetti", "9789974896257")


# Mostrar los datos originales
print("DATOS ORIGINALES")
print("Título:", libro1.get_titulo())
print("Autor:", libro1.get_autor())
print("ISBN:", libro1.get_isbn())


# Modificar los datos usando los setters
libro1.set_titulo("Gracias por el fuego")
libro1.set_autor("Mario Benedetti")
libro1.set_isbn("9789974000000")


# Mostrar los datos modificados
print("\nDATOS MODIFICADOS")
print("Título:", libro1.get_titulo())
print("Autor:", libro1.get_autor())
print("ISBN:", libro1.get_isbn())




# Reflexión:
# Los atributos privados permiten proteger los datos de un objeto.
# Los getters permiten consultar sus valores.
# Los setters permiten modificar esos valores de forma controlada.