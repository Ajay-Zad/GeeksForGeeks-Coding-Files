#User function Template for python3
class Solution:

    def print2largest(self,arr, n):
        # code here
        s = set(arr)
        arr = list(s) 
        arr.sort(reverse=True)
        if len(arr) == 1:
            return -1
        else:
            return arr[1]
