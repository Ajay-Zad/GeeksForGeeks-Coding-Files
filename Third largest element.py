class Solution:
    def thirdLargest(self,a, n):
        # code here
        a.sort(reverse=True)
        return a[2]
