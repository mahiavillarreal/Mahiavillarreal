# Desafío 65: Polimorfismo con figuras geométricas
#
# La clase base Figura define el método area().
# Circulo y Cuadrado heredan de Figura y sobrescriben area()
# con su propio cálculo.

import math


class Figura:
    """Clase base para las figuras geométricas."""

    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        """Calcula el área. Cada subclase debe sobrescribirlo."""
        raise NotImplementedError("Cada figura debe definir su área.")


class Circulo(Figura):
    """Representa un círculo."""

    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def area(self):
        """Área del círculo: π * radio²."""
        return math.pi * self.radio ** 2


class Cuadrado(Figura):
    """Representa un cuadrado."""

    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado

    def area(self):
        """Área del cuadrado: lado²."""
        return self.lado ** 2


def main():
    """Demuestra el polimorfismo con figuras geométricas."""

    print("Desafío 65: Polimorfismo con figuras geométricas")
    print()

    # 1. Crear los objetos
    circulo = Circulo(5)
    cuadrado = Cuadrado(4)

    # 2. Guardarlos en una misma lista
    figuras = [circulo, cuadrado]

    # 3 y 4. Recorrer la lista y llamar a area() sin preguntar el tipo
    for figura in figuras:
        print(f"{figura.nombre}: área = {figura.area():.2f}")


if __name__ == "__main__":
    main()