# .:: Merge Sort - Recursion::.
# Algorithms and Data Structures Tutorial - Full course for beginners 
# Youtube - FreeCode Camp

def merge_sort(values):

    # check preliminare, 
    # se array contiene solo 1 numero o vuoto, restituisce l'array
    if(len(values)<= 1): return values

    # pivot (metà dell'array originale approssimato per difetto)
    middle_index = len(values) // 2

    # facciamo una divisione dei valori dell'array in base al pivot (valore medio arrotondato per difetto)
    left_values = merge_sort(values[:middle_index])
    right_values = merge_sort(values[middle_index:])
    
    # ** stampo a video per vedere
    #print("%15s %-15s" % (left_values, right_values))

    sorted_values = []
    
    left_index = 0
    right_index = 0
    
    while left_index < len(left_values)and right_index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1

        sorted_values += left_values[left_index:]
        sorted_values += right_values[right_index:]
        return sorted_values


numbers = [1,5,3,7,6,4,9,2]
print(merge_sort(numbers))
