from collections import deque


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


def construir_arbol():
    entrada_raiz = input("Valor para la raiz (enter para cancelar): ").strip()
    if not entrada_raiz:
        return None

    raiz = Nodo(entrada_raiz)
    cola = deque([raiz])

    while cola:
        nodo_actual = cola.popleft()

        while True:
            opcion = input(
                f"Nodo actual [{nodo_actual.valor}] - ¿Agregar (i)zquierdo, "
                f"(d)erecho, (s)iguiente nodo o (t)erminar?: "
            ).strip().lower()

            if opcion == "i":
                if nodo_actual.izquierda is not None:
                    print("Ese nodo ya tiene hijo izquierdo.")
                    continue
                valor_izq = input("-> Valor para el hijo izquierdo: ").strip()
                if valor_izq != "":
                    nuevo_izq = Nodo(valor_izq)
                    nodo_actual.izquierda = nuevo_izq
                    cola.append(nuevo_izq)

            elif opcion == "d":
                if nodo_actual.derecha is not None:
                    print("Ese nodo ya tiene hijo derecho.")
                    continue
                valor_der = input("-> Valor para el hijo derecho: ").strip()
                if valor_der != "":
                    nuevo_der = Nodo(valor_der)
                    nodo_actual.derecha = nuevo_der
                    cola.append(nuevo_der)

            elif opcion == "s":
                break

            elif opcion == "t":
                return raiz

            else:
                print("Opcion no valida. Usa i, d, s o t.")

    return raiz


def imprimir_arbol(nodo, nivel=0, prefijo="Raiz: "):
    if nodo is not None:
        print("  " * nivel + prefijo + str(nodo.valor))
        imprimir_arbol(nodo.izquierda, nivel + 1, "Izquierda: ")
        imprimir_arbol(nodo.derecha, nivel + 1, "Derecha: ")


if __name__ == "__main__":
    raiz = construir_arbol()
    print("\n--- Arbol resultante ---")
    imprimir_arbol(raiz)