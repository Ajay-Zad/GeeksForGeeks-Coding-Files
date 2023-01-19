#User function Template for python3

class Solution:
    def required(self, a, n, k):
        # Your code goes here
        cnt = 0
        l = []
        for i in a:
            if i <= k:
                pass
            else:
                cnt = (i-k)
                l.append(cnt)  
                k = i
        
        if cnt > 0:
            return sum(l)
        else:
            return -1
    

