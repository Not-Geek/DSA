## 1. Check if pallindrome 
def isPalindrome(self, A):
    low = 0
    high = len(A)-1

    while low < high :
        while low!=high and not A[low].isalnum():
            low+=1
        while low!=high  and not A[high].isalnum():
            high-=1
        if A[low].lower()!=A[high].lower():
            #print (A[low], A[high])
            return 0
        low+=1
        high-=1
    return 1

## 2. Remove consecutive characters
def solve(self, A, B):
    ans = ""
    i = 0
    while i < len(A):
        count = 1
        while i<len(A)-1 and A[i] == A[i+1]:
            count += 1
            i+=1
        for j in range(count%B):
            ans+=A[i]
        i+=1
    return ans
