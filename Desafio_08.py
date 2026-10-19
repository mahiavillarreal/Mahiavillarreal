# Muestra el título del programa
print ("Solución para el desafío 8")
# Solicita un número entero al usuario
numero = int (input ("Ingrese un numero entero: "))
# Lista de divisores a comprobar
divisores = [2, 3, 5, 7, 9, 10, 11]
# Recorre cada divisor de la lista
for divisor in divisores:    
    # Verifica si el número es múltiplo del divisor
    if numero % divisor ==0:
        print (f"El numero {numero} es multiplo de (divisor)")
    # Si no es múltiplo, muestra otro mensaje
    else:
        print (f"El numero {numero} NO es multiplo de (divisor)")
