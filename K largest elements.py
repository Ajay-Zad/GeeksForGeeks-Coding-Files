#User function Template for python3

class Solution:
    #Function to return k largest elements from an array.
    def kLargest(self,li,n,k):
        # code here
        li.sort(reverse=True)
        l = []
        for i in range(0,k):
            l.append(li[i])
        return l
        
