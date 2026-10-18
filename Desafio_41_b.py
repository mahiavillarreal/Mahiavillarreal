# Desafío 41: Resaltar palabras utilizando recursividad


# Este programa utiliza el módulo personalizado procesador_texto
# para resaltar recursivamente todas las apariciones
# de una palabra clave dentro de un texto.


import desafio_41_procesador_texto as procesador_texto


def resaltar_ocurrencias(texto, palabra_clave):
    """Resalta recursivamente todas las apariciones de una palabra."""


    # Buscar la primera aparición de la palabra clave
    posicion = texto.lower().find(palabra_clave.lower())


    # Caso base:
    # Si la palabra no aparece, devolver el texto restante
    if posicion == -1:
        return texto


    # Separar el texto antes de la palabra encontrada
    texto_anterior = texto[:posicion]


    # Obtener la palabra encontrada respetando su escritura original
    palabra_encontrada = texto[
        posicion:posicion + len(palabra_clave)
    ]


    # Obtener el resto del texto
    texto_restante = texto[
        posicion + len(palabra_clave):
    ]


    # Resaltar la palabra utilizando el módulo personalizado
    palabra_resaltada = procesador_texto.resaltar(
        palabra_encontrada
    )


    # Caso recursivo:
    # Procesar nuevamente el texto restante
    return (
        texto_anterior
        + palabra_resaltada
        + resaltar_ocurrencias(texto_restante, palabra_clave)
    )




def main():
    """Solicita el texto y la palabra que se desea resaltar."""


    print("Desafío 41: Resaltar palabras recursivamente")
    print()


    # Solicitar los datos al usuario
    texto = input("Ingrese un texto: ")
    palabra_clave = input("Ingrese la palabra que desea resaltar: ")


    print()


    # Evitar trabajar con una palabra clave vacía
    if palabra_clave == "":
        print("Debe ingresar una palabra para resaltar.")
        return


    # Llamar a la función recursiva
    resultado = resaltar_ocurrencias(texto, palabra_clave)


    # Mostrar los resultados
    print("Texto original:")
    print(texto)


    print()
    print("Texto con la palabra resaltada:")
    print(resultado)




# Ejecutar el programa
if __name__ == "__main__":
    main()