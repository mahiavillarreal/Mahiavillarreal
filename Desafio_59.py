# Desafío 59: Herencia y especialización
# LibroDigital y EBook
#
# Este programa muestra herencia en varios niveles.
# LibroDigital hereda de Libro y EBook hereda de LibroDigital.
# EBook sobrescribe mostrar_informacion() para agregar su dato propio.


class Libro:
    """Representa los datos generales de un libro."""

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def mostrar_informacion(self):
        """Muestra la información básica del libro."""
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")


class LibroDigital(Libro):
    """Representa un libro en formato digital."""

    def __init__(self, titulo, autor, isbn, formato, tamano_archivo):
        # Se inicializan los atributos heredados de Libro
        super().__init__(titulo, autor, isbn)

        # Atributos propios de LibroDigital
        self.formato = formato
        self.tamano_archivo = tamano_archivo

    def mostrar_informacion(self):
        """Muestra toda la información del libro digital."""
        super().mostrar_informacion()
        print(f"Formato: {self.formato}")
        print(f"Tamaño del archivo: {self.tamano_archivo}")


class EBook(LibroDigital):
    """Representa un libro digital con enlace de descarga."""

    def __init__(self, titulo, autor, isbn, formato, tamano_archivo,
                 enlace_descarga):
        # Se inicializan los atributos heredados de LibroDigital
        super().__init__(titulo, autor, isbn, formato, tamano_archivo)

        # Atributo propio de EBook
        self.enlace_descarga = enlace_descarga

    def mostrar_informacion(self):
        """Muestra toda la información del EBook."""
        # Reutiliza el método de LibroDigital
        super().mostrar_informacion()

        # Agrega el dato específico de EBook
        print(f"Enlace de descarga: {self.enlace_descarga}")


def main():
    """Prueba el funcionamiento de las clases."""

    print("Desafío 59: LibroDigital y EBook")
    print()

    # Crear un objeto LibroDigital
    libro_digital = LibroDigital(
        "Fundamentos de Bases de Datos",
        "Laura Fernández",
        "9781122334455",
        "PDF",
        "8 MB",
    )

    # Crear un objeto EBook
    ebook = EBook(
        "Aprende JavaScript desde Cero",
        "Martín Rodríguez",
        "9785566778899",
        "EPUB",
        "4 MB",
        "https://biblioteca-ejemplo.com/descargas/javascript",
    )

    # Mostrar la información con el mismo método en ambos objetos
    print("Información del LibroDigital:")
    libro_digital.mostrar_informacion()

    print()

    print("Información del EBook:")
    ebook.mostrar_informacion()


if __name__ == "__main__":
    main()