# .:: KnapSack Problem - Programmazione Dinamica ::.
# Dato un insieme di oggetti ciascuno con un peso e un valore, determinare il valore massimo che può essere ottenuto mettendo oggetti in un knapsack di capacità limitata.

# risoluzione del problema KnapSack attraverso questa tecnica
# UniMarconi - Corso Algoritmi e Strutture Dati

def knapsack(pesi, valori, capacita):
    n = len(pesi)
    dp = [[0] * (capacita + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacita + 1):
            if pesi[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - pesi[i - 1]] + valori[i - 1])
            else:
                dp[i][w] = dp[1 - 1][w]
    return dp[n][capacita]

pesi = [10, 20, 30]
valori = [60, 100, 120]
capacita = 50

print(knapsack(pesi, valori, capacita))