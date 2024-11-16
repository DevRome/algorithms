# .:: Merge Sort ::.

def merge_sort(list):
    # sort a list in ascending order

    # check preliminare
    if len(list) <= 1: return list

    # trova il punto medio della lista e divide in sublist
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right =merge_sort(right_half)

    # ricorsivamente ordina le sottoliste create in precedenza 

    # rimette insieme le sottoliste create ed ordinate

    # restituisce la nuova lista
    return merge(left, right)

def split(list):
    # divide la lista unsorted dal punto di mezzo(midpoint) in sottoliste
    # restituisce due sottoliste - left e right
    
    midpoint = len(list) // 2
    left = list[:midpoint] # dall'inzio della lista al midpoint
    right = list[midpoint:] # dal midpoint alla fine della lista
    return left, right    

def merge(left, right):
    # unisce due array, ordinandoli nel processo
    # restituisce una nuova lista unita ed ordinata

    l = []
    i = 0 # indice dell' array left
    j = 0 # indice dell' array right

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    
    while i < len(left):
        l.append(left[i])
        i+=1
    
    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l

# lista da ordinare
list = [1,3,2,6,5,9,8,7]
newList = merge_sort(list)
print(newList)