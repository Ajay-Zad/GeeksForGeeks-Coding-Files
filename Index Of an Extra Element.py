class Solution:
    def findExtra(self,a,b,n):
        #add code here
        for i in range(0,len(b)):
            if a[i] != b[i]:
                return i
        else:
            return i+1
