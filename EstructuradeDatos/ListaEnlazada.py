class Nodo:
    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None


class ListasEnlazadas:
    def __init__(self):
        self.cabeza = None

    def insertar_Nodo_al_inicio(self, numero):
        nuevo_nodo = Nodo(numero)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        
        nuevo_nodo.siguiente = self.cabeza 
        self.cabeza = nuevo_nodo

    def insertar_Nodo_al_Final(self, numero):
        nuevo_nodo = Nodo(numero)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        
        
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
            
        actual.siguiente = nuevo_nodo 

     
    def eliminar_al_inicio(self):
        if self.cabeza is None:
            print("La lista está vacía, no hay elementos para eliminar.")
            return
        
        
        self.cabeza = self.cabeza.siguiente

   
    def eliminar_al_final(self):
        if self.cabeza is None:
            print("La lista está vacía, no hay elementos para eliminar.")
            return
        
        
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return
        
        
        actual = self.cabeza
        while actual.siguiente.siguiente is not None:
            actual = actual.siguiente
            
        
        actual.siguiente = None

    def Imprimir_Lista_Enlazada(self):
        actual = self.cabeza
        while actual:
            print(actual.numero, "->", end=" ")
            actual = actual.siguiente
        print("None")


Mi_Lista = ListasEnlazadas()

Mi_Lista.insertar_Nodo_al_inicio(5)
Mi_Lista.insertar_Nodo_al_inicio(4)
Mi_Lista.insertar_Nodo_al_inicio(3)
Mi_Lista.insertar_Nodo_al_inicio(6)
Mi_Lista.Imprimir_Lista_Enlazada()

print("\nEliminar al inicio")
Mi_Lista.eliminar_al_inicio()
Mi_Lista.Imprimir_Lista_Enlazada() 

print("\nEliminar al final")
Mi_Lista.eliminar_al_final()
Mi_Lista.Imprimir_Lista_Enlazada()