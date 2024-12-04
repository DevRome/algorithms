def kmp_search(text, pattern): 
    m = len(pattern) 
    n = len(text) 
    
    # Calcolo della tabella dei prefissi 
    lps = [0] * m 
    compute_lps_array(pattern, m, lps)
    i=j=0 
    while i < n: 
        if pattern[j] == text[i]: 
            i += 1 
            j += 1 
        if j == m:
            print(f"Pattern trovato all'indice {i-j}")
            j = lps[j-1] 
        elif i < n and pattern[j] != text[i]:
            if j != 0: 
                j = lps[j-1] 
            else: i += 1 

def compute_lps_array(pattern, m, lps): 
    len = 0 
    lps[0] = 0 
    i=1

    while i < m: 
        if pattern[i] == pattern[len]: 
            len += 1 
            lps[i] = len 
            i += 1 
        else: 
            if len != 0: 
                len = lps[len-1]
            else: lps[i] = 0 
            i += 1