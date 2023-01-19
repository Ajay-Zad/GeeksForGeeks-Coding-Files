#User function Template for python3

class Solution:
    def lastIndex(self, s):
        # code here
        s = s[::-1]
        s1 = s.find("1")
        if s1 == -1:
            return s1
        s2 = len(s)
        s3 = s2 - s1
        return (s3-1)

        
        

