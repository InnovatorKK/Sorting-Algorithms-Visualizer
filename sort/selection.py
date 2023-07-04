def Selection(arr):
    compairs = 0
    swaps = 0
    ret = []
    compairing = []
    min = 0

    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j

            if i != min:      
                arr[i], arr[min] = arr[min], arr[i] 
                swaps += 1
            ret.append(arr[:])
            compairing.append((j, min))
                
            compairs += 1
            

    return ret, swaps, compairs, compairing
            
            