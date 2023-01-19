#User function Template for python3

class Solution:
    def distinct(self, M, N):
        # code here
        l = []
        for i in M:
            ii = set(i)
            for j in ii:
                l.append(j)
        
        s1 = set(l)
        l2 = []
        for i in s1:
            if l.count(i) >= N:
               l2.append(i) 
        return len(l2)
