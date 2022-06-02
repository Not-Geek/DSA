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
