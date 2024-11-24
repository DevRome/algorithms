# .:: Selection Sort ::.
# Algorithms and Data Structures Tutorial - Full course for beginners 
# Youtube - FreeCode Camp

# lista di elementi non ordinati
unsortedList = [2,4,1,3,6,5]

# algoritmo
def selection_sort(list):
    
    sortedList = [] # inizializzazione lista ordinata (vuota)
    
    for i in range(0, len(list)):
         
         # troviamo l'indice del valore minimo della lista unsorted
         indexToMove = findMinIndex(list) 
         sortedList.append(list.pop(indexToMove))

         # OPT - visualizzo cosa succede
         print("%-25s %-25s" % (list, sortedList))
    return sortedList

def findMinIndex(list):

    minIndex = 0
    # troviamo l'indice corrispondente al valore minimo
    for i in range(1, len(list)): 
        # se il primo elemento della lista è maggiore del successivo, allora diventa valore minimo
        if list[i] < (list[minIndex]): minIndex = i
    return minIndex

print(selection_sort(unsortedList))