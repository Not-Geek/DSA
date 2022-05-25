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

## 3. Reverse a list
test_cases = int(input())
for i in range(test_cases):
    length = int(input())
    arr = list(map(int, input().strip().split()))
    for i in arr[::-1]:
        print (i, end = " ")
        
        
## 4. Quick Sort
def quicksort(self, arr, low, high):
    if (low < high):
        pi = self.part(arr, low, high)
        self.quicksort(arr, low, pi-1)
        self.quicksort(arr, pi+1, high)

def part(self, arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i +=1
            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    return i+1

## 5. Subarray with given sum
class Solution:
    def subArraySum(self,arr, n, s): 
        l = 0
        temp = 0
        for i in range(n):
            temp+=arr[i]
            if temp > s:
                while(temp > s):
                    temp-=arr[l]
                    l+=1
            if temp==s:
                return [l+1,i+1]
        return [-1]
    
