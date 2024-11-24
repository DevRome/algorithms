
# .:: Selection Sort ::.
# Algoritmo elaborato da me

# lista di elementi non ordinati
unsortedList = [1,4,2]


# algoritmo
def selection_sort(list):
    
    sortedList = [] # inizializzazione lista ordinata (vuota)
    
    # inizio l'iterazione per ottenere un elemento da confrontare con gli altri elementi della lista
    for i in range(0, len(list)):

        # imposto l'indice iniziale al primo elemento della lista
        # andrò a far partire il confronto su questo elemento e lo userò come pivot
        minIndex = i 
        
        # con il secondo for, scorro gli elementi della lista confrontandoli con il pivot
        for j in range(0, len(list)):
            
            print(f"minIndex: {minIndex}")
            # non fa uscire il conto degli index fuori dal range
            if minIndex > len(list) - 1: minIndex = 0

            # eseguo il confronto tra il pivot e gli elementi della lista
            # se l'elemento confrontato con il pivot è minore del pivot, allora quello diventa il minIndex (nuovo pivot)
            print(f"confronto j: {list[j]} con indice attuale: {list[minIndex]}")
            if list[j] < list[minIndex]: minIndex = j
        
        # aggiungo alla nuova lista ordinata il valore minimo trovato
        sortedList.append(list[minIndex])
        print(sortedList)

        # elimino l'elemento minimo trovato dalla vecchia lista
        list.pop(minIndex)

    # stampo la lista 
    print(sortedList)
                

# richiamo algoritmo
selection_sort(unsortedList)

