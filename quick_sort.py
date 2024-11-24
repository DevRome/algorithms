# .:: Quick Sort ::.
# Algorithms and Data Structures Tutorial - Full course for beginners 
# Youtube - FreeCode Camp

# quick sort - è ricorsivo, chiama se stesso più volte
# usiamo la filosofi divide and conquer:
# quindi dividiamo il problema in sottoproblemi più piccoli

def quicksort(values): 
    
    # se l'array iniziale e < 1 o vuoto allora restituisce direttamente quello
    if(len(values)) <= 1:
        return values
    
    # inizializzo i primi 3 subarray: 
    # pivot (val.iniziale), subarray > pivot, subarray < pivot
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]

    # controllo i valori di tutti gli elementi dell'array, confrontandoli con il pivot
    # li inserisco nella lista corrsipondente
    for value in values[1:]:
        if value <= pivot: less_than_pivot.append(value)
        else: greater_than_pivot.append(value)

    # stampo a video per vedere che succede
    print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))

    # ricorsione: richiamo il quick sort anche per gli subarray dei subarray
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

# genera numero e richiama funzione
numbers = [3,2,6,5,7,1,4]
sorted_numbers = quicksort(numbers)
print(sorted_numbers)