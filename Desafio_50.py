# Desafío 50: Ampliación de la clase Autor

# Para hacer más completa la clase Autor, agregamos atributos como
# fecha de nacimiento, nacionalidad y género literario, y métodos
# para mostrar la información, agregar libros y consultar las obras.


class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento, genero):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.libros = []

    def agregar_libro(self, titulo):
        self.libros.append(titulo)

    def mostrar_informacion(self):
        print("Autor:", self.nombre)
        print("País de origen:", self.nacionalidad)
        print("Nació el:", self.fecha_nacimiento)
        print("Género:", self.genero)

    def mostrar_libros(self):
        print("Obras publicadas:")
        for libro in self.libros:
            print("*", libro)


# Crear un autor
autor1 = Autor(
    "Gabriel García Márquez",
    "Colombiana",
    "06/03/1927",
    "Realismo mágico"
)

# Agregar libros
autor1.agregar_libro("Cien años de soledad")
autor1.agregar_libro("El amor en los tiempos del cólera")
autor1.agregar_libro("Crónica de una muerte anunciada")

# Mostrar información
autor1.mostrar_informacion()
autor1.mostrar_libros()


# Reflexión:
# Al sumar más atributos, cada objeto guarda datos más completos
# sobre el autor que representa.
# Los métodos permiten trabajar con esa información: registrar obras
# y mostrarlas de forma ordenada.
# Así la clase Autor queda más útil y fácil de reutilizar.