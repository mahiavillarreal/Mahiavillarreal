print ("Solucion para el desafio 3")
n = int (input("Ingrese un numero entero positivo: "))
resultado = 0
for numero in range (1, n + 1):
    resultado = resultado + numero
print ("La suma de los primeros", n, "numeros naturales es: ", resultado)