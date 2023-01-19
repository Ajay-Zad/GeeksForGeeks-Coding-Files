#User function Template for python3

class Solution:

    def firstRepChar(self, s):
        # code here
        s1 = ""
        for i in s:
            if i in s1:
                return i
            else:
                s1 = s1 + i
        else:
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.firstRepChar(s))
# } Driver Code Ends