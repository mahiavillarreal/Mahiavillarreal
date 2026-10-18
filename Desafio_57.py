# Desafío 57: Herencia - clase Poeta
#
# La clase Autor guarda los datos básicos de un autor.
# La clase Poeta hereda de Autor y agrega el atributo tipo_poesia.


class Autor:
    """Representa a un autor con nombre y nacionalidad."""

    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrar_datos_basicos(self):
        """Muestra el nombre y la nacionalidad del autor."""
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")


class Poeta(Autor):
    """Representa a un poeta, que es un tipo particular de autor."""

    def __init__(self, nombre, nacionalidad, tipo_poesia):
        # Se inicializan los atributos heredados con super()
        super().__init__(nombre, nacionalidad)

        # Atributo exclusivo de Poeta
        self.tipo_poesia = tipo_poesia

    def mostrar_ficha(self):
        """Muestra toda la información del poeta."""
        super().mostrar_datos_basicos()
        print(f"Tipo de poesía: {self.tipo_poesia}")


def main():
    """Demuestra el funcionamiento de la herencia."""

    print("Desafío 57: Herencia - clase Poeta")
    print()

    # 1. Crear dos objetos Poeta
    neruda = Poeta("Pablo Neruda", "Chile", "Poesía amorosa")
    storni = Poeta("Alfonsina Storni", "Argentina", "Poesía modernista")

    # 2. Mostrar los datos de cada poeta
    print("Ficha del primer poeta:")
    neruda.mostrar_ficha()

    print()

    print("Ficha del segundo poeta:")
    storni.mostrar_ficha()

    # 3. Verificar el uso de lo heredado de Autor
    print()
    print("Método heredado de Autor (usado por Poeta):")
    storni.mostrar_datos_basicos()

    print()
    print("Atributos heredados de Autor:")
    print(f"Nombre: {neruda.nombre}")
    print(f"Nacionalidad: {neruda.nacionalidad}")

    # Comprobar la relación de herencia
    print()
    print(f"¿neruda es un Autor? {isinstance(neruda, Autor)}")
    print(f"¿neruda es un Poeta? {isinstance(neruda, Poeta)}")
    print(f"¿Poeta es subclase de Autor? {issubclass(Poeta, Autor)}")


if __name__ == "__main__":
    main()