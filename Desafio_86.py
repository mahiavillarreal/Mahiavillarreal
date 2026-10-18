# Desafío 86: Crear un archivo de préstamos de libros


from pathlib import Path




# Función para registrar un préstamo de libro
def registrar_prestamo(nombre_libro, prestatario, fecha):


    # Guardar el archivo en la misma carpeta que este programa
    ruta_archivo = Path(__file__).resolve().parent / "prestamos.txt"


    try:
        # Abrir el archivo en modo append para no borrar datos anteriores
        with open(ruta_archivo, "a", encoding="utf-8") as archivo:


            # Escribir los datos con un formato claro y legible
            archivo.write(f"Libro: {nombre_libro}\n")
            archivo.write(f"Prestatario: {prestatario}\n")
            archivo.write(f"Fecha del préstamo: {fecha}\n")
            archivo.write("------------------------------\n")


        print("\n¡Préstamo registrado correctamente!")
        return True


    except OSError as error:
        print(f"\nError al guardar el préstamo: {error}")
        return False




# Programa principal
if __name__ == "__main__":


    print("DESAFÍO 86: REGISTRO DE PRÉSTAMOS DE LIBROS")
    print()


    # Permitir registrar varios préstamos
    while True:


        # Solicitar los tres datos obligatorios
        nombre_libro = input("Ingrese el nombre del libro: ").strip()
        prestatario = input("Ingrese el nombre del prestatario: ").strip()
        fecha = input("Ingrese la fecha del préstamo: ").strip()


        # Comprobar que los campos no estén vacíos
        if nombre_libro and prestatario and fecha:


            # Guardar el préstamo sin sobrescribir los anteriores
            registrar_prestamo(nombre_libro, prestatario, fecha)


        else:
            print("\nError: Debe completar los tres campos.")


        # Preguntar si desea registrar otro préstamo
        print()
        continuar = input(
            "¿Desea registrar otro préstamo? (s/n): "
        ).strip().lower()


        if continuar != "s":
            print("\nPrograma finalizado.")
            break


        print()