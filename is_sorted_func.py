# .:: controlla se una lista è ordinata o no ::.
# Algorithms and Data Structures Tutorial - Full course for beginners 
# Youtube - FreeCode Camp

numbersList = [1,3,2,4,5,6]

def is_sorted(myList):
    for index in range(len(myList) - 1):
        if myList[index] > myList[index + 1]: return False
    return True

print(is_sorted(numbersList))