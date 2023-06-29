def Insert(arr):
    compairs = 0
    swaps = 0
    ret = []
    compairing = []
    
    key = 1
    for i in range(1, len(arr)):
        for j in range(i):
            key = i-j
            if arr[key] < arr[key-1]:
                arr[key], arr[key-1] = arr[key-1], arr[key]
                swaps += 1
            compairing.append((key, key-1))
            ret.append(arr[:])
            compairs += 1

    return ret, swaps, compairs, compairing
            
            