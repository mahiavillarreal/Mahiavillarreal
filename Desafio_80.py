# Desafío 80: Evaluación de expresiones matemáticas con árboles


# Clase para representar los nodos del árbol
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None




# Función para construir el árbol de expresiones
def construir_arbol(expresion):


    # Separar números y operadores
    tokens = expresion.split()


    # Listas para almacenar nodos y operadores
    nodos = []
    operadores = []


    # Establecer la precedencia de los operadores
    prioridad = {"+": 1, "-": 1, "*": 2, "/": 2}


    # Crear un nodo operador con dos hijos
    def crear_nodo():
        operador = operadores.pop()


        nuevo_nodo = Nodo(operador)
        nuevo_nodo.derecha = nodos.pop()
        nuevo_nodo.izquierda = nodos.pop()


        nodos.append(nuevo_nodo)


    # Recorrer los elementos de la expresión
    for token in tokens:


        if token not in prioridad:
            # Crear un nodo para cada número entero
            nodos.append(Nodo(int(token)))


        else:
            # Respetar la prioridad de las operaciones
            while (operadores and
                   prioridad[operadores[-1]] >= prioridad[token]):
                crear_nodo()


            operadores.append(token)


    # Procesar los operadores restantes
    while operadores:
        crear_nodo()


    # Devolver la raíz del árbol
    return nodos[0]




# Función recursiva para evaluar el árbol
def evaluar_arbol(nodo):


    # Si el nodo contiene un número, devolverlo
    if nodo.izquierda is None and nodo.derecha is None:
        return nodo.valor


    # Evaluar los subárboles izquierdo y derecho
    izquierda = evaluar_arbol(nodo.izquierda)
    derecha = evaluar_arbol(nodo.derecha)


    # Realizar la operación correspondiente
    if nodo.valor == "+":
        return izquierda + derecha


    elif nodo.valor == "-":
        return izquierda - derecha


    elif nodo.valor == "*":
        return izquierda * derecha


    elif nodo.valor == "/":
        return izquierda / derecha




# Programa principal
if __name__ == "__main__":


    print("DESAFÍO 80: ÁRBOL DE EXPRESIONES")
    print()


    # Expresión matemática solicitada
    expresion = "5 + 3 * 4"


    # Construir el árbol
    arbol = construir_arbol(expresion)


    # Evaluar el árbol
    resultado = evaluar_arbol(arbol)


    # Mostrar los resultados
    print("Expresión matemática:", expresion)
    print("Resultado de la expresión:", resultado)
