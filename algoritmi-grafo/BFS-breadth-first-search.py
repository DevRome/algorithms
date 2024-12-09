# .:: BFS breadth::.
# Micheal Sambol - fonte youtube 

graph = {
    "A": ["B", "C"],
    "B": ["D", "E", "F"],
    "C": ["G"],
    "D": [],
    "E": [],
    "F": ["H"],
    "G": ["I"],
    "H": [],
    "I": [],
}

def bfs(graph, node):
    visited = []
    queue = []

    # aggiungiamo il node in lettura alle liste
    visited.append(node)
    queue.append(node)

    # iteriamo finché il loop NON è vuoto
    while queue:
        s = queue.pop(0) # rimuoviamo il node che è stato aggiunto alla queue per primo
        print(s, end = " ")

        # iteriamo sugli node degli altri edges
        for n in graph[s]:
            # se il node in questione NON è stato visitato, lo aggiungiamo alle liste
            if n not in visited:
                visited.append(n)
                queue.append(n)