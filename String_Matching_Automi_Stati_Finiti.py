class FSA: 
    def __init__(self, pattern): 
        self.pattern = pattern 
        self.M = len(pattern) 
        self.transitions = {} 
        self.build_transitions()
    
    def build_transitions(self): 
        for q in range(self.M + 1): 
            for char in set(self.pattern): 
                k = min(self.M, q + 1) 
                while k > 0 and self.pattern[:k] != self.pattern[q-k+1:q] + char: 
                    k -= 1 
                self.transitions[(q, char)] = k
    
    def search(self, text): 
        n = len(text) 
        q=0 
        results = [] 
        for i in range(n): 
            q = self.transitions.get((q, text[i]), 0) 
            if q == self.M: 
                results.append(i - self.M + 1) 
            return results

# Esempio di utilizzo 
fsa = FSA("ABABC") 
print(fsa.search("ABABABCABABABC"))
