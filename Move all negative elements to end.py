#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        n = []
        p = []
        s = []
        for i in arr:
            if i < 0:
                n.append(i)
            else:
                p.append(i)
        s = p + n 
        for i in range(0,len(s)):
            arr[i] = s[i]