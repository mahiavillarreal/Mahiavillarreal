# Desafío 33: Generación de un número aleatorio
# Este programa utiliza el módulo random para generar
# un número aleatorio entre 1 y 100.


print("Desafío 33: Generación de un número aleatorio")


# Importar el módulo random para trabajar con números aleatorios
import random




# Crear una función para generar un número aleatorio
def generar_numero_aleatorio():
    """Genera y devuelve un número entero aleatorio entre 1 y 100."""


    # Generar un número entero aleatorio incluyendo ambos extremos
    numero = random.randint(1, 100)


    # Devolver el número generado
    return numero




# Crear la función principal del programa
def main():
    """Ejecuta el programa y muestra el número generado."""


    # Llamar a la función y guardar el resultado
    numero_aleatorio = generar_numero_aleatorio()


    # Mostrar el número aleatorio generado
    print("Número aleatorio generado:", numero_aleatorio)




# Ejecutar el programa
if __name__ == "__main__":
    main()