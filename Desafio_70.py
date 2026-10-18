# Desafío 70: Excepción personalizada NegativeNumberError
# Cálculo de raíces cuadradas con manejo de excepciones

import math


class NegativeNumberError(Exception):
    """Se lanza cuando se intenta calcular la raíz de un número negativo."""

    def __init__(self, numero):
        self.numero = numero
        super().__init__(
            f"No se puede calcular la raíz cuadrada de {numero}: "
            "el número es negativo."
        )


def calcular_raiz(numero):
    """Devuelve la raíz cuadrada de un número no negativo."""
    if numero < 0:
        raise NegativeNumberError(numero)
    return math.sqrt(numero)


def main():
    print("Desafío 70: Raíz cuadrada con excepción personalizada")
    print()

    try:
        numero = float(input("Ingresá un número: "))
        raiz = calcular_raiz(numero)

    except ValueError:
        print("Error: debés ingresar un valor numérico válido.")

    except NegativeNumberError as error:
        print(f"Error: {error}")

    else:
        print(f"La raíz cuadrada de {numero} es {raiz:.2f}")

    finally:
        print("Fin del programa.")


if __name__ == "__main__":
    main()