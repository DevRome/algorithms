from collections import deque 

class AhoCorasick: 
    def __init__(self, words): 
        self.words = words 
        self.max_states = sum(len(word) for word in words) 
        self.transitions = [{}] 
        self.fails = [0]
        self.outputs = [set()] 
        self.build_automaton() 
    
    def build_automaton(self): 
        for i, word in enumerate(self.words): 
            state = 0 
            for char in word: 
                if char in self.transitions[state]:
                    state = self.transitions[state][char] 
                else: 
                    self.transitions.append({}) 
                    self.fails.append(0) 
                    self.outputs.append(set()) 
                    new_state = len(self.transitions) - 1 
                    self.transitions[state][char] = new_state 
                    state = new_state
                    self.outputs[state].add(i) 
                    queue = deque() 
                    for char, state in self.transitions[0].items(): 
                        queue.append(state) 
                        self.fails[state] = 0 
                        while queue: state = queue.popleft()
                        for char, new_state in self.transitions[state].items(): 
                            queue.append(new_state) 
                            failure = self.fails[state] 
                            while failure and char not in self.transitions[failure]: 
                                failure = self.fails[failure] 
                            self.fails[new_state] = self.transitions[failure].get(char, 0) 
                            self.outputs[new_state] |= self.outputs[self.fails[new_state]]
    def search(self, text): 
        state = 0 
        results = [] 
        for i, char in enumerate(text): 
            while state and char not in self.transitions[state]: 
                state = self.fails[state] 
                state = self.transitions[state].get(char, 0) 
                for match in self.outputs[state]:
                    word = self.words[match] 
                    results.append((i - len(word) + 1, word)) 
                    return results 
                # Esempio di utilizzo 
                ac = AhoCorasick(["he", "she", "his", "hers"]) 
                print(ac.search("ushers"))