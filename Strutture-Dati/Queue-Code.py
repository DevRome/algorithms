# .:: Queue - Code ::.

from collections import deque

queue = deque()

# Aggiungere elementi (enqueue)
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue dopo enqueue:", queue)  # Output: deque([10, 20, 30])

# Rimuovere elementi (dequeue)
elemento = queue.popleft()
print("Elemento rimosso:", elemento)  # Output: 10
print("Queue dopo dequeue:", queue)   # Output: deque([20, 30])
