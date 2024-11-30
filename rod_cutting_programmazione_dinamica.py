# .:: Rod Cutting Problem - Programmazione Dinamica ::.
# Data un'asta di lunghezza n e una tabella dei prezzi per ogni lunghezza, determinare il massimo ricavo ottenibile tagliando e vendendo l'asta.

# risoluzione del problema KnapSack attraverso questa tecnica
# UniMarconi - Corso Algoritmi e Strutture Dati

def rod_cutting(prezzi, n):
    dp = [0] * (n+1)
    for i in range(1, n + 1):
        max_val = float("-inf")
        for j in range(i):
            max_val = max(max_val, prezzi[j] + dp[i - j -1])
        dp[i] = max_val
    return dp[n]

prezzi = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
print(rod_cutting(prezzi, n)) # output 22