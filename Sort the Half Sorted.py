#User function Template for python3

class Solution:
    def sortHalves (self, arr, n):
        # your code here
        return arr.sort()

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    arr = list(map(int, input().split()))
    ob = Solution()
    ob.sortHalves (arr, n)
    
    for i in range (n):
        print (arr[i], end = " ")
    print ()
    
# Contributed By: Pranay Bansal
# } Driver Code Ends