# Desafío 73: Eliminar elementos duplicados de una lista


def eliminar_duplicados(lista):
    """Devuelve una lista sin duplicados, conservando el orden original."""
    sin_duplicados = []

    for elemento in lista:
        if elemento not in sin_duplicados:
            sin_duplicados.append(elemento)

    return sin_duplicados


def main():
    print("Desafío 73: Eliminar duplicados de una lista")
    print()

    numeros = [4, 7, 2, 7, 9, 4, 1, 2, 9, 5, 1]

    resultado = eliminar_duplicados(numeros)

    print("Lista original:     ", numeros)
    print("Lista sin duplicados:", resultado)


if __name__ == "__main__":
    main()