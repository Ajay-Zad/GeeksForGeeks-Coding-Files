#User function Template for python3

class Solution:
    def searchInsertK(self, Arr, N, k):
        # code here
        if k in Arr:
            a = Arr.index(k)
            return a
        else:
            cnt = 0
            for i in Arr:
                if i < k:
                    cnt = cnt + 1
                else:
                    return cnt
            else:
                return len(Arr)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends