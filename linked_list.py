class Node:

    """
    An object for storing a single node of a linked list
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return "<Node data: %s>" %self.data
    
# creo due Node
Node1 = Node(10)
Node2 = Node(20)

# concateno i Nodes
Node1.next_node = Node2

print(Node1.next_node)

# Creo una Singly Linked List
class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    # restituisce il numero di nodi nella lista, necessita di 0(n) linear time
    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next_node
        return count
    
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

# creo una LinkedList, gli aggiungo dei Node ed infine stampo la size
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
print(l.size())


