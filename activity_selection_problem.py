# .:: Activity Selection Problem ::.
# Probelma della copertura delle attività
# UniMarconi - Corso Algoritmi e Strutture Dati

def activity_selection(attivita, inzio, fine):
    def recursive_selection(attivita, n, prev_end):
        if n == 0:
            return []
        first = attivita[0]
        if first[0] >= prev_end:
            return [first] + recursive_selection(attivita[1:], n - 1, first[1])
        else:
            return recursive_selection(attivita[1:], n -1, prev_end)
    
    attivita.sort(key=lambda x: x[1])
    return recursive_selection(attivita, len(attivita), inzio)

# esempio di utilizzo
attivita = [(1,4),(3,5), (0,6), (5,7), (3,8), (5,9), (6,10), (8,11)]
print(activity_selection(attivita, 0,0)) # output [(1,4), (5,7), (8,11)]
