# Desafío 37: Análisis de texto con collections


# Este programa analiza un texto ingresado por el usuario,
# identifica las 10 palabras más frecuentes utilizando Counter
# del módulo collections y muestra los resultados en un gráfico
# de barras utilizando matplotlib.


# Importar Counter para contar la frecuencia de las palabras
from collections import Counter


# Importar matplotlib para crear el gráfico de barras
import matplotlib.pyplot as plt




# Crear una función para analizar el texto
def analizar_texto(texto):
    # Convertir todo el texto a minúsculas
    texto = texto.lower()


    # Eliminar algunos signos de puntuación
    signos = ".,;:¿?¡!()"


    for signo in signos:
        texto = texto.replace(signo, "")


    # Separar el texto en palabras
    palabras = texto.split()


    # Contar cuántas veces aparece cada palabra
    contador = Counter(palabras)


    # Obtener las 10 palabras más comunes
    palabras_comunes = contador.most_common(10)


    # Devolver los resultados
    return palabras_comunes




# Crear una función para mostrar el gráfico
def crear_grafico(palabras_comunes):
    # Crear listas para guardar las palabras y sus frecuencias
    palabras = []
    frecuencias = []


    # Recorrer los resultados obtenidos
    for palabra, frecuencia in palabras_comunes:
        palabras.append(palabra)
        frecuencias.append(frecuencia)


    # Crear el gráfico de barras
    plt.bar(palabras, frecuencias)


    # Agregar título y nombres a los ejes
    plt.title("Las 10 palabras más comunes")
    plt.xlabel("Palabras")
    plt.ylabel("Frecuencia")


    # Ajustar el gráfico para que se vea correctamente
    plt.tight_layout()


    # Mostrar el gráfico
    plt.show()




# Crear la función principal del programa
def main():
    print("Desafío 37: Análisis de texto")
    print()


    # Solicitar un texto al usuario
    texto = input("Ingrese un texto para analizar: ")


    # Analizar el texto ingresado
    palabras_comunes = analizar_texto(texto)


    print()


    # Verificar que se hayan ingresado palabras
    if len(palabras_comunes) > 0:
        print("Las 10 palabras más comunes son:")


        # Mostrar cada palabra junto con su frecuencia
        for palabra, frecuencia in palabras_comunes:
            print(palabra, ":", frecuencia)


        # Crear y mostrar el gráfico de barras
        crear_grafico(palabras_comunes)


    else:
        print("No se ingresaron palabras para analizar.")




# Ejecutar el programa desde la función principal
if __name__ == "__main__":
    main()