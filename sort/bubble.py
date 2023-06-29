def Bubble(arr):
    compairs = 0
    swaps = 0
    ret = []
    compairing = []

    for i in range(len(arr)-1):
        issorted = True
        for node in range(len(arr)-1-i):
            
            if arr[node] > arr[node+1]:
                arr[node], arr[node+1] = arr[node+1], arr[node]
                swaps += 1
                issorted = False
            compairing.append((node, node+1))
            ret.append(arr[:])
            compairs += 1
            
        if issorted:
            break
        
    return ret, swaps, compairs, compairing