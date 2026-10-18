# Desafío 76: Árbol binario y recorrido en preorden


# Clase que representa un nodo del árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None




# Función para recorrer el árbol en preorden
def recorrer_preorden(nodo):
    if nodo is not None:
        # 1. Visitar la raíz
        print(nodo.valor, end=" ")


        # 2. Recorrer el subárbol izquierdo
        recorrer_preorden(nodo.izquierda)


        # 3. Recorrer el subárbol derecho
        recorrer_preorden(nodo.derecha)




# Programa principal
if __name__ == "__main__":
    print("DESAFÍO 76: ÁRBOL BINARIO")
    print()


    # Nivel 1: raíz del árbol
    raiz = Nodo(10)


    # Nivel 2: hijos de la raíz
    raiz.izquierda = Nodo(5)
    raiz.derecha = Nodo(15)


    # Nivel 3: hijos de los nodos del segundo nivel
    raiz.izquierda.izquierda = Nodo(3)
    raiz.izquierda.derecha = Nodo(7)


    raiz.derecha.izquierda = Nodo(12)
    raiz.derecha.derecha = Nodo(20)


    # Mostrar el recorrido en preorden
    print("Recorrido en preorden:")
    recorrer_preorden(raiz)
    print()


