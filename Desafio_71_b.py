# Desafío 71: Lectura de archivos y manejo de excepciones


from pathlib import Path


# Ubicación del archivo de texto
ruta = Path(__file__).resolve().parent / "desafio_71_ejemplo.txt"


# Crear un archivo de ejemplo si todavía no existe
if not ruta.exists():
    with open(ruta, "w", encoding="utf-8") as nuevo:
        nuevo.write("Bienvenidos al Desafío 71.\n")
        nuevo.write("Estamos aprendiendo a leer archivos con Python.\n")


archivo = None


try:
    archivo = open(ruta, "r", encoding="utf-8")
    contenido = archivo.read()


    print("CONTENIDO DEL ARCHIVO:")
    print(contenido)


except FileNotFoundError:
    print("Error: El archivo no existe.")


except OSError as error:
    print("Error al abrir o leer el archivo:", error)


finally:
    if archivo is not None:
        archivo.close()
        print("El archivo se cerró correctamente.")


    print("Fin del programa.")


