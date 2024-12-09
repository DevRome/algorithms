# .:: Coin Change Problem ::.
# algoritmo Greedy

def coin_change_greedy(coins, target):
    coins.sort(reverse=True)  # Ordina le monete in ordine decrescente
    count = 0
    for coin in coins:
        if target == 0:
            break
        # Usa quante più monete possibili della denominazione corrente
        num_coins = target // coin
        count += num_coins
        target -= num_coins * coin

    # Se non è possibile raggiungere esattamente il target, restituisci -1
    return count if target == 0 else -1

# Esempio di utilizzo
coins = [1, 2, 5]
target = 11
print("Minimo numero di monete (Greedy):", coin_change_greedy(coins, target))  # Output: 3 (5+5+1)
