from collections import deque

def programa_colas():
    cola = deque()
    
    while True:
        print("\n--- MENÚ DE COLAS ---")
        print("1. Insertar cola")
        print("2. Borrar en cola")
        print("3. Listar cola")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            try:
                numero = float(input("Ingrese un número para añadir a la cola: "))
                cola.append(numero)
                print(f"Número {numero} añadido a la cola.")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
                
        elif opcion == '2':
            if len(cola) > 0:
                eliminado = cola.popleft()
                print(f"Elemento {eliminado} eliminado de la cola.")
            else:
                print("La cola está vacía, no hay elementos para borrar.")
                
        elif opcion == '3':
            if len(cola) > 0:
                print("Elementos en la cola (Primero -> Último):", list(cola))
            else:
                print("La cola está vacía.")
                
        elif opcion == '4':
            print("Saliendo del menú de colas...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ciclo principal para preguntar si desea volver a ejecutar el programa
def main():
    mientras_ejecutando = True
    while mientras_ejecutando:
        programa_colas()
        respuesta = input("\n¿Desea ejecutar nuevamente el programa de colas? (s/n): ").strip().lower()
        if respuesta != 's':
            mientras_ejecutando = False
            print("¡Hasta luego!")

if __name__ == "__main__":
    main()