def programa_pilas():
    pila = []
    
    while True:
        print("\n--- MENÚ DE PILAS ---")
        print("1. Insertar en pila")
        print("2. Borrar en pila")
        print("3. Listar pila")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            try:
                numero = float(input("Ingrese un número para apilar: "))
                pila.append(numero)
                print(f"Número {numero} apilado con éxito.")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
                
        elif opcion == '2':
            if len(pila) > 0:
                eliminado = pila.pop()
                print(f"Elemento {eliminado} desapilado (borrado).")
            else:
                print("La pila está vacía, no hay elementos para borrar.")
                
        elif opcion == '3':
            if len(pila) > 0:
                print("Elementos en la pila (Inicio -> Fin):", pila)
            else:
                print("La pila está vacía.")
                
        elif opcion == '4':
            print("Saliendo del menú de pilas...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


def main():
    mientras_ejecutando = True
    while mientras_ejecutando:
        programa_pilas()
        respuesta = input("\n¿Desea ejecutar nuevamente el programa de pilas? (s/n): ").strip().lower()
        if respuesta != 's':
            mientras_ejecutando = False
            print("¡Hasta luego!")

if __name__ == "__main__":
    main()