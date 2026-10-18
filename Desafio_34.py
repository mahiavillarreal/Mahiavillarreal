# Desafío 34: Uso del módulo string
# Este programa utiliza recursos del módulo string para analizar
# un texto y reconocer letras, números y signos de puntuación.


print("Desafío 34: Uso del módulo string")


# Importar el módulo string
import string




# Crear una función para analizar un texto
def analizar_texto(texto):
    """Cuenta letras, números y signos de puntuación de un texto."""


    # Crear contadores para cada tipo de carácter
    cantidad_letras = 0
    cantidad_numeros = 0
    cantidad_puntuacion = 0


    # Recorrer cada carácter del texto
    for caracter in texto:


        # Verificar si el carácter es una letra
        if caracter in string.ascii_letters:
            cantidad_letras += 1


        # Verificar si el carácter es un número
        elif caracter in string.digits:
            cantidad_numeros += 1


        # Verificar si es un signo de puntuación
        elif caracter in string.punctuation:
            cantidad_puntuacion += 1


    # Devolver los tres resultados
    return cantidad_letras, cantidad_numeros, cantidad_puntuacion




# Crear la función principal
def main():
    """Solicita un texto y muestra los resultados del análisis."""


    # Solicitar al usuario un texto
    texto = input("Ingrese un texto: ")


    # Analizar el texto utilizando la función creada
    letras, numeros, puntuacion = analizar_texto(texto)


    # Mostrar los resultados
    print()
    print("RESULTADOS DEL ANÁLISIS:")
    print("Cantidad de letras:", letras)
    print("Cantidad de números:", numeros)
    print("Cantidad de signos de puntuación:", puntuacion)




# Ejecutar el programa
if __name__ == "__main__":
    main()