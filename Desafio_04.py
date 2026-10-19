print ("Solución para el desafío 4")
entrada = input ("Introduce una lista de numeros enteros: ")
lista_texto = entrada.split(",")
cantidad_pares = 0
for texto in lista_texto:
    numero = int (texto.strip())
    if numero % 2 == 0:
        cantidad_pares =cantidad_pares + 1
print ("Cantidad de numeros pares:", cantidad_pares)
