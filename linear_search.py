"""
sdas
"""

def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target: return i
    return False

list = [1,2,3,4,5,6,7,8,9,10]
target = 6

result = linear_search(list, target)
print(f"posizione: {result}")