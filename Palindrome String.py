#User function Template for python3
class Solution:
    def isPalindrome(self, S):
        # code here
        s1 = S[::-1]
        if s1 == S:
            return 1
        else:
            return 0
