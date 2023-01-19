#User function Template for python3

class Solution:
    def sortedMatrix(self,N,Mat):
        #code here
        l = []
        for i in Mat:
            for j in i:
                l.append(j)
        l.sort()
        l1 = []
        l2 = []
        i = 0
        while i < (N*N):
            for j in range(i,i+N):
                l1.append(l[j])
            l2.append(l1)
            l1 = []
            i = i + N
        return l2


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        v=[]
        for i in range(N):
            a=list(map(int,input().strip().split()))
            v.append(a)
        ob=Solution()
        ans=ob.sortedMatrix(N,v)
        for i in range(N):
            for j in range(N):
                print(ans[i][j],end=" ")
            print()
# } Driver Code Ends