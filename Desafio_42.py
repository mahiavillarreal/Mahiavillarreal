# Desafío 42: Invertir palabras de una oración con recursividad


# Este programa utiliza una función recursiva para invertir el orden
# de las palabras de una oración sin utilizar funciones incorporadas
# de Python destinadas a invertir cadenas o listas.




# Crear una función recursiva para invertir las palabras
def invertir_palabras(palabras, posicion):
    # Caso base:
    # Si llegamos a la primera palabra, la devolvemos
    # y finalizamos las llamadas recursivas
    if posicion == 0:
        return palabras[0]


    # Caso recursivo:
    # Tomar la palabra de la posición actual y llamar nuevamente
    # a la función para continuar con la palabra anterior
    return palabras[posicion] + " " + invertir_palabras(
        palabras, posicion - 1
    )




# Crear la función principal del programa
def main():
    print("Desafío 42: Invertir palabras con recursividad")
    print()


    # Solicitar una oración al usuario
    oracion = input("Ingrese una oración: ")


    # Separar la oración en palabras
    palabras = oracion.split()


    # Verificar que la oración contenga al menos una palabra
    if len(palabras) > 0:
        # Llamar a la función comenzando desde la última posición
        resultado = invertir_palabras(palabras, len(palabras) - 1)


        print()
        print("Oración original:")
        print(oracion)


        print()
        print("Oración con las palabras invertidas:")
        print(resultado)
    else:
        print("No se ingresaron palabras.")




# Ejecutar el programa desde la función principal
if __name__ == "__main__":
    main()