# .:: Binary Search ::.
# Algorithms and Data Structures Tutorial - Full course for beginners 
# Youtube - FreeCode Camp

def binary_search(list, target):
    first = 0 # primo elemento della lista
    last = len(list) - 1 # ultimo elemento della lista (partendo da 0)

    while first <= last:

        # mi posiziono al centro della list
        midpoint = (first + last) // 2 # // arrotonda al numero più basso

        if list[midpoint] == target: return midpoint
        elif list[midpoint] < target: first = midpoint + 1
        elif list[midpoint] > target: last = midpoint - 1
    
    return None # se non ha trovato niente


# Nel binary search la list DEVE essere ordinata!!
list = [1,2,3,4,5,6,7,8,9,10]
target = 11
result = binary_search(list, target)
print(result)