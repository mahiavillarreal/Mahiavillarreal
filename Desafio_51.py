# Desafío 51: Búsqueda de libros y autores en una biblioteca


# Para buscar un libro o un autor, podemos recorrer las listas
# y comparar los nombres o títulos con el dato ingresado.
# Utilizamos métodos de búsqueda dentro de la clase Biblioteca.




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


    def buscar_autor(self, nombre):
        for autor in self.autores:
            if autor.nombre.lower() == nombre.lower():
                return autor
        return None


    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None




# Crear autores
autor1 = Autor("Mario Benedetti")
autor2 = Autor("Gabriel García Márquez")


# Crear libros
libro1 = Libro("La tregua", autor1)
libro2 = Libro("Cien años de soledad", autor2)


# Crear biblioteca
biblioteca = Biblioteca()


biblioteca.agregar_autor(autor1)
biblioteca.agregar_autor(autor2)


biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)


# Buscar un autor
autor_encontrado = biblioteca.buscar_autor("Mario Benedetti")


if autor_encontrado:
    print("Autor encontrado:", autor_encontrado.nombre)
else:
    print("Autor no encontrado.")


# Buscar un libro
libro_encontrado = biblioteca.buscar_libro("La tregua")


if libro_encontrado:
    print("Libro encontrado:", libro_encontrado.titulo)
    print("Escrito por:", libro_encontrado.autor.nombre)
else:
    print("Libro no encontrado.")




# Reflexión:
# Una función de búsqueda puede recorrer las listas de la biblioteca
# y comparar los datos para encontrar un libro o un autor.
# El método lower() permite comparar sin distinguir mayúsculas.
# Si encuentra una coincidencia, devuelve el objeto.
# Si no encuentra resultados, devuelve None.



