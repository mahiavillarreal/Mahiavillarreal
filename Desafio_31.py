# Desafío 31: Palíndromo
# Este programa crea una función llamada es_palindromo
# que recibe una cadena de texto y devuelve True
# si es un palíndromo o False en caso contrario.
# Funciona con palabras y también con frases.

import unicodedata


def normalizar(cadena):
    """Deja solo letras y números, en minúsculas y sin tildes."""

    # Convertir a minúsculas
    cadena = cadena.lower()

    # Separar las tildes de las letras (á -> a + ´) y descartarlas
    cadena = unicodedata.normalize("NFD", cadena)
    cadena = "".join(c for c in cadena if unicodedata.category(c) != "Mn")

    # Conservar solo letras y números (quita espacios y signos)
    return "".join(c for c in cadena if c.isalnum())


def es_palindromo(cadena):
    """Devuelve True si la cadena se lee igual al derecho y al revés."""

    limpia = normalizar(cadena)

    # Comparar la cadena con su versión invertida
    return limpia == limpia[::-1]


def main():
    print("Desafío 31: Palíndromo\n")

    # Pedir texto hasta que el usuario escriba algo válido
    while True:
        texto = input("Ingrese una palabra o frase: ").strip()

        if normalizar(texto):
            break

        print("Debe ingresar al menos una letra o número.\n")

    print()

    if es_palindromo(texto):
        print(f'"{texto}" es un palíndromo.')
    else:
        print(f'"{texto}" no es un palíndromo.')


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Evita el traceback si el usuario cancela con Ctrl + C
        print("\nPrograma cancelado por el usuario.")