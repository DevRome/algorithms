# .:: DFS - Depth First Search ::.
# Micheal Sambol - fonte youtube 
graph = {
    "A": ["B", "G"],
    "B": ["C", "D", "E"],
    "C": [],
    "D": [],
    "E": ["F"],
    "F": [],
    "G": ["H"],
    "H": ["I"],
    "I": [],
}

def dfs(graph, node):
    visited = []
    stack = deque()

    # aggiungiamo il node in lettura alle liste
    visited.append(node)
    stack.append(node)

    # iteriamo finché il loop NON è vuoto
    while stack:
        s = stack.pop() # rimuoviamo il node in cima allo stack
        print(s, end = " ")

        # iteriamo sugli node degli altri edges
        for n in reversed(graph[s]):
            # se il node in questione NON è stato visitato, lo aggiungiamo alle liste
            if n not in visited:
                visited.append(n)
                stack.append(n)