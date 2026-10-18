# Desafío 29: Elementos en común entre dos listas
# Este programa crea una función que recibe dos listas
# y devuelve True si tienen al menos un elemento en común.
# En caso contrario, devuelve False.


def tienen_elemento_en_comun(lista1, lista2):
    """Devuelve True si las dos listas comparten al menos un elemento."""

    # Convertir la segunda lista en un conjunto (set) para que
    # cada búsqueda sea mucho más rápida (O(1) en promedio)
    conjunto2 = set(lista2)

    # Recorrer la primera lista y verificar si algún elemento
    # también está en el conjunto
    return any(elemento in conjunto2 for elemento in lista1)

    # Alternativa aún más corta:
    # return not set(lista1).isdisjoint(lista2)


def mostrar_resultado(lista1, lista2):
    """Muestra las listas y si tienen elementos en común."""

    print(f"Primera lista: {lista1}")
    print(f"Segunda lista: {lista2}")

    if tienen_elemento_en_comun(lista1, lista2):
        # Mostrar también cuáles son los elementos compartidos
        comunes = sorted(set(lista1) & set(lista2))
        print(f"Resultado: True (en común: {comunes})")
    else:
        print("Resultado: False (no tienen elementos en común)")

    print()


def main():
    print("Desafío 29: Elementos en común entre dos listas\n")

    # Casos de prueba
    mostrar_resultado([2, 5, 8, 10], [1, 4, 8, 9])   # Hay un elemento común
    mostrar_resultado([1, 2, 3], [4, 5, 6])           # No hay elementos comunes
    mostrar_resultado([], [1, 2, 3])                  # Lista vacía
    mostrar_resultado(["a", "b"], ["b", "c"])         # Funciona con cualquier tipo


if __name__ == "__main__":
    main()