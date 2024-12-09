from anytree import Node, RenderTree

# Creare nodi
radice = Node("Radice")
figlio1 = Node("Figlio 1", parent=radice)
figlio2 = Node("Figlio 2", parent=radice)
figlio1_1 = Node("Figlio 1.1", parent=figlio1)

# Stampare l'albero
for pre, fill, nodo in RenderTree(radice):
    print(f"{pre}{nodo.name}")
