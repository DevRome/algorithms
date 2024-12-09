from binarytree import Node

# Creare un albero binario
radice = Node(10)
radice.left = Node(5)
radice.right = Node(15)
radice.left.left = Node(2)
radice.left.right = Node(7)

# Stampare l'albero
print(radice)
