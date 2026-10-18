# Desafío 78: Árbol binario y valor máximo en postorden


# Clase que representa un nodo del árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None




# Función recursiva para recorrer el árbol en postorden
# y devolver el valor máximo encontrado
def maximo_postorden(nodo):


    # Caso base: si el nodo no existe
    if nodo is None:
        return None


    # 1. Recorrer el subárbol izquierdo
    max_izquierda = maximo_postorden(nodo.izquierda)


    # 2. Recorrer el subárbol derecho
    max_derecha = maximo_postorden(nodo.derecha)


    # 3. Visitar el nodo actual
    print(nodo.valor, end=" ")


    # Comparar los valores encontrados
    maximo = nodo.valor


    if max_izquierda is not None:
        maximo = max(maximo, max_izquierda)


    if max_derecha is not None:
        maximo = max(maximo, max_derecha)


    return maximo




# Programa principal
if __name__ == "__main__":


    print("DESAFÍO 78: RECORRIDO EN POSTORDEN")
    print()


    # Construir el árbol binario
    raiz = Nodo(10)


    # Segundo nivel
    raiz.izquierda = Nodo(5)
    raiz.derecha = Nodo(15)


    # Tercer nivel
    raiz.izquierda.izquierda = Nodo(3)
    raiz.izquierda.derecha = Nodo(7)
    raiz.derecha.izquierda = Nodo(12)
    raiz.derecha.derecha = Nodo(20)


    # Recorrer el árbol y encontrar el máximo
    print("Recorrido en postorden:")
    valor_maximo = maximo_postorden(raiz)


    # Mostrar el resultado final
    print()
    print("Valor máximo del árbol:", valor_maximo)
