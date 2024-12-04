def boyer_moore_search(text, pattern): 
    m = len(pattern) 
    n = len(text) 
    # Preprocessing 
    bad_char = bad_char_heuristic(pattern, m)
    i=0 
    while i <= n - m: 
        j=m-1 
        while j >= 0 and pattern[j] == text[i + j]: 
            j -= 1 
            if j < 0: 
                print(f"Pattern trovato all'indice {i}") 
                i += (m - bad_char[ord(text[i + m])] if i + m < n else 1)
            else: 
                i += max(1, j - bad_char[ord(text[i + j])]) 

def bad_char_heuristic(pattern, size): 
    bad_char = [-1] * 256 
    for i in range(size): 
        bad_char[ord(pattern[i])] = i 
        return bad_char
