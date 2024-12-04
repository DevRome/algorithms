def rabin_karp_search(text, pattern): 
    d = 256 # Numero di caratteri nell'alfabeto 
    q = 101 # Un numero primo 
    m = len(pattern) 
    n = len(text) 
    p = t = 0 # hash value per pattern e text 
    h=1

    for i in range(m-1): 
        h = (h * d) % q 
        
        # Calcolo dell'hash iniziale 
        for i in range(m): 
            p = (d * p + ord(pattern[i])) % q 
            t = (d * t + ord(text[i])) % q

            for i in range(n - m + 1): 
                if p == t: 
                    if pattern == text[i:i+m]: 
                        print(f"Pattern trovato all'indice {i}") 
                        if i < n - m: 
                            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q 
                            if t < 0: 
                                t += q