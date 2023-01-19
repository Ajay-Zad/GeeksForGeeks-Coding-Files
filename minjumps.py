#User function Template for python3
class Solution:
    def minJumps(self, arr, n):
        #code here
        sum = 0
        i = 0
        while True:
            sum = sum + arr[sum]
            i = i + 1
            if sum >= n:
                return i


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr,n)
        print(ans)
# } Driver Code Ends