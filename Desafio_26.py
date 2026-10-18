# Desafío 26: Juego de la Vida de Conway
# Este programa simula la evolución de células vivas y muertas
# en un tablero utilizando NumPy y Matplotlib.


print("Desafío 26: Juego de la Vida de Conway")


# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation




# Crear un tablero con un patrón inicial
def crear_tablero(filas, columnas):


    # Crear una matriz llena de ceros
    tablero = np.zeros((filas, columnas), dtype=int)


    # Colocar un patrón inicial en el centro del tablero
    centro_fila = filas // 2
    centro_columna = columnas // 2


    tablero[centro_fila - 1, centro_columna] = 1
    tablero[centro_fila, centro_columna + 1] = 1
    tablero[centro_fila + 1, centro_columna - 1] = 1
    tablero[centro_fila + 1, centro_columna] = 1
    tablero[centro_fila + 1, centro_columna + 1] = 1


    return tablero




# Contar los vecinos vivos de una celda
def contar_vecinos(tablero, fila, columna):


    vecinos_vivos = 0
    filas, columnas = tablero.shape


    for desplazamiento_fila in range(-1, 2):
        for desplazamiento_columna in range(-1, 2):


            # No contar la propia celda
            if desplazamiento_fila == 0 and desplazamiento_columna == 0:
                continue


            fila_vecina = fila + desplazamiento_fila
            columna_vecina = columna + desplazamiento_columna


            # Verificar que el vecino esté dentro del tablero
            if (
                0 <= fila_vecina < filas
                and 0 <= columna_vecina < columnas
            ):
                vecinos_vivos += tablero[fila_vecina, columna_vecina]


    return vecinos_vivos




# Crear la siguiente generación del tablero
def actualizar_tablero(tablero):


    nuevo_tablero = np.zeros_like(tablero)
    filas, columnas = tablero.shape


    for fila in range(filas):
        for columna in range(columnas):


            vecinos = contar_vecinos(tablero, fila, columna)


            # Una celda viva continúa viva con 2 o 3 vecinos
            if tablero[fila, columna] == 1 and vecinos in (2, 3):
                nuevo_tablero[fila, columna] = 1


            # Una celda muerta nace con exactamente 3 vecinos
            elif tablero[fila, columna] == 0 and vecinos == 3:
                nuevo_tablero[fila, columna] = 1


    return nuevo_tablero




# Visualizar la evolución del tablero
def mostrar_simulacion(tablero, iteraciones):


    figura, eje = plt.subplots()
    imagen = eje.imshow(tablero, cmap="binary", vmin=0, vmax=1)


    eje.set_xticks([])
    eje.set_yticks([])


    def animar(generacion):


        # Actualizar el tablero completo
        tablero[:] = actualizar_tablero(tablero)


        # Actualizar la imagen
        imagen.set_data(tablero)
        eje.set_title("Generación " + str(generacion + 1))


        return [imagen]


    animacion = FuncAnimation(
        figura,
        animar,
        frames=iteraciones,
        interval=500,
        repeat=False
    )


    plt.show()

    # Mantener la animación guardada mientras se muestra
    return animacion


# Función principal
def main():


    # Crear un tablero de 20 filas y 20 columnas
    tablero = crear_tablero(20, 20)


    # Mostrar el tablero inicial
    print("Tablero inicial:")
    print(tablero)


    # Mostrar 50 generaciones
    mostrar_simulacion(tablero, 50)




# Ejecutar el programa
if __name__ == "__main__":
    main()