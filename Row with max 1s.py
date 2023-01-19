#User function Template for python3
class Solution:

    def rowWithMax1s(self,arr, n, m):
        # code here
        cnt = 0
        ii = 0
        m = 0
        for i in arr:
            ii = ii + 1
            if i.count(1) > cnt:
                cnt = i.count(1)
                m = ii
        return m-1