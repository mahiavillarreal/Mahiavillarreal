# Desafío 38: Uso del módulo os en un procesador de texto

# Este programa utiliza el módulo os para interactuar con el sistema operativo.
# Permite guardar un texto en un archivo y leer el contenido
# de un archivo existente.

import os

# Guardar el archivo junto al script, sin importar desde dónde se ejecute
CARPETA_SCRIPT = os.path.dirname(os.path.abspath(__file__))


def obtener_ruta(nombre_archivo):
    """Devuelve la ruta completa del archivo, dentro de la carpeta del script."""
    return os.path.join(CARPETA_SCRIPT, nombre_archivo)


def guardar_archivo(ruta, contenido):
    """Guarda un texto dentro de un archivo. Devuelve True si salió bien."""

    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)
    except OSError as error:
        print(f"No se pudo guardar el archivo: {error}")
        return False

    print("Archivo guardado correctamente.")
    return True


def leer_archivo(ruta):
    """Lee y devuelve el contenido de un archivo, o None si no existe."""

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except FileNotFoundError:
        return None
    except OSError as error:
        print(f"No se pudo leer el archivo: {error}")
        return None


def main():
    print("Desafío 38: Guardar y leer archivos\n")

    # Pedir un texto no vacío
    while True:
        texto = input("Ingrese un texto para guardar: ").strip()
        if texto:
            break
        print("El texto no puede estar vacío.\n")

    ruta = obtener_ruta("texto_guardado.txt")

    print()

    # Si algo falla al guardar, no tiene sentido seguir
    if not guardar_archivo(ruta, texto):
        return

    # Mostrar dónde se guardó y cuánto pesa (usando os)
    print(f"\nUbicación: {ruta}")
    print(f"Tamaño: {os.path.getsize(ruta)} bytes\n")

    # Leer nuevamente el archivo
    contenido = leer_archivo(ruta)

    if contenido is not None:
        print("Contenido del archivo:")
        print(contenido)
    else:
        print("No se pudo leer el archivo.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma cancelado por el usuario.")