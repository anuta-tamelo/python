
def bubbleSort(array, cmp):
   for n in range(0, len(array)):
        for i in range(0, len(array) - 1 - n):
            if cmp(array[i], array[i + 1]): array[i], array[i + 1] = array[i + 1], array[i]

a = [1, 0, 5, 4, 2, 0]

def cmpLess(left, right):
    return left < right

def cmpGreat(left, right):
    return not cmpLess(left, right)

bubbleSort(a, cmpGreat)
print(a)