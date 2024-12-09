# Classe Nodo per un albero binario
class NodoBinario:
    def __init__(self, valore):
        self.valore = valore
        self.sinistro = None  # Figlio sinistro
        self.destro = None    # Figlio destro

# Creazione dell'albero binario
radice = NodoBinario(10)
radice.sinistro = NodoBinario(5)
radice.destro = NodoBinario(15)

# Aggiungere altri nodi
radice.sinistro.sinistro = NodoBinario(2)
radice.sinistro.destro = NodoBinario(7)
radice.destro.sinistro = NodoBinario(12)
radice.destro.destro = NodoBinario(20)

# Funzione per attraversare l'albero (esempio: visita in ordine)
def visita_in_ordine(nodo):
    if nodo is not None:
        visita_in_ordine(nodo.sinistro)
        print(nodo.valore, end=" ")
        visita_in_ordine(nodo.destro)

# Stampare i valori dell'albero in ordine
print("Visita in ordine:")
visita_in_ordine(radice)

# Output: Visita in ordine:2 5 7 10 12 15 20
