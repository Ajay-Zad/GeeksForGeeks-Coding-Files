from collections import *
class Solution:
    def duplicates(self, arr, n): 
        # code here
        b = Counter(arr)
        l = []
        cnt = 0
        for i,j in b.items():
            if j > 1:
                l.append(i)
                cnt = 1
        if cnt == 1:
            l.sort()
            return l
        else:
            l.append(-1)
            return l
            
         
        
        
            
