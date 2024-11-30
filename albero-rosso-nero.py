# .:: Albero Rosso Nero - Strutture Dati Avanzate ::.
# Arricchimento delle strutture dati
# UniMarconi - Corso Algoritmi e Strutture Dati

class TreeNode:
    def __init__(self, key, color, size=1):
        self.key = key
        self.color = color
        self.size = size
        self.left = None
        self.right = None
        self.parent = None

    def insert(root, key):
        if root is None:
            return TreeNode(key, "red")
        if key < root.key:
            root.left = insert(root.left, key)
            root.left.parent = root
        else:
            root.right = insert(root.right, key)
            root.right.parent = root
        root.size = 1 + (root.left.size if root.left else 0) + (root.right.size if root.right else 0)
        return root
    
    def delete(root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = delete(root.left, key)
        elif key > root.key:
            root.right = delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = minValueNode(root.right)
            root.key = temp.key
            root.right = delete(root.right, temp.key)
        root.size = 1 + (root.left.size if root.left else 0) + (root.right.size if root.right else 0)
        return root

    def minValueNode(node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # rotazione
    def left_rotate(root, x):
        y = x.right
        x.right = y.left
        
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent

        if x.parent is None:
            root = y
        elif x == x.parent.left:
            x.parent.left = y
        else: x.parent.right = y
        y.left = x
        x.parent = y

        # aggiornare le dimenioni dei sottoalberi
        x.size = 1 + (x.left.size if x.left else 0) + (x.right.size if x.right else 0)
        y.size = 1 + (y.left.size if y.left else 0) + (y.right.size if y.right else 0)
        return root
    
    def right_rotate(root, y):
        x = y.left
        y.left = x.right
        if x.right is not None:
            x.righr.parent = y
        x.parent = y.parent
        if y.parent is None:
            root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.prent.left = x
        x.right = y
        y.parent = x

        #aggiornare le dimenioni dei sottoalberi
        y.size = 1 + (y.left.size if y.left else 0) + (y.right.size if y.right else 0)
        x.size = 1 + (x.left.size if x.left else 0) + (x.right.size if x.right else 0)
        return root
    
    # ricerca del k-esimo elementio più piccolo
    def kth_smallest(root, k):
        if root is None:
            return None
        left_size = root.left.size if root.left else 0
        if k <= left_size:
            return kth_smallest(root.left, k)
        elif k == left_size + 1:
            return root.key
        else:
            return kth_smallest(root.right, k - left_size - 1)
    
    def rank(root, key):
        if root is None:
            return 0
        if key < root.key:
            return rank(root.left, key)
        elif key == root.key:
            return root.left.size if root.left else 0
        else:
            return 1 + (root.left.size if root.left else 0) + rank(root.right, key)
            