# Desafío 54: Encapsulamiento con @property
#
# Este programa implementa la clase Autor utilizando encapsulamiento.
# Los atributos nombre y nacionalidad son privados y se accede a ellos
# mediante propiedades. Los setters validan que no se ingresen
# cadenas vacías.


class Autor:
    """Representa a un autor con nombre y nacionalidad."""

    def __init__(self, nombre, nacionalidad):
        # Los valores se asignan utilizando los setters
        # para que sean validados desde el momento de la creación.
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    @property
    def nombre(self):
        """Devuelve el nombre del autor."""
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        """Modifica el nombre si el valor ingresado es válido."""
        if not isinstance(nuevo_nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede ser una cadena vacía.")

        self._nombre = nuevo_nombre.strip()

    @property
    def nacionalidad(self):
        """Devuelve la nacionalidad del autor."""
        return self._nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        """Modifica la nacionalidad si el valor ingresado es válido."""
        if not isinstance(nueva_nacionalidad, str):
            raise TypeError("La nacionalidad debe ser una cadena de texto.")
        if not nueva_nacionalidad.strip():
            raise ValueError("La nacionalidad no puede ser una cadena vacía.")

        self._nacionalidad = nueva_nacionalidad.strip()


def main():
    """Demuestra el funcionamiento de la clase Autor."""

    print("Desafío 54: Encapsulamiento con @property")
    print()

    # 1. Crear un objeto Autor
    autor = Autor("Gabriel García Márquez", "Colombiana")

    # 2. Mostrar sus datos