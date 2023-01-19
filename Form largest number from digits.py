#User function Template for python3

class Solution:
    def MaxNumber(self, arr, n):
        #code here.
        arr.sort(reverse=True)
        s = ""
        for i in arr:
            s = s + str(i)
        return s
        
    


