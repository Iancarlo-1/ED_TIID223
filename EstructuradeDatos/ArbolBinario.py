class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


raiz = Nodo(1)

raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)

raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)

raiz.derecha.izquierda = Nodo(6)
raiz.derecha.derecha = Nodo(7)


def imprimir_arbol(nodo, nivel=0, prefijo="Raiz: "):
    if nodo is not None:
        print("  " * nivel + prefijo + str(nodo.valor))
        imprimir_arbol(nodo.izquierda, nivel + 1, "Izquierda: ")
        imprimir_arbol(nodo.derecha, nivel + 1, "Derecha: ")


imprimir_arbol(raiz)
