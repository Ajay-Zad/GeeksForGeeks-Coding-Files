#User function Template for python3

class Solution:
    def factorial(self, N):
        #code here
        sum = 1
        for i in range(1,N+1):
            sum = sum * i
        s = str(sum)
        return s

            