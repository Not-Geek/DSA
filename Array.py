## 1. PEAK ELEMENT

def peakElement(self,arr, n):
    # Code here
    ans = 0
    if n == 1 or arr[0] > arr[1]:
        return 0
    elif arr[n-1] > arr[n-2]:
        return n-1
    else:
        for i in range(1,n-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return i

## 2. Find minimum and maximum element in an array

def getMinMax( a, n):
    min_el = a[1]
    max_el = a[1]
    
    for i in a:
        if i < min_el :
            min_el = i
        if i > max_el :
            max_el = i
        
    return [min_el, max_el]
    
