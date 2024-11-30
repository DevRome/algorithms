# .:: LCS - Longest Common Subsequence - Programmazione dinamica::.
# Date due stringhe, trovare la lunghezza della loro sottosequenza comune più lunga

# risoluzione del problema KnapSack attraverso questa tecnica
# UniMarconi - Corso Algoritmi e Strutture Dati

def lcs(x, y):
    m = len(x)
    n = len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

x = "AGGTAB"
y = "GXTXAYB"
print(lcs(x, y)) # output 4