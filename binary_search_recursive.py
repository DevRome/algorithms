def binary_search_recursive(list, target):
    
    # se la lista è vuota restituisce False
    if len(list) == 0: return False

    else:

        # calcolo midpoint della lista
        midpoint = (len(list)) // 2  # // restituisce solo parte intera
        
        # se il midpoint coincide con il target, restituisce il midpoint
        if list[midpoint] == target: return midpoint

        else:
            if list[midpoint] < target: return binary_search_recursive(list[midpoint+1:], target)
            else: return binary_search_recursive(list[:midpoint], target)


list = [1,2,3,4,5,6,7,8,9,10]
target = 5
result = binary_search_recursive(list, target)
print(result)