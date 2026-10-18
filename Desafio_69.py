# Desafío 69: Cálculo del factorial con manejo de excepciones


def calcular_factorial(numero):
    # Comprobar que el número sea entero
    if type(numero) is not int:
        raise TypeError("El número debe ser un entero.")


    # Comprobar que no sea negativo
    if numero < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo.")


    # Establecer un límite para evitar cálculos demasiado grandes
    if numero > 1000:
        raise OverflowError("El número es demasiado grande para ser procesado.")


    # Calcular el factorial
    factorial = 1


    for i in range(1, numero + 1):
        factorial *= i


    return factorial




# Programa principal
print("DESAFÍO 69: CÁLCULO DEL FACTORIAL")
print()


try:
    # Solicitar un número al usuario
    entrada = input("Ingrese un número entero positivo: ")
    numero = int(entrada)


    # Calcular y mostrar el resultado
    resultado = calcular_factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")


except TypeError as error:
    print("Error de tipo:", error)


except ValueError as error:
    print("Error de valor:", error)


except OverflowError as error:
    print("Error de tamaño:", error)


finally:
    print("Fin del programa.")




# Reflexión:
# La función calcula el factorial mediante un ciclo for.
# TypeError controla los valores que no son enteros.
# ValueError controla los números negativos y las entradas inválidas.
# OverflowError controla los números demasiado grandes.
# El manejo de excepciones evita que el programa termine abruptamente.



