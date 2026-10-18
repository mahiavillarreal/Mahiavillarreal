# Desafío 30: Algoritmo del Máximo Común Divisor (MCD)
# Este programa crea una función que calcula el
# Máximo Común Divisor de dos números utilizando
# el algoritmo de Euclides.


print("Desafío 30: Algoritmo del Máximo Común Divisor")




# Crear una función para calcular el MCD
def calcular_mcd(numero1, numero2):


    # Repetir el proceso hasta que el segundo número sea 0
    while numero2 != 0:


        # Aplicar el algoritmo de Euclides
        numero1, numero2 = numero2, numero1 % numero2


    # Devolver el MCD encontrado
    return numero1




# Crear la función principal del programa
def main():


    # Solicitar al usuario los dos números
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))


    print()


    # Llamar a la función
    resultado = calcular_mcd(numero1, numero2)


    # Mostrar el resultado
    print("El Máximo Común Divisor es:", resultado)




# Ejecutar el programa
if __name__ == "__main__":
    main()