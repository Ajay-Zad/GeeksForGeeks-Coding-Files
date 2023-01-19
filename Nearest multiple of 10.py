#User function Template for python3

class Solution:
    def roundToNearest (self, N) : 
        #Complete the function
        N = int(N)
        N1 = N
        if N % 5 == 0 and N % 10 != 0:
            print(N-5)
        else:
            while N % 10 != 0:
                N = N + 1
            a = N
            b = N - 10
            
            c = a - N1
            if c <= 5:
                a = str(a)
                return a
            else:
                b = str(b)
                return b
                

