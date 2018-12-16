def sum(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1: 
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])

print(sum([2, 4, 6, 8, 10]))

