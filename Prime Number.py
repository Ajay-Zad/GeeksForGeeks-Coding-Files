#User function Template for python3

class Solution:
    def isPrime (self, N):
        # code here
        flag = 0
        if N <= 0 or N == 1:
            return 0
        for i in range(2,(N//2)+1):
            if N % i == 0:
                flag = 1
                break
        if flag == 0:
            return 1
        else:
            return 0
            
