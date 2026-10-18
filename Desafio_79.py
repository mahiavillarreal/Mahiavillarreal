# Desafío 79: Árbol de búsqueda binaria (ABB)


# Clase que representa un nodo del árbol
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None




# Función para insertar valores en el árbol
def insertar(nodo, valor):


    # Si no existe un nodo, crear uno nuevo
    if nodo is None:
        return Nodo(valor)


    # Los valores menores se insertan a la izquierda
    if valor < nodo.valor:
        nodo.izquierda = insertar(nodo.izquierda, valor)


    # Los valores mayores se insertan a la derecha
    elif valor > nodo.valor:
        nodo.derecha = insertar(nodo.derecha, valor)


    # Devolver la raíz del árbol o subárbol
    return nodo




# Función para buscar un valor en el árbol
def buscar(nodo, valor):


    # Si llegamos a un espacio vacío, no existe
    if nodo is None:
        return False


    # Si encontramos el valor, devolver True
    if valor == nodo.valor:
        return True


    # Buscar a la izquierda si es menor
    if valor < nodo.valor:
        return buscar(nodo.izquierda, valor)


    # Buscar a la derecha si es mayor
    return buscar(nodo.derecha, valor)




# Función para mostrar los valores ordenados
def mostrar_inorden(nodo):
    if nodo is not None:
        mostrar_inorden(nodo.izquierda)
        print(nodo.valor, end=" ")
        mostrar_inorden(nodo.derecha)




# Programa principal
if __name__ == "__main__":


    print("DESAFÍO 79: ÁRBOL DE BÚSQUEDA BINARIA")
    print()


    # Conjunto de números enteros únicos
    numeros = [50, 30, 70, 20, 40, 60, 80]


    # Construir el árbol insertando cada número
    raiz = None


    for numero in numeros:
        raiz = insertar(raiz, numero)


    print("Números ingresados:", numeros)


    # Mostrar el árbol mediante recorrido en inorden
    print("Valores del árbol en orden:")
    mostrar_inorden(raiz)
    print()


    # Solicitar un número para buscar
    print()
    try:
        numero_buscado = int(input("Ingrese un número para buscar: "))


        # Comprobar si el número existe en el árbol
        if buscar(raiz, numero_buscado):
            print(f"El número {numero_buscado} existe en el árbol.")
        else:
            print(f"El número {numero_buscado} no existe en el árbol.")


    except ValueError:
        print("Error: Debe ingresar un número entero válido.")



