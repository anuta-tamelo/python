
def bubbleSort(array, cmp):
   for n in range(0, len(array)):
        for i in range(0, len(array) - 1 - n):
            if cmp(array[i], array[i + 1]): array[i], array[i + 1] = array[i + 1], array[i]

a = [1, 0, 5, 4, 2, 0]

#bubbleSort(a, lambda left, right: left > right)
print(a[::-2])