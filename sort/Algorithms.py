class Algorithms(object):
    def __init___(self):
        pass
    
    def Bubble(self, arr):
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
    
    def Insert(self, arr):
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

    def Selection(self, arr):
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
                compairs += 1
                compairing.append((j, min))
                ret.append(arr[:])

    
            arr[i], arr[min] = arr[min], arr[i] 
            swaps += 1
                    
                

        return ret, swaps, compairs, compairing