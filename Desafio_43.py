# Desafío 43: El mono que cuenta manzanas


def contar_manzanas(cantidad):


    # Caso base: si no hay manzanas, termina
    if cantidad == 0:
        return 0


    # El mono vuelve a contar desde 1 hasta cantidad
    print(f"El mono cuenta {cantidad} manzana(s).")


    # Acumula lo contado y llama nuevamente a la función
    return cantidad + contar_manzanas(cantidad - 1)




# Programa principal
if __name__ == "__main__":


    print("DESAFÍO 43: EL MONO QUE CUENTA MANZANAS")
    print()


    try:
        manzanas = int(input("Ingrese la cantidad de manzanas: "))


        if manzanas < 0:
            print("La cantidad no puede ser negativa.")
        else:
            total = contar_manzanas(manzanas)


            print()
            print(f"Cantidad de manzanas en la pila: {manzanas}")
            print(f"Total acumulado por el mono: {total}")


    except ValueError:
        print("Debe ingresar un número entero válido.")



