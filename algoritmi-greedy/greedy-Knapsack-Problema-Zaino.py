# .:: Knapsack Problem - problema dello zaino ::.
# algoritmo Greedy

def knapsack_greedy(weights, values, W):
    n = len(values)
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    items.sort(reverse=True, key=lambda x: x[0])  # Ordina per valore/peso decrescente
    
    total_value = 0
    total_weight = 0
    
    for ratio, weight, value in items:
        if total_weight + weight <= W:
            total_weight += weight
            total_value += value
        else:
            break
    
    return total_value

# Esempio di utilizzo
weights = [4, 5, 6]
values = [3, 4, 5]
W = 8
print("Valore massimo (Greedy):", knapsack_greedy(weights, values, W))  # Output: 7
