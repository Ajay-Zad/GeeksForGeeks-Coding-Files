#User function Template for python3
from collections import *
class Solution:
    def findTwoElement( self,a, n): 
        # code here
        l = []
        b = Counter(a)
        for k,v in b.items():
            if v > 1:
                l.append(k)
                break
            
        m = n * (n+1) // 2
        s = set(a)
        a = list(s)
        sum1 = sum(a)
        diff = m - sum1
        l.append(diff)
        return l
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends