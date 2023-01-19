#User function Template for python3

class Solution:
    def getOddOccurrence(self, arr, n):
        # code here 
        s = set(arr)
        for i in s:
            if arr.count(i) % 2 == 1:
                return i
