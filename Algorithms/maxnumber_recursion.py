def max(fst, snd):
    if fst > snd: 
        return fst
    else:
        return snd


def max_number(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    else:
        arg = max_number(arr[1:])
        return max(arr[0], arg )

print(max_number([0, 12, 17, 24, 3, 78]))
