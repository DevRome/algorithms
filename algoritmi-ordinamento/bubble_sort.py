# .:: Algoritmi Ordinamento: Bubble Sort ::.
# da YouTube

# prende una unsorted list e la ordina confrontando gli elementi consecutivi


# Esempio 1
def bubble_sort(list):
    indexing_length = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list[i] > list[i + 1]:
                sorted = False
                # scambia il valore contenuto in list[i] con quello in list[i+1]
                list[i], list[i+1] = list[i+1], list[i]
    return list

print(bubble_sort([1,5,3,8,7])) 


# Esempio 2 - on doppio ciclo for
def bubble_sort_2(list):
    for i in range(len(list) - 1, 0, -1): # iteriamo sulla lista a ritroso
        for j in range(i): # iteriamo sugli elementi da 0 a i
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list
print(bubble_sort_2([2, 4, 3, 1]))