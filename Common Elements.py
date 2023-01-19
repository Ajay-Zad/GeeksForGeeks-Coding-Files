#User function Template for python3

class Solution:
    def common_element(self,v1,v2):
        #code here
        l = []
        for i in v1:
            if i in v2:
                l.append(i)
        l.sort()
        return l