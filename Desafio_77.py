# Desafío 77: Recorrido en inorden y suma de nodos


# Clase que representa un nodo del árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None




# Función recursiva que recorre el árbol en inorden
# y devuelve la suma de todos sus nodos
def sumar_inorden(nodo):


    # Si no hay nodo, su valor para la suma es 0
    if nodo is None:
        return 0


    # 1. Recorrer y sumar el subárbol izquierdo
    suma_izquierda = sumar_inorden(nodo.izquierda)


    # 2. Visitar el nodo actual
    print(nodo.valor, end=" ")


    # 3. Recorrer y sumar el subárbol derecho
    suma_derecha = sumar_inorden(nodo.derecha)


    # Devolver la suma de izquierda, raíz y derecha
    return suma_izquierda + nodo.valor + suma_derecha




# Programa principal
if __name__ == "__main__":


    print("DESAFÍO 77: RECORRIDO EN INORDEN")
    print()


    # Construir un árbol binario de tres niveles
    raiz = Nodo(10)


    # Segundo nivel
    raiz.izquierda = Nodo(5)
    raiz.derecha = Nodo(15)


    # Tercer nivel
    raiz.izquierda.izquierda = Nodo(3)
    raiz.izquierda.derecha = Nodo(7)
    raiz.derecha.izquierda = Nodo(12)
    raiz.derecha.derecha = Nodo(20)


    # Recorrer el árbol y calcular la suma
    print("Recorrido en inorden:")
    suma_total = sumar_inorden(raiz)


    # Mostrar el resultado final
    print()
    print("Suma total de los nodos:", suma_total)
