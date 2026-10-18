# Desafío 67: Manejo de excepciones en Python
# División de dos números enteros con try-except


def pedir_entero(mensaje):
    """Pide un número entero al usuario. Puede lanzar ValueError."""
    return int(input(mensaje))


def realizar_division():
    """Pide dos enteros, los divide y maneja los errores posibles."""
    try:
        dividendo = pedir_entero("Ingresá el dividendo (número entero): ")
        divisor = pedir_entero("Ingresá el divisor (número entero): ")

        cociente = dividendo / divisor

    except ValueError:
        # Se ingresó texto, decimales u otro valor que no es entero
        print("Error: el valor ingresado no es un número entero válido.")

    except ZeroDivisionError:
        # El divisor es cero
        print("Error: no se puede dividir entre cero.")

    else:
        # Solo se ejecuta si no hubo ninguna excepción
        print(f"Resultado: {dividendo} / {divisor} = {cociente:.2f}")

    finally:
        # Se ejecuta siempre
        print("Operación finalizada.")


def main():
    print("Desafío 67: División con manejo de excepciones")
    print()
    realizar_division()


if __name__ == "__main__":
    main()


# Reflexión:
# - try contiene el código que puede fallar (input, int() y la división).
# - ValueError captura los valores no numéricos o no enteros.
# - ZeroDivisionError captura la división entre cero.
# - else muestra el resultado solo cuando todo salió bien.
# - finally se ejecuta siempre, haya o no error.