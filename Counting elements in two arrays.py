#User function Template for python3

class Solution:
    def countEleLessThanOrEqual(self,arr1,n1,arr2,n2):
        #returns the required output
        l = []
        for i in arr1:
            cnt = 0
            for j in arr2:
                if i >= j:
                    cnt = cnt + 1
            l.append(cnt)
        return l
    
