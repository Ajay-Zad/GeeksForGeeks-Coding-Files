#User function Template for python3
class Solution:

    def maxRepeating(self,arr, n, k):
        # code here
        s = set(arr)
        l1 = []
        j = 0
        j1 = 0
        for i in s:
            j = arr.count(i)
            if j >= j1:
                j1 = j
        l1 = []
        for i in s:
           if arr.count(i) == j1:
               l1.append(i)
        return min(l1)
                  
            
            
