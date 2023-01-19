#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        A.sort()
        a = 0
        b = M
        l = []
        B = []
        while True:
            if b == len(A)+1:
                break
            B = A[a:b]
            d = B[len(B)-1] - B[0]
            l.append(d)
            a = a + 1
            b = b + 1
        return min(l)

