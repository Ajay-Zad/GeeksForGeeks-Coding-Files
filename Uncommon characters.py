#User function Template for python3

class Solution:
    def UncommonChars(self,A, B):
        #code here
        s = ""
        for i in A :
            if i not in B:
                if i not in s:
                    s = s + i
        for i in B:
            if i not in A:
                if i not in s:
                    s = s + i
        l = list(s)
        l.sort()
        s = ""
        for i in l:
            s = s + i
        if s == '':
            return -1
        else:
            return s

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends