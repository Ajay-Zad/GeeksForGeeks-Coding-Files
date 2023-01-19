class Solution:
    def checkFib(self,arr, N):
        # Your code goes here
        i = 1
        f1 = 0
        f2 = 1
        l= []
        if 0 in arr:
            l.append(0)
        f3 = 0
        while f3 <= max(arr):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
            l.append(f3)
            i = i + 1
        l1 = []
        for i in arr:
            if i in l:
                l1.append(i)
        return len(l1)
                


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a = list(map(int,input().split()))
        ob=Solution()
        ans=ob.checkFib(a,n)
        print(ans)
# } Driver Code Ends