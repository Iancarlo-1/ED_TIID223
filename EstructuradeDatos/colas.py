from collections import deque
""" Crear la cola """
cola = deque (["Ana", "Carlos"])
cola.append("Jorge")
cola.append("Carlos")
print("Cola actual:", cola)

atendido = cola.popleft
print(f"Se atendio a :{atendido}")
print("Cola restante", cola)

atendido = cola.popleft()
print(f"Se atendio a: {atendido}")
print("Cola restante", cola)