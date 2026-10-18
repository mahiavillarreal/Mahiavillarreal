# Desafío 28: Primera letra de cada palabra en mayúscula
# Este programa crea una función que recibe una cadena de texto
# y devuelve la misma cadena con la primera letra
# de cada palabra convertida a mayúscula.

print("Desafío 28: Primera letra de cada palabra en mayúscula")


# Crear una función que transforme la cadena
def convertir_a_titulo(cadena):

    # Separar la cadena en palabras
    palabras = cadena.split(" ")

    # Poner en mayúscula la primera letra de cada palabra
    # (capitalize() deja el resto en minúscula)
    palabras_modificadas = [palabra.capitalize() for palabra in palabras]

    # Unir las palabras otra vez en una sola cadena
    cadena_modificada = " ".join(palabras_modificadas)

    # Devolver la cadena modificada
    return cadena_modificada


# Crear la función principal del programa
def main():

    # Solicitar al usuario que ingrese una frase
    texto = input("Ingrese una frase: ")

    # Llamar a la función y guardar el resultado
    resultado = convertir_a_titulo(texto)

    # Mostrar la cadena original
    print()
    print("Cadena original:")
    print(texto)

    # Mostrar la cadena modificada
    print()
    print("Cadena con mayúsculas iniciales:")
    print(resultado)


# Ejecutar el programa desde la función principal
if __name__ == "__main__":
    main()