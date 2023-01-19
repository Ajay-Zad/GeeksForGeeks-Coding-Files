#User function Template for python3

def missingNumber( A, N):
     # Your code goes here
     s = sum(A)
     s1 = 0
     for i in range(1,N+1):
         s1 = s1 + i
     return s1-s
         
     