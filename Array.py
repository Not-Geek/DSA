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
    
## 6. Sort arrays of 0's, 1's and 2's
def sort012(self,arr,n):
    l = 0 
    h = n-1
    i=0
    while i<=h:
        if arr[i] == 0:
            arr[l], arr[i] = arr[i], arr[l]
            l+=1
            i+=1
        elif arr[i]==2:
            arr[h], arr[i] = arr[i], arr[h]
            h-=1
        else:
            i+=1
    return arr

## 7. Move positive to front of array
def segregateElements(self, arr, n):
    # Your code goes here
    ans_arr = []
    for i in range(n):
        if arr[i] >=0:
            ans_arr.append(arr[i])
    for i in range(n):
        if arr[i] < 0:
            ans_arr.append(arr[i])
    return ans_arr

## 8. Common element in 3 array
class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        diction = OrderedDict([])
        ans=[]
        for i in A:
            if i in diction and diction[i]==0:
                diction[i]+=1
            elif i not in diction:
                diction[i] = 1
        #print (diction)
        for i in B:
            if i in diction and diction[i]==1:
                diction[i]+=1
                
        #print (diction)
        for i in C:
            if i in diction and diction[i]==2:
                diction[i]+=1
        for i in diction:
            if diction[i]==3:
                ans.append(i)
        #print (diction)
        #print(ans)
        return ans
    
    ## 9. First repeating element
    def firstRepeated(self,arr, n):

    #arr : given array
    #n : size of the array
    dics = {}
    for i in range(n):
        if arr[i] in dics:
            dics[arr[i]] +=1
        else: 
            dics[arr[i]] = 1
    for i in range(n):
        if dics[arr[i]]>1 :
            return i+1
    return -1
