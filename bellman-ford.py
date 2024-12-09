def bellman_ford(grafo, sorgente):
    """
    Implementa l'algoritmo di Bellman-Ford per trovare le distanze minime e rilevare cicli negativi.

    Args:
        grafo: Lista di archi nel formato (origine, destinazione, peso).
        sorgente: Nodo sorgente.

    Returns:
        distanze: Dizionario con le distanze minime dal nodo sorgente.
        ciclo_negativo: Booleano, True se è presente un ciclo con peso negativo.
    """
    # Inizializza le distanze come infinito, tranne la sorgente
    nodi = {nodo for arco in grafo for nodo in arco[:2]}  # Estrae tutti i nodi
    distanze = {nodo: float('inf') for nodo in nodi}
    distanze[sorgente] = 0

    # Rilassa gli archi per |nodi| - 1 volte
    for _ in range(len(nodi) - 1):
        for origine, destinazione, peso in grafo:
            if distanze[origine] + peso < distanze[destinazione]:
                distanze[destinazione] = distanze[origine] + peso

    # Controlla la presenza di cicli con peso negativo
    for origine, destinazione, peso in grafo:
        if distanze[origine] + peso < distanze[destinazione]:
            return distanze, True  # Trovato un ciclo negativo

    return distanze, False


# Esempio di utilizzo
grafo = [
    ('A', 'B', 1),
    ('B', 'C', 3),
    ('A', 'C', 10),
    ('C', 'D', 2),
    ('D', 'B', -6)  # Ciclo con peso negativo
]

sorgente = 'A'
distanze, ciclo_negativo = bellman_ford(grafo, sorgente)

if ciclo_negativo:
    print("Il grafo contiene un ciclo con peso negativo.")
else:
    print("Distanze minime dalla sorgente:", distanze)
