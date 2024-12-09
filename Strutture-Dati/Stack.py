# .:: Stack - Pile ::.

stack = []

# Aggiungere elementi (push)
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack dopo push:", stack)  # Output: [10, 20, 30]

# Rimuovere elementi (pop)
elemento = stack.pop()
print("Elemento rimosso:", elemento)  # Output: 30
print("Stack dopo pop:", stack)       # Output: [10, 20]



# Secondo esempio di stack
# con libreria deque, più performante
from collections import deque

stack = deque()

# Aggiungere elementi
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack dopo push:", stack)  # Output: deque([10, 20, 30])

# Rimuovere elementi
elemento = stack.pop()
print("Elemento rimosso:", elemento)  # Output: 30
print("Stack dopo pop:", stack)       # Output: deque([10, 20])

