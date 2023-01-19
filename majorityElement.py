#User function template for Python 3
from collections import *
class Solution:
    def majorityElement(self, A, N):
        #Your code here
        b = Counter(A)
        for i,j in b.items():
            if j > (N/2):
                return i
        else:
            return -1
