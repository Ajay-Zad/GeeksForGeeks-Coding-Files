#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        s = range(1,n+1)
        s1 = sum(s)
        s2 = sum(array)
        
        diff = s1 - s2
        return diff


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends