# .:: Albero Statistiche D'ordine - Strutture Dati Avanzate ::.
# Arricchimento delle strutture dati
# UniMarconi - Corso Algoritmi e Strutture Dati

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1
    
    def insert(root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.roght = insert(root.right, key)
        root.size += 1
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
            root.right = delete (root.right, temp.key)
        root.size -= 1
        return root
    
    def minValueNode(node):
        current = node 
        while current.left is not None:
            current = current.left
        return current
    
    def kth_smallest(root, k):
        if root is None:
            return None
        left_size = root.left.size if root.left else 0
        if k <= left.size:
            return kth_smallest(root.left, k)
        elif k == left.size + 1:
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