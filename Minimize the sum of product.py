#User function Template for python3

class Solution:
    def minValue(self, a, b, n):
        # Your code goes here
        a.sort()
        b.sort(reverse=True)
        sum = 0
        for i,j in zip(a,b):
            sum = sum + (i*j)
        return sum
        

