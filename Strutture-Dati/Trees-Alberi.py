# Classe Nodo per un albero
class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.figli = []  # Lista per contenere i figli

    def aggiungi_figlio(self, nodo):
        self.figli.append(nodo)

# Creazione dell'albero
radice = Nodo("Radice")

# Aggiungere figli alla radice
figlio1 = Nodo("Figlio 1")
figlio2 = Nodo("Figlio 2")
radice.aggiungi_figlio(figlio1)
radice.aggiungi_figlio(figlio2)

# Aggiungere figli ai nodi
figlio1.aggiungi_figlio(Nodo("Figlio 1.1"))
figlio1.aggiungi_figlio(Nodo("Figlio 1.2"))
figlio2.aggiungi_figlio(Nodo("Figlio 2.1"))

# Funzione per stampare l'albero
def stampa_albero(nodo, livello=0):
    print("  " * livello + str(nodo.valore))
    for figlio in nodo.figli:
        stampa_albero(figlio, livello + 1)

# Stampare l'albero
stampa_albero(radice)
