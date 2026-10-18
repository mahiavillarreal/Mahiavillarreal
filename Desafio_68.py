# Desafío 68: Operaciones matemáticas y manejo de excepciones


def realizar_operaciones(valores):
    print("DESAFÍO 68: OPERACIONES MATEMÁTICAS")
    print()


    for valor in valores:
        try:
            print("Valor:", valor)


            # Convertir el valor a número
            numero = float(valor)


            # Realizar operaciones matemáticas
            doble = numero * 2
            cuadrado = numero ** 2
            division = 100 / numero


        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")


        except TypeError:
            print("Error: El tipo de dato no permite realizar la operación.")


        except ValueError:
            print("Error: El valor ingresado no es numérico.")


        else:
            print("Doble:", doble)
            print("Cuadrado:", cuadrado)
            print("Resultado de 100 dividido entre", numero, ":", division)


        finally:
            print("Operación finalizada.")
            print()




# Lista con diferentes tipos de valores
valores = [10, 5, 0, "hola", None, "4", -2]


# Ejecutar el programa
realizar_operaciones(valores)




# Reflexión:
# El programa recorre una lista y realiza operaciones matemáticas.
# ZeroDivisionError controla la división entre cero.
# TypeError controla los tipos de datos incompatibles.
# ValueError controla los valores que no pueden convertirse a números.
# El manejo de excepciones permite continuar con los demás valores.
