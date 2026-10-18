# Desafío 40: Máximo Común Divisor con recursividad

# Este programa calcula el Máximo Común Divisor (MCD) de dos números
# mediante una función recursiva y el algoritmo de Euclides.


# Crear una función recursiva para calcular el MCD
def calcular_mcd(a, b):
    # Caso base:
    # Si el segundo número es 0, el MCD es el primer número
    if b == 0:
        return abs(a)

    # Caso recursivo:
    # Aplicar el algoritmo de Euclides llamando nuevamente
    # a la función con b y el residuo de dividir a entre b
    return calcular_mcd(b, a % b)


# Crear la función principal del programa
def main():
    print("Desafío 40: Máximo Común Divisor con recursividad")
    print()

    # Solicitar dos números enteros al usuario
    try:
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: debe ingresar números enteros.")
        return

    # Calcular el MCD utilizando la función recursiva
    resultado = calcular_mcd(numero1, numero2)

    print()

    # Mostrar el resultado
    print("El MCD de", numero1, "y", numero2, "es:", resultado)


# Ejecutar el programa desde la función principal
if __name__ == "__main__":
    main()