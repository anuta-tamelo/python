def find_smallest(arr, si):
    smallest = arr[si]
    smallest_index = si
    for i in range(si, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    for i in range(0, len(arr)):
        smallest = find_smallest(arr, i)
        arr[smallest], arr[i] = arr[i], arr[smallest]
    return arr


print(selectionSort([3, 4, 6, 0, 1] ))
