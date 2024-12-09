import heapq

def dijkstra(grafo, sorgente):
    """
    Implementa l'algoritmo di Dijkstra per trovare le distanze minime da un nodo sorgente.

    Args:
        grafo: Dizionario dove le chiavi sono nodi e i valori sono liste di tuple (vicino, peso).
        sorgente: Nodo di partenza.

    Returns:
        distanze: Dizionario con la distanza minima da 'sorgente' a ogni nodo.
    """
    # Inizializza le distanze come infinito per tutti i nodi, eccetto la sorgente
    distanze = {nodo: float('inf') for nodo in grafo}
    distanze[sorgente] = 0

    # Coda di priorità per esplorare i nodi in base alla distanza minima
    coda = [(0, sorgente)]  # (distanza, nodo)

    while coda:
        distanza_corrente, nodo_corrente = heapq.heappop(coda)

        # Salta i nodi già esplorati con una distanza migliore
        if distanza_corrente > distanze[nodo_corrente]:
            continue

        # Esplora i vicini
        for vicino, peso in grafo[nodo_corrente]:
            distanza = distanza_corrente + peso

            # Se troviamo una distanza migliore, aggiorna e inserisci nella coda
            if distanza < distanze[vicino]:
                distanze[vicino] = distanza
                heapq.heappush(coda, (distanza, vicino))

    return distanze

# Esempio di utilizzo
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 6)],
    'C': [('A', 4), ('B', 2), ('D', 3)],
    'D': [('B', 6), ('C', 3)]
}

sorgente = 'A'
distanze = dijkstra(grafo, sorgente)
print("Distanze minime dalla sorgente:", distanze)
