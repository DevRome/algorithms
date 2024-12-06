# Linear Search with strings
# Algorithms and Data Structures Tutorial - Full course for beginners 
# Youtube - FreeCode Camp

names = [
    "Lorenzo Raspa",
    "Andrea Cantarini",
    "Daniele Lucarini",
    "Michele Bellomo",
    "Cumparello Porcello",
    "Maurello Lello Lello"
]

def linear_search(list, target):
    for i in range(0, len(list)):
        if target == list[i]:
            return i
    return None

print(linear_search(names, "Andrea Cantarini"))
