#User function Template for python3


# function for adding one to number 
class Solution:
    def addOne(self,a, n):
        # code here
        s = ""
        for i in a:
            s = s + str(i)
        s1 = int(s) + 1
        s2 = str(s1)
        a = []
        for i in s2:
            a.append(i)
        return a
        