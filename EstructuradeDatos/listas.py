class Nodo:
    def _init_(self,dato):
        self.dato = dato
        self.siguiente = None

class LinkedList:
    def _init_(self):
        self.head = None


#agregar y mostrar elelmentos

    def agregar(self,dato):
        nuevo = Nodo(dato) #creamos un nuevo nodo con el dato
        if not self.head:   #la cabeza pasa a ser el nodo creado (nuevo)
            self.head = nuevo
        else:  #vamos a recorrer desde la cabeza hasta el nodo que su siguiente dato sea None
            actual = self.head
            while actual.siguiente:
              actual = actual.siguiente
            actual.siguiente = nuevo


            #mostrar elementos
    def mostrar(self):
        actual = self.head
        print("Cancion actual: ", actual.dato, "\n")
        print("Pila de reproduccion:")

        while actual:  #recorremos desde la cabeza hasta que el ultimo sea None
            print("",actual.dato,"\n", end=" -> ")
            actual = actual.siguiente
        print("Fin de la lista de reproduccion")


    def eliminar(self,dato):
        actual = self.head
        anterior = None
        while actual and actual.dato != dato: #recorremos la lista nodo por nodo hasta encontrar el que queremos borrar
            #si lo encontramos "actual" se queda apuntando a ese nodo, y si no lo encontramos  acta termina en None
            anterior = actual
            actual = actual.siguiente
        if not actual:
            return
        if not anterior: #significa que el nodo a eliminar es la cabeza
            self.head = actual.siguiente

        else:
            anterior.siguiente = actual.siguiente



lista = LinkedList()
lista.agregar("Nos hizo falta tiempo - Luis Miguel")
lista.agregar("Cuestion de piel - Luis Miguel")
lista.agregar("Me niego a estar solo - Luis Miguel")
lista.agregar("Yo se que volveras - Luis Miguel")
lista.agregar("Un te amo - Luis Miguel")


lista.mostrar()