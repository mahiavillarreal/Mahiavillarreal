# Desafío 27: Suma y promedio de una lista
# Este programa crea una función que recibe una lista de números
# y devuelve la suma y el promedio de sus elementos.


print("Desafío 27: Suma y promedio de una lista")




# Crear una función que calcule la suma y el promedio
def calcular_suma_promedio(lista_numeros):


    # Calcular la suma de todos los números de la lista
    suma = sum(lista_numeros)


    # Calcular el promedio
    promedio = suma / len(lista_numeros)


    # Devolver ambos resultados
    return suma, promedio




# Crear la función principal del programa
def main():


    # Crear una lista de números
    numeros = [10, 20, 30, 40, 50]


    # Mostrar la lista original
    print("Lista de números:")
    print(numeros)


    print()


    # Llamar a la función y guardar los resultados
    suma, promedio = calcular_suma_promedio(numeros)


    # Mostrar los resultados
    print("La suma de los números es:", suma)
    print("El promedio de los números es:", promedio)




# Ejecutar el programa desde la función principal
if __name__ == "__main__":
    main()