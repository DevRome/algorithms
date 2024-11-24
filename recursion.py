# .:: Recursion ::.
# Algorithms and Data Structures Tutorial - Full course for beginners 
# Youtube - FreeCode Camp

# La ricorsione è l'abilita di una funzione di richiamare se stessa

# funzione con iterazione
def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


# l'equivalente in ricorsione sarebbe
def sum2(numbers):
    if not numbers:
        return 0
    print("Calling sum(%s)" % numbers[1:])
    remaining_sum = sum2(numbers[1:])
    print("Calling to sum(%s) returning %d + %d" % (numbers, numbers[0], remaining_sum))
    return numbers[0] + remaining_sum
    

numbers = [1,2,3,4]
print(sum(numbers))
print(sum2(numbers))