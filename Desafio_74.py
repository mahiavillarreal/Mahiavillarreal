# Desafío 74: Suma de listas de diferentes longitudes


def sumar_listas(lista1, lista2):
    resultado = []


    # Obtener la longitud de la lista más larga
    longitud_maxima = max(len(lista1), len(lista2))


    # Recorrer las posiciones de ambas listas
    for i in range(longitud_maxima):


        # Si falta un elemento, se utiliza el valor 0
        if i < len(lista1):
            numero1 = lista1[i]
        else:
            numero1 = 0


        if i < len(lista2):
            numero2 = lista2[i]
        else:
            numero2 = 0


        # Sumar y guardar el resultado
        suma = numero1 + numero2
        resultado.append(suma)


    return resultado




# Programa principal
print("DESAFÍO 74: SUMA DE LISTAS")
print()


lista1 = [10, 20, 30, 40, 50]
lista2 = [5, 15, 25]


lista_resultado = sumar_listas(lista1, lista2)


print("Primera lista:", lista1)
print("Segunda lista:", lista2)
print("Lista resultante:", lista_resultado)


