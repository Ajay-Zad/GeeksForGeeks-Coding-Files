#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        i = 1
        f1 = 0
        f2 = 1
        l= []
        l.append(1)
        if n == 1:
            return l
        while i < n:
            f3 = f1 + f2
            f1 = f2
            f2 = f3
            l.append(f3)
            i = i + 1
        return l
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len (res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends